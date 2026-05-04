"""
create_meme.py
Assembles four image panels into a professional statistics meme PNG.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white",
) -> None:
    """
    Assemble four panels into a side-by-side statistics meme and save as PNG.

    Parameters
    ----------
    original_img : np.ndarray
        2D grayscale array – "Reality" panel.
    stipple_img : np.ndarray
        2D grayscale array – "Your Model" panel.
    block_letter_img : np.ndarray
        2D grayscale array – "Selection Bias" panel.
    masked_stipple_img : np.ndarray
        2D grayscale array – "Estimate" panel.
    output_path : str
        File path for the saved PNG (e.g. "my_statistics_meme.png").
    dpi : int
        Resolution of the saved figure (150–300 recommended).
    background_color : str
        Matplotlib-compatible colour string for the figure background.
    """
    panels = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    labels = ["Reality", "Your Model", "Selection Bias", "Estimate\n('seems legit')"]

    fig = plt.figure(figsize=(18, 6), facecolor=background_color)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.82, bottom=0.05, wspace=0.06)

    gs = GridSpec(1, 4, figure=fig)

    for idx, (panel, label) in enumerate(zip(panels, labels)):
        ax = fig.add_subplot(gs[0, idx])
        ax.imshow(panel, cmap="gray", vmin=0, vmax=1)
        ax.axis("off")

        # Add a thin border rectangle around each panel
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(1.5)
            spine.set_edgecolor("#555555")

        # Panel label above each image
        ax.set_title(
            label,
            fontsize=15,
            fontweight="bold",
            pad=8,
            color="#222222",
        )

    # Main title
    fig.suptitle(
        "Selection Bias & Missing Data",
        fontsize=20,
        fontweight="bold",
        y=0.97,
        color="#111111",
    )

    plt.savefig(output_path, dpi=dpi, bbox_inches="tight", facecolor=background_color)
    plt.close(fig)
    print(f"Meme saved to: {output_path}")
