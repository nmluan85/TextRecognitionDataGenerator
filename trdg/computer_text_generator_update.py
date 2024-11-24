import random as rnd
import os
from typing import Tuple
from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont
from PIL.ImageColor import getrgb

from trdg.utils import get_text_width, get_text_height

# Thai Unicode reference: https://jrgraphix.net/r/Unicode/0E00-0E7F
TH_TONE_MARKS = [
    "0xe47",
    "0xe48",
    "0xe49",
    "0xe4a",
    "0xe4b",
    "0xe4c",
    "0xe4d",
    "0xe4e",
]
TH_UNDER_VOWELS = ["0xe38", "0xe39", "\0xe3A"]
TH_UPPER_VOWELS = ["0xe31", "0xe34", "0xe35", "0xe36", "0xe37"]
GRAYSCALE_COLORS = [
    "#000000", "#141414", "#282828", "#3C3C3C", "#505050", "#646464", 
    "#787878", "#8C8C8C", "#A0A0A0", "#B4B4B4", "#C8C8C8", "#DCDCDC", 
    "#F0F0F0", "#FFFFFF"
]
def _get_valid_font_from_directory(font_directory: str, text: str, min_font_size: int, max_font_size: int) -> ImageFont:
    # List all font files in the directory
    font_files = [f for f in os.listdir(font_directory) if f.endswith(".ttf")]
    
    # Try random fonts until one can display the text
    # while True:
        # Randomly choose a font file from the directory
    font_file = rnd.choice(font_files)
    font_path = os.path.join(font_directory, font_file)
    font_size = rnd.randint(min_font_size, max_font_size)
    print(font_size)
    image_font = ImageFont.truetype(font_path, 20)
    return image_font, font_size
    # # Randomly select a font size between min_font_size and max_font_size
    # text_width, text_height = image_font.getsize(text)
    # if text_width > 0 and text_height > 0:
    #     return image_font, font_size  # Return the valid font
    # try:
        #     # Load the font with the random size
        #     image_font = ImageFont.truetype(font_path, font_size)
            
        #     # Create a dummy image to check if the font can render the text
        #     img = Image.new("RGB", (100, 100))
        #     draw = ImageDraw.Draw(img)
        #     text_width, text_height = draw.textsize(text, font=image_font)
            
        #     # Check if the font can render the text without errors
        #     if text_width > 0 and text_height > 0:
        #         return image_font, font_size  # Return the valid font
        # except Exception:
        #     pass  # If the font cannot render the text, try another font

