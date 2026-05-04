"""
step5_create_masked.py
Applies a block-letter mask to a stippled image to simulate selection bias.
"""

import numpy as np


def create_masked_stipple(
    stipple_img: np.ndarray,
    mask_img: np.ndarray,
    threshold: float = 0.5,
) -> np.ndarray:
    """
    Apply a binary mask to a stippled image.

    Where the mask pixel is dark (below threshold) the corresponding
    stipple pixel is erased to white (1.0), simulating the systematic
    removal of data points caused by selection bias.
    Where the mask pixel is light (at or above threshold) the stipple
    pixel is kept unchanged.

    Parameters
    ----------
    stipple_img : np.ndarray
        2D float array (H x W) with values in [0, 1].
        0.0 = stipple dot (data point), 1.0 = background.
    mask_img : np.ndarray
        2D float array (H x W) with values in [0, 1].
        0.0 = masked / hidden area, 1.0 = visible area.
    threshold : float
        Pixels in mask_img below this value are treated as the mask.

    Returns
    -------
    np.ndarray
        2D float array (H x W) with the same shape as the inputs.
    """
    if stipple_img.shape != mask_img.shape:
        raise ValueError(
            f"Shape mismatch: stipple {stipple_img.shape} vs mask {mask_img.shape}"
        )

    result = stipple_img.copy()

    # Where the mask is dark (letter area) → erase stipples → set to white
    masked_region = mask_img < threshold
    result[masked_region] = 1.0

    return result
