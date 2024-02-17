import requests
import numpy as np

path = 'https://raw.githubusercontent.com/dieghernan/celestial_data/main/data/constellations.geojson'


def load_constellation() -> tuple[np.array, list]:
    """

    :return:
    """
    response = requests.get(path)
    data = response.json()

    constellations = data['features']

    ret_data = []
    names = []

    for idx in range(len(constellations)):
        constellation = [constellations[idx]['properties']['display_ra'], constellations[idx]['properties']['display_dec']]
        ret_data.append(constellation)
        names.append(constellations[idx]['properties']['id'])
    ret_data = np.array(ret_data)

    ret_data = ret_data * np.pi / 180.0
    return ret_data, names
