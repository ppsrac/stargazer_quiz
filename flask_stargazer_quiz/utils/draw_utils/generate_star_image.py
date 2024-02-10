import numpy as np
from typing import Callable
from PIL import Image, ImageDraw


def generate_star_image(path: str, star_data: np.array, size: tuple[int, int] = (1000, 1000),
                        radius: float = 400.0, plot_func: Callable[[float], float] = None):
    img = Image.new("RGB", size, color=(255, 255, 255))
    row, col = size

    # draw things in image
    draw_img = ImageDraw.Draw(img)

    # draw ellipse in image
    cen_x, cen_y = row >> 1, col >> 1
    x1, y1, x2, y2 = cen_x - radius, cen_y - radius, cen_x + radius, cen_y + radius
    draw_img.ellipse([x1, y1, x2, y2], outline=(0, 0, 0))

    img.save(path)
