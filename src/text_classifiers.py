"""Adapted from the `parser` module of [`pptx2md`](https://github.com/ssine/pptx2md)"""

from pptx.enum.dml import MSO_COLOR_TYPE, MSO_THEME_COLOR
from pptx.enum.shapes import PP_PLACEHOLDER


def is_title(shape):
    return (
        shape.is_placeholder
        and (
            shape.placeholder_format.type in [
                PP_PLACEHOLDER.TITLE,
                PP_PLACEHOLDER.SUBTITLE,
                PP_PLACEHOLDER.VERTICAL_TITLE,
                PP_PLACEHOLDER.CENTER_TITLE,
            ]
        )
    )


def is_accent(font):
    return (
        font.underline
        or font.italic
        or (
            font.color.type == MSO_COLOR_TYPE.SCHEME
            and font.color.theme_color in [
                MSO_THEME_COLOR.ACCENT_1,
                MSO_THEME_COLOR.ACCENT_2,
                MSO_THEME_COLOR.ACCENT_3,
                MSO_THEME_COLOR.ACCENT_4,
                MSO_THEME_COLOR.ACCENT_5,
                MSO_THEME_COLOR.ACCENT_6,
            ]
        )
    )

def is_strong(font):
    return (
        font.bold
        or (
            font.color.type == MSO_COLOR_TYPE.SCHEME
            and font.color.theme_color in [
                MSO_THEME_COLOR.DARK_1,
                MSO_THEME_COLOR.DARK_2
            ]
        )
    )
