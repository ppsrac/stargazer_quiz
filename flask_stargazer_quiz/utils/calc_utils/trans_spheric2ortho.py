import numpy as np
from math import pi
from typing import Optional
from datetime import datetime
from utils.time_utils.get_sidereal_time import get_sidereal_time


def spheric2ortho(star_data: np.array, location: tuple[float, float],
                  time_info: Optional[tuple] = None) -> np.array:
    """

    :param star_data: 2D np array storing the information of stars for each row in the order of ra, dec, mag
    :param location:
    :param time_info:
    :return:
    """

    # get necessary infos.
    latitude_deg, longitude_deg = location
    sidereal_time = get_sidereal_time(longi=longitude_deg, timeinfo=time_info)

    # convert unit of location into radian
    latitude_rad, longitude_rad = latitude_deg * pi /180.0, longitude_deg * pi /180.0

    # h.a = sidereal - r.a
    hour_angle = sidereal_time - star_data[:, 0]





    pass
