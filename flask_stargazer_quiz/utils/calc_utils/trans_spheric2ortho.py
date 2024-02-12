import numpy as np
from math import pi
from typing import Optional
from datetime import datetime
from utils.time_utils.get_sidereal_time import get_sidereal_time


def spheric2ortho(data: np.array, location: tuple[float, float] = (37.5, 127.0),
                  time_info: Optional[tuple] = None) -> np.array:
    """
    Convert given star data which contains (r.a, dec, mag) into star data which contains orthogonal coordinate info.

    :param data: 2D np array storing the information of stars for each row in the order of ra, dec, mag
    :param location: tuple which contains latitude, longitude. (unit: degree)
    :param time_info: the desired specific time e.g (year, month, day, hour, minute). current time if not specified
    :return: star data which converted to np array which row contains (idx, x, y, z, mag) of single star.
    """

    # get necessary infos.
    latitude_deg, longitude_deg = location
    sidereal_time = get_sidereal_time(longi=longitude_deg, timeinfo=time_info)

    # convert unit of location into radian
    latitude_rad, longitude_rad = latitude_deg * pi / 180.0, longitude_deg * pi / 180.0

    # h.a = sidereal - r.a
    hour_angle = sidereal_time - data[:, 0]

    # get sin and cos of latitude
    sin_phi, cos_phi = np.sin(latitude_rad), np.cos(latitude_rad)
    sin_dec, cos_dec = np.sin(data[:, 1]), np.cos(data[:, 1])

    # spherical trigonometry
    sina = sin_dec * sin_phi + cos_dec * cos_phi * np.cos(hour_angle)

    x = (sin_dec - (sin_phi * sina)) / cos_phi
    y = -np.sin(hour_angle) * cos_dec
    z = sina

    theta = np.arccos(z) * 2.0 / np.pi
    r = np.sqrt(x * x + y * y)

    rx, ry = x * theta / r, y * theta / r

    return rx, ry, z


def convert_star(star_data: np.array, location: tuple[float, float] = (37.5, 127.0),
                 time_info: Optional[tuple] = None) -> np.array:
    x, y, z = spheric2ortho(star_data, location, time_info)
    idx = np.arange(star_data.shape[0])

    # TODO: use id as a foreign key to find star info with id.
    ret_array = np.transpose(np.array([idx, x, y, z, star_data[:, 2]]))
    return ret_array


def convert_constline(line_data: np.array, location: tuple[float, float] = (37.5, 127.0),
                      time_info: Optional[tuple] = None) -> np.array:
    x, y, z = spheric2ortho(line_data, location, time_info)

    # TODO: Add constellation infos in ret_array
    ret_array = np.transpose(np.array([x, y, z]))
    return ret_array

