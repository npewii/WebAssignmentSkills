import argparse
import sys
import fnmatch
import pyperclip
import tomllib
from dataclasses import dataclass
from pathlib import Path
from collections.abc import Iterator

CONFIG_FILE = Path('extractor.config.toml')


@dataclass
class ExtractorConfig:
    include_file_pattern: list[str]
    exclude_file_pattern: list[str]
    exclude_dir_pattern: list[str]
    max_depth: int
    strip: bool
    directories: list[Path]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='extractor',
        description='Extract files whose names match the specified patterns and combine them.',
    )

    parser.add_argument(
        'directories',
        nargs='*',
        default=[Path('.')],
        type=Path,
        help='directories to search',
    )

    parser.add_argument(
        '-i',
        '--include',
        dest='include_file_pattern',
        nargs='+',
        default=['*'],
        help='file patterns to include',
    )

    parser.add_argument(
        '-e',
        '--exclude',
        dest='exclude_file_pattern',
        nargs='+',
        default=[],
        help='file patterns to exclude',
    )

    parser.add_argument(
        '-E',
        '--exclude-dir',
        dest='exclude_dir_pattern',
        nargs='+',
        default=[],
        help='directory patterns to exclude',
    )

    parser.add_argument(
        '-d',
        '--depth',
        dest='max_depth',
        type=int,
        default=sys.maxsize,
        help='maximum directory depth',
    )

    parser.add_argument(
        '-s',
        '--strip',
        action='store_true',
        help='strip trailing whitespace and blank lines',
    )

    return parser


def iter_files(
    directories: list[Path],
    include_file_pattern: list[str],
    exclude_file_pattern: list[str],
    exclude_dir_pattern: list[str],
    max_depth: int
) -> Iterator[Path]:
    for directory in directories:
        if not directory.is_dir():
            sys.exit(f'{directory}: not a directory')

        root_depth = len(directory.parts)

        for path in directory.rglob('*'):
            if len(path.parts) - root_depth > max_depth:
                continue

            if not path.is_file():
                continue

            relative = path.relative_to(directory)

            if any(
                fnmatch.fnmatch(part, pattern)
                for part in relative.parts[:-1]
                for pattern in exclude_dir_pattern
            ):
                continue

            if not any(
                fnmatch.fnmatch(path.name, pattern)
                for pattern in include_file_pattern
            ):
                continue

            if any(
                fnmatch.fnmatch(path.name, pattern)
                for pattern in exclude_file_pattern
            ):
                continue

            yield path


def extract(path: Path, strip: bool) -> str | None:
    try:
        with path.open('r', encoding='utf-8') as f:
            if not strip:
                return f.read()

            return ''.join(stripped + '\n' for line in f if (stripped := line.rstrip()))
    except UnicodeDecodeError:
        return None


def get_config_from_args(args: argparse.Namespace) -> ExtractorConfig:
    return ExtractorConfig(
        include_file_pattern=args.include_file_pattern,
        exclude_file_pattern=args.exclude_file_pattern,
        exclude_dir_pattern=args.exclude_dir_pattern,
        max_depth=args.max_depth,
        strip=args.strip,
        directories=args.directories,
    )


def load_config_from_toml(args: argparse.Namespace) -> ExtractorConfig:
    try:
        with CONFIG_FILE.open('rb') as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        return get_config_from_args(args)
    except tomllib.TOMLDecodeError as e:
        sys.exit(f'config parse error: {e}')

    return ExtractorConfig(
        include_file_pattern=data.get(
            'include_file_pattern', args.include_file_pattern),
        exclude_file_pattern=data.get(
            'exclude_file_pattern', args.exclude_file_pattern),
        exclude_dir_pattern=data.get(
            'exclude_dir_pattern', args.exclude_dir_pattern),
        max_depth=data.get('max_depth', args.max_depth),
        strip=data.get('strip', args.strip),
        directories=[Path(d) for d in data['directories']
                     ] if 'directories' in data else args.directories,
    )


def build_content(config: ExtractorConfig) -> str:
    parts: list[str] = []

    for path in sorted(iter_files(
        config.directories,
        config.include_file_pattern,
        config.exclude_file_pattern,
        config.exclude_dir_pattern,
        config.max_depth,
    )):
        content = extract(path, config.strip)

        if content is None:
            continue

        parts.append(f'========== {path} ==========\n')
        parts.append(content)
        parts.append('\n')

    return ''.join(parts)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    config = get_config_from_args(args) if len(
        sys.argv) > 1 else load_config_from_toml(args)

    content = build_content(config)

    print(content)
    pyperclip.copy(content)


if __name__ == '__main__':
    main()
