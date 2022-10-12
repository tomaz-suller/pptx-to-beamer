import argparse
from pathlib import Path

def get_input_output_dir_parser(
        parser: argparse.ArgumentParser
) -> argparse.ArgumentParser:
    parser.add_argument(
        'input_dir',
        type=Path,
        help='Input directory',
    )
    parser.add_argument(
        'output_dir',
        type=Path,
        help='Output directory',
    )

    return parser
