from flask import Flask, request, render_template
from utils.load_utils.load_star_data import load_star_data, trans_loc_data
from utils.time_utils.get_sidereal_time import get_sidereal_time
from utils.draw_utils.generate_star_image import generate_star_image



# Init method.
# When the Flask app is first executed, initialize the internal data structures.

class StarGazerApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Flask initialization finished")


app = StarGazerApp(__name__)


@app.route('/draw', methods=['GET'])
def draw_blank():
    if request.method == 'GET':
        img_path = 'static/test.png'
        print(img_path)
        generate_star_image(img_path, None)
        print("Image generated")
        path = '../' + img_path
        print(path)
        return render_template('draw_image.html', path=path)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
