import argparse
import shutil
from pathlib import Path

from helper import get_input_output_dir_parser

parser = argparse.ArgumentParser(
    'Rename files based on RENAME_DICT'
)
parser.add_argument(
    '--rename-filename',
    type=str,
    help='Path to rename key file, relative to the input directory',
    default='rename.txt',
)
parser = get_input_output_dir_parser(parser)

args = parser.parse_args()
input_dir: Path = args.input_dir
rename_filename: str = args.rename_filename
rename_filepath = input_dir / rename_filename

rename_dict = {filepath.name: filepath.name for filepath in input_dir.glob('*.pptx')}
rename_file_dict: dict[str, str] = {}

if rename_filepath.exists():
    with open(rename_filepath, encoding='utf8') as f:
        lines = f.readlines()
    for line in lines:
        old_name, new_name = (value.strip() for value in line.split(','))
        rename_file_dict[old_name] = new_name

rename_dict = {**rename_dict, **rename_file_dict}
for old_name, new_name in rename_dict.items():
    shutil.copy(
        input_dir / old_name,
        args.output_dir / new_name,
    )
