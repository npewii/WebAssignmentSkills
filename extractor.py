import argparse
import sys
import fnmatch
import pyperclip
from pathlib import Path
from collections.abc import Iterator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='extractor',
        description='Extract files whose names match the specified patterns and combine them.',
    )

    parser.add_argument(
        'directories',
        nargs='*',
        default=['.'],
        help='directories to search',
    )

    parser.add_argument(
        '--include-file-pattern',
        action='append',
        default=[],
        help='file patterns to include',
    )

    parser.add_argument(
        '--exclude-file-pattern',
        action='append',
        default=[],
        help='file patterns to exclude',
    )

    parser.add_argument(
        '--exclude-dir-pattern',
        action='append',
        default=[],
        help='directory patterns to exclude',
    )

    parser.add_argument(
        '--max-depth',
        type=int,
        default=sys.maxsize,
        help='maximum directory depth',
    )

    parser.add_argument(
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
        root_depth = len(directory.parts)

        for path in directory.rglob('*'):
            depth = len(path.parts) - root_depth

            if depth > max_depth:
                continue

            if not path.is_file():
                continue

            if any(
                fnmatch.fnmatch(parent.name, pattern)
                for parent in path.parents
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


def extract(path: Path, strip: bool) -> str:
    try:
        with path.open('r', encoding='utf-8') as f:
            if not strip:
                return f.read()

            parts: list[str] = []

            for line in f:
                line = line.rstrip()

                if not line:
                    continue

                parts.append(line + '\n')

            return ''.join(parts)

    except UnicodeDecodeError:
        return ''


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    result: list[str] = []

    for path in iter_files(
        [Path(p) for p in args.directories],
        args.include_file_pattern or ['*'],
        args.exclude_file_pattern,
        args.exclude_dir_pattern,
        args.max_depth
    ):
        result.append(f'========== {path.name} ==========\n')
        result.append(extract(path, args.strip))
        result.append('\n')

    content: str = ''.join(result)

    print(content)
    pyperclip.copy(content)


if __name__ == '__main__':
    main()
