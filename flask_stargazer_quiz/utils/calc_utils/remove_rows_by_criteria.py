import numpy as np
from math import pi


def remove_rows_by_criteria(star_data: np.array, alti_deg: float = 10.0, max_mag: float = 5.0):
    """
    filter star data with altiude limit and magnitude limit.
    :param star_data: np array of given star data. Each row contains (id, x, y, z, mag) of single star.
    :param alti_deg: lower limit of star altitude. (unit: degree)
    :param max_mag: upper limit of star magnitude. (unit: mag)
    :return: np array of star data which satisfies above condition.
    """
    alti = np.sin(alti_deg * pi / 180.0)
    mask = (star_data[:, 3] > alti) & (star_data[:, 4] < max_mag)
    filtered_data = star_data[mask]
    return filtered_data
