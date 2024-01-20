import requests
import os
from flask import Flask, request, render_template

app = Flask(__name__) # is the first page always called this?

api_key = os.getenv('API_KEY')
base_url = f'http://api.weatherstack.com/current?access_key={api_key}&query=' # what is the f?

# does this have to be here or can it be after ?
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = ""
    city = ""
    photos = []
    description = ""

    if request.method == 'POST':
        city = request.form['city']
        response = requests.get(base_url + city)
        weather_celsius = response.json()['current']['temperature']
        weather_fahrenheit = celsius_to_fahrenheit(weather_celsius)
        description = response.json()['current']['weather_descriptions'][0]
        weather = f"{weather_fahrenheit}°F"
        photos = get_weather_images(description)
    return render_template("index.html", city=city, weather=weather, photos=photos, description=description)

def get_weather_images(description):
    if description == 'Partly cloudy':
        return ["<span style='font-size:100px;'>&#9925;</span>"]
    elif description == 'Clear' or 'Sunny' in description:
        return ["<span style='font-size:100px;'>&#127774;</span>"]
    elif 'rain' in description.lower():
        return ["<span style='font-size:100px;'>&#9748;</span>"]
    elif 'mist' in description.lower() or 'Fog' in description.lower() or 'haze' in description.lower():
        return ["<span style='font-size:100px;'>&#127787;</span>"]
    elif 'overcast' in description.lower():
        return ["<span style='font-size:100px;'>&#127787;</span>"]
    elif 'snow' in description.lower():
        return ["<span style='font-size:100px;'>&#9924;</span>"]
    elif 'cloudy' in description.lower():
        return ["<span style='font-size:100px;'>&#9925;</span>"]
    else:
        return ["image_default.jpg"]



if __name__ == '__main__':
    app.run(debug=True)
