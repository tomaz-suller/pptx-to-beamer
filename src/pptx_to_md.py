from pathlib import Path

from models import Presentation


def pptx_to_md(input_dir: Path, output_dir: Path) -> None:
    for pptx_path in input_dir.glob('*.pptx'):
        name = pptx_path.stem
        presentation = Presentation.read(pptx_path)
        presentation_output_dir = output_dir / name
        presentation_output_dir.mkdir(parents=True)
        presentation.save(presentation_output_dir)


if __name__ == '__main__':
    import argparse

    from helper import get_input_output_dir_parser

    parser = argparse.ArgumentParser(
        description='Convert PowerPoint presentations to Markdown files'
    )
    parser = get_input_output_dir_parser(parser)
    args = parser.parse_args()
    pptx_to_md(args.input_dir, args.output_dir)
