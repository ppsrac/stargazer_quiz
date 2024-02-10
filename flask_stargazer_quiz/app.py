from flask import Flask, request, render_template
import time
from utils.load_utils.load_star_data import load_star_data, trans_loc_data
from utils.time_utils.get_sidereal_time import get_sidereal_time
from utils.draw_utils.generate_star_image import generate_star_image


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


@app.route('/draw', methods=['GET'])
def default_star_map():
    if request.method == 'GET':
        img_path, html_img_path = 'static/test.png', '../static/test.png'

        # generate star image
        generate_star_image(img_path, None)

        return render_template('draw_image.html', path=html_img_path)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
