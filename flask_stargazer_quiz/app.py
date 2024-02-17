from flask import Flask, request, render_template
import time
from utils.load_utils.load_star_data import load_star_data, trans_loc_data
from utils.load_utils.load_const_line import load_const_line
from utils.load_utils.load_constellations import load_constellation
from utils.time_utils.get_sidereal_time import get_sidereal_time
from utils.calc_utils.trans_spheric2ortho import convert_star, convert_constline, convert_constellation
from utils.calc_utils.remove_rows_by_criteria import remove_stars_by_criteria, remove_constlines_by_criteria, remove_constellations_by_criteria
from utils.draw_utils.generate_star_image import generate_star_image


# data file path
data_path = 'data/hyg_v37.csv'

star_loc_data = None
star_info_data = None
const_line_loc_data = None
constellation_loc_data = None
constellation_name_data = None


# Init method.
# When the Flask app is first executed, initialize the internal data structures.

class StarGazerApp(Flask):
    def __init__(self, *args, **kwargs):
        global star_loc_data, star_info_data, const_line_loc_data, constellation_loc_data, constellation_name_data
        super().__init__(*args, **kwargs)
        loc_data, star_info_data = load_star_data(data_path)
        star_loc_data = trans_loc_data(loc_data)
        const_line_loc_data = load_const_line()
        constellation_loc_data, constellation_name_data = load_constellation()


app = StarGazerApp(__name__)


@app.route('/draw', methods=['GET'])
def default_star_map():
    if request.method == 'GET':
        img_path, html_img_path = 'static/test.png', '../static/test.png' # absolute path does not work.
        """
        See https://stackoverflow.com/questions/5157772/src-absolute-path-problem
        """

        # get the data source from
        ortho_star_data, ortho_const_line, ortho_constellation = (convert_star(star_loc_data),
                                                                  convert_constline(const_line_loc_data),
                                                                  convert_constellation(constellation_loc_data))
        filtered_star_data, filtered_const_line, filtered_constellation = (remove_stars_by_criteria(ortho_star_data),
                                                                           remove_constlines_by_criteria(ortho_const_line),
                                                                           remove_constellations_by_criteria(ortho_constellation, constellation_name_data))

        # generate star image
        generate_star_image(img_path, filtered_star_data, filtered_const_line, filtered_constellation)

        return render_template('draw_image.html', path=html_img_path)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
