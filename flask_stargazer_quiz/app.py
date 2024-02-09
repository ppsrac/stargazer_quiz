from flask import Flask
import time
from utils.load_utils.load_star_data import load_star_data, trans_loc_data
from utils.time_utils.get_sidereal_time import get_sidereal_time

# data file path
data_path = 'data/hyg_v37.csv'

star_loc_data = None
star_info_data = None


# Init method.
# When the Flask app is first executed, initialize the internal data structures.

class StarGazerApp(Flask):
    def __init__(self, *args, **kwargs):
        global star_loc_data, star_info_data
        super().__init__(*args, **kwargs)
        loc_data, star_info_data = load_star_data(data_path)
        star_loc_data = trans_loc_data(loc_data)


app = StarGazerApp(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
