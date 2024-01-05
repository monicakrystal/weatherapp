import requests
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = ""
    city = ""
    if request.method == 'POST':
        city = request.form['city']
    return render_template("index.html", city=city)


if __name__ == '__main__':
    app.run(debug=True)
