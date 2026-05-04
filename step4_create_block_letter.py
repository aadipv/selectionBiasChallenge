"""
step4_create_block_letter.py
Generates a block letter "S" (or any letter) as a 2D numpy array
matching the given image dimensions.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_block_letter_s(
    height: int,
    width: int,
    letter: str = "S",
    font_size_ratio: float = 0.9,
) -> np.ndarray:
    """
    Generate a block letter rendered in black on a white background.

    Parameters
    ----------
    height : int
        Height of the output array in pixels.
    width : int
        Width of the output array in pixels.
    letter : str
        The character to render (default "S").
    font_size_ratio : float
        Fraction of the smaller image dimension to use as the font size.

    Returns
    -------
    np.ndarray
        2D array of shape (height, width) with float values in [0, 1].
        0.0 = black (letter area), 1.0 = white (background).
    """
    # Create a white PIL image
    img = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(img)

    # Compute font size from the smaller dimension
    font_size = int(min(height, width) * font_size_ratio)

    # Try to load a bold system font; fall back to the default PIL font
    font = None
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]
    for path in font_paths:
        try:
            font = ImageFont.truetype(path, size=font_size)
            break
        except (IOError, OSError):
            continue

    if font is None:
        # Pillow's built-in bitmap font – very small but always available
        font = ImageFont.load_default()

    # Measure the rendered text so we can centre it
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (width - text_w) // 2 - bbox[0]
    y = (height - text_h) // 2 - bbox[1]

    # Draw the letter in black
    draw.text((x, y), letter, fill=0, font=font)

    # Convert to float array in [0, 1]
    arr = np.array(img, dtype=np.float32) / 255.0
    return arr
