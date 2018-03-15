from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<city>/analysis')
def print_city(city):
    return "Hello {}!".format(city)


if __name__ == '__main__':
    app.run()
