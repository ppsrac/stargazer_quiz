import numpy as np
from typing import Callable
from PIL import Image, ImageDraw


def generate_star_image(path: str, star_data: np.array, size: tuple[int, int] = (1000, 1000),
                        radius: float = 400.0, plot_func: Callable[[np.array], np.array] = None):
    img = Image.new("RGB", size, color=(255, 255, 255))
    row, col = size

    # draw things in image
    draw_img = ImageDraw.Draw(img)

    # draw ellipse in image
    cen_x, cen_y = row >> 1, col >> 1
    x1, y1, x2, y2 = cen_x - radius, cen_y - radius, cen_x + radius, cen_y + radius
    draw_img.ellipse([x1, y1, x2, y2], outline=(0, 0, 0))

    # If plot_func is none, substitute default plot_func
    w = np.log(10) * 0.15
    if not plot_func:
        def default_plot_func(arr):
            # return 20 * np.ones(shape=(len(star_data)))
            return np.exp(w * (5.0 - arr[:, 4]))
        plot_func = default_plot_func

    # get plot size
    pt_size = plot_func(star_data)

    for i in range(len(star_data)):
        x, y, sz = radius * star_data[i][1] + cen_x, radius * star_data[i][2] + cen_y, pt_size[i]
        draw_img.ellipse([x - sz, y - sz, x + sz, y + sz], fill=(0, 0, 0), outline=(0, 0, 0), width=1)

    img.save(path)
