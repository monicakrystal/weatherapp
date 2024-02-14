import requests
import os
from flask import Flask, request, render_template

app = Flask(__name__)

api_key = os.getenv('API_KEY')
base_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q='  # SIGNIFICANCE OF THE F? need it everytime?


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = ""
    city = ""
    description = ""
    photos = []

    if request.method == 'POST':
        city = request.form['city']
        response = requests.get(base_url + city)
        weather = response.json()['current']['temp_f']
        description = response.json()['current']['condition']['text']
        photos = get_weather_images(description)
    return render_template("index.html", city=city, weather=weather, description=description, photos=photos)


def get_weather_images(description):
    description = description.lower()
    description = description.replace(' ', '_')

    weather_images = {
        'partly_cloudy': 'cloud',
        'clear': "☀️",
        'sunny': "☀️",
        'rain': "🌧️",
        'overcast': "6"
    }

    if 'rain' in description:
        return weather_images['rain']
    else:
        return weather_images.get(description, "Unknown weather")


if __name__ == '__main__':
    app.run(debug=True)
