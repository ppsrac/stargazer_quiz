import numpy as np
from typing import Callable
from PIL import Image, ImageDraw


def generate_star_image(star_data: np.array, size: tuple[int, int] = (800, 800),
                        radius: float = 600.0, plot_func: Callable[[float], float] = None):
    img = Image.new("RGB", size, color=(0, 0, 0))
    return img
