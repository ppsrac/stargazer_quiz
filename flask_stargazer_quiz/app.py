from flask import Flask

StarData = []

# Init method.
# When the Flask app is first executed, initialize the internal data structures.

class StarGazerApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Custom Hello")


app = StarGazerApp(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
