from astropy.time import Time
from datetime import datetime
from math import pi
from typing import Optional


#TODO: delete dependency of astropy.time
"""
Can obtain the Julian day from datetime without astropy.time.
See https://stackoverflow.com/questions/33964461/handling-julian-days-in-c11-14.
"""
def get_sidereal_time(longi: float, timeinfo: Optional[tuple] = None) -> float:
    """
    Returns the sidereal time of the desired location at a specific time
    :param longi: the longitude of the desired location
    :param timeinfo: the desired specific time e.g (year, month, day, hour, minute). current time if not specified
    :return: the sidereal time of the desired location at a specific time
    """
    # get datetime from base datetime module or use current time.
    t = datetime.now() if timeinfo is None else datetime(*timeinfo)
    # convert datetime to astropy time object
    t_astropy = Time(t)
    jd = t_astropy.jd

    # now calculate local sidereal time.
    gmst = 18.697374558 + 24.06570982441907 * (jd - 2451545)
    theta = (gmst * 15.0 + longi) % 360.0
    return theta * pi / 180.0
