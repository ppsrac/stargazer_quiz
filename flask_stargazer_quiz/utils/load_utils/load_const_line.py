import requests
import numpy as np

path = 'https://raw.githubusercontent.com/dieghernan/celestial_data/main/data/constellations.lines.geojson'


def load_const_line() -> np.array:
    response = requests.get(path)
    data = response.json()

    const_line = data['features']

    ret_data = []

    for idx in range(len(const_line)):
        single_line = const_line[idx]['geometry']['coordinates']
        # print(single_line)
        for i in range(len(single_line)):
            for j in range(len(single_line[i]) - 1):
                ret_data.append(single_line[i][j])
                ret_data.append(single_line[i][j + 1])
    ret_data = np.array(ret_data)

    ret_data = ret_data * np.pi / 180.0
    return ret_data

