import argparse
from pathlib import Path

def get_input_output_dir_parser(
        parser: argparse.ArgumentParser
) -> argparse.ArgumentParser:
    parser.add_argument(
        'input_dir',
        type=Path,
        help='Path to directory containing PowerPoint presentations',
    )
    parser.add_argument(
        'output_dir',
        type=Path,
        help='Path to save generated Markdown files to',
    )

    return parser
