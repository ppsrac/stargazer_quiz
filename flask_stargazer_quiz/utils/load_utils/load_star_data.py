import pandas as pd
import numpy as np


def load_star_data(path: str) -> tuple:
    """
    split the
    :param path: location of star csv file.
    :return: tuple of loc_data and info_data
    """
    # load data from csv file
    data = pd.read_csv(path)
    # separate the data into loc_data and others.
    loc_cols = ['id', 'rarad', 'decrad', 'mag']
    info_cols = ['id', 'hip', 'hd', 'hr', 'bf', 'proper', 'spect', 'con']
    loc_data, info_data = data[loc_cols], data[info_cols]
    return loc_data, info_data


def trans_loc_data(loc_data: pd.DataFrame) -> np.array:
    """
    transform loc_data into np array
    ret_array[idx] means the data which star data's id is idx.

    :param loc_data: loc_data from load_star_data
    :return: transformed np array of loc_data
    """
    # convert loc_data into np arrays.
    loc_array = loc_data.values

    # estimate size of the retrieve array.
    num_row = int(np.max(loc_array[:, 0])) + 1

    # generate retrieve array with column ['rarad', 'decrad', 'mag']
    ret_array = np.zeros(shape=(num_row, 3), dtype=np.float64)
    ret_array[:, 2] = 999.0

    # fil the data from loc_array
    for data in loc_array:
        idx = int(data[0])
        ret_data = data[1:]
        ret_array[idx] = ret_data

    # return the retrieve array
    return ret_array