def generate(
    text: str,
    fonts: str,
    gray_scale: bool,
    min_font_size: int,
    max_font_size: int,
    orientation: int,
    random_spacing: bool,
    max_random_spacing: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    if orientation == 0:
        return _generate_horizontal_text(
            text,
            fonts,
            gray_scale,
            min_font_size,
            max_font_size,
            random_spacing,
            max_random_spacing,
            space_width,
            character_spacing,
            fit,
            word_split,
            stroke_width,
            stroke_fill,
        )
    elif orientation == 1:
        return _generate_vertical_text(
            text,
            fonts,
            gray_scale,
            min_font_size,
            max_font_size,
            random_spacing,
            max_random_spacing,
            space_width,
            character_spacing,
            fit,
            stroke_width,
            stroke_fill,
        )
    else:
        raise ValueError("Unknown orientation " + str(orientation))


def _compute_character_width(image_font: ImageFont, character: str) -> int:
    if len(character) == 1 and (
        "{0:#x}".format(ord(character))
        in TH_TONE_MARKS + TH_UNDER_VOWELS + TH_UNDER_VOWELS + TH_UPPER_VOWELS
    ):
        return 0
    # Casting as int to preserve the old behavior
    return round(image_font.getlength(character))


def _generate_horizontal_text(
    text: str,
    fonts: str,
    gray_scale: bool,
    min_font_size: int,
    max_font_size: int,
    random_spacing: bool,
    max_random_spacing: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    image_font, font_size = _get_valid_font_from_directory(fonts, text, min_font_size, max_font_size)

    space_width = int(get_text_width(image_font, " ") * space_width)

    if word_split:
        splitted_text = []
        for w in text.split(" "):
            splitted_text.append(w)
            splitted_text.append(" ")
        splitted_text.pop()
    else:
        splitted_text = text

    piece_widths = [
        _compute_character_width(image_font, p) + 
        (rnd.randint(0, max_random_spacing) if random_spacing and p != " " else 0)
        if p != " " else space_width
        for p in splitted_text
    ]
    text_width = sum(piece_widths)
    if not word_split:
        text_width += character_spacing * (len(text) - 1)

    text_height = max([get_text_height(image_font, p) for p in splitted_text])

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGB", (text_width, text_height), (0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask, mode="RGB")
    txt_mask_draw.fontmode = "1"

    # colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
    # c1, c2 = colors[0], colors[-1]


    # fill = (
    #     rnd.randint(min(c1[0], c2[0]), max(c1[0], c2[0])),
    #     rnd.randint(min(c1[1], c2[1]), max(c1[1], c2[1])),
    #     rnd.randint(min(c1[2], c2[2]), max(c1[2], c2[2])),
    # )
    # stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
    #     stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]

    #     stroke_fill = (
    #         rnd.randint(min(stroke_c1[0], stroke_c2[0]), max(stroke_c1[0], stroke_c2[0])),
    #         rnd.randint(min(stroke_c1[1], stroke_c2[1]), max(stroke_c1[1], stroke_c2[1])),
    #         rnd.randint(min(stroke_c1[2], stroke_c2[2]), max(stroke_c1[2], stroke_c2[2])),
    #     )

    if gray_scale:
        grayscale_color = rnd.choice(GRAYSCALE_COLORS)
        fill = getrgb(grayscale_color)
    else:
        text_color = "#000000,#FFFFFF"
        colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
        c1, c2 = colors[0], colors[-1]


        fill = (
            rnd.randint(min(c1[0], c2[0]), max(c1[0], c2[0])),
            rnd.randint(min(c1[1], c2[1]), max(c1[1], c2[1])),
            rnd.randint(min(c1[2], c2[2]), max(c1[2], c2[2])),
        )
    if gray_scale:
        grayscale_color = rnd.choice(GRAYSCALE_COLORS)
        stroke_width = rnd.randint(1, 2)
        stroke_fill = getrgb(grayscale_color)
    else:
        stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
        stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]

        stroke_fill = (
            rnd.randint(min(stroke_c1[0], stroke_c2[0]), max(stroke_c1[0], stroke_c2[0])),
            rnd.randint(min(stroke_c1[1], stroke_c2[1]), max(stroke_c1[1], stroke_c2[1])),
            rnd.randint(min(stroke_c1[2], stroke_c2[2]), max(stroke_c1[2], stroke_c2[2])),
        )

    for i, p in enumerate(splitted_text):
        txt_img_draw.text(
            (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
            p,
            fill=fill,
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        txt_mask_draw.text(
            (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
            p,
            fill=((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255),
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox()), font_size
    else:
        return txt_img, txt_mask, font_size


def _generate_vertical_text(
    text: str,
    fonts: str,
    gray_scale: bool,
    min_font_size: int,
    max_font_size: int,
    random_spacing: bool,
    max_random_spacing: bool,
    space_width: int,
    character_spacing: int,
    fit: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    image_font, font_size = _get_valid_font_from_directory(fonts, text, min_font_size, max_font_size)

    space_height = int(get_text_height(image_font, " ") * space_width)

    char_heights = [
        get_text_height(image_font, c) + (rnd.randint(0, max_random_spacing) if random_spacing and c != " " else 0)
        if c != " " else space_height
        for c in text
    ]
    text_width = max([get_text_width(image_font, c) for c in text])
    text_height = sum(char_heights) + character_spacing * len(text)

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask)
    txt_mask_draw.fontmode = "1"

    # colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
    # c1, c2 = colors[0], colors[-1]

    # fill = (
    #     rnd.randint(c1[0], c2[0]),
    #     rnd.randint(c1[1], c2[1]),
    #     rnd.randint(c1[2], c2[2]),
    # )
    if gray_scale:
        grayscale_color = rnd.choice(GRAYSCALE_COLORS)
        fill = getrgb(grayscale_color)
    else:
        text_color = "#000000,#FFFFFF"
        colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
        c1, c2 = colors[0], colors[-1]

        fill = (
            rnd.randint(c1[0], c2[0]),
            rnd.randint(c1[1], c2[1]),
            rnd.randint(c1[2], c2[2]),
        )


    # stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
    # stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]

    # stroke_fill = (
    #     rnd.randint(stroke_c1[0], stroke_c2[0]),
    #     rnd.randint(stroke_c1[1], stroke_c2[1]),
    #     rnd.randint(stroke_c1[2], stroke_c2[2]),
    # )
    if gray_scale:
        grayscale_color = rnd.choice(GRAYSCALE_COLORS)
        stroke_width = rnd.randint(1, 3)
        stroke_fill = getrgb(grayscale_color)
    else:
        stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
        stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]

        stroke_fill = (
            rnd.randint(min(stroke_c1[0], stroke_c2[0]), max(stroke_c1[0], stroke_c2[0])),
            rnd.randint(min(stroke_c1[1], stroke_c2[1]), max(stroke_c1[1], stroke_c2[1])),
            rnd.randint(min(stroke_c1[2], stroke_c2[2]), max(stroke_c1[2], stroke_c2[2])),
        )

    for i, c in enumerate(text):
        txt_img_draw.text(
            (0, sum(char_heights[0:i]) + i * character_spacing),
            c,
            fill=fill,
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        txt_mask_draw.text(
            (0, sum(char_heights[0:i]) + i * character_spacing),
            c,
            fill=((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255),
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox()), font_size
    else:
        return txt_img, txt_mask, font_size
