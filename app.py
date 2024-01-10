import requests
from flask import Flask, request, render_template

app = Flask(__name__)

api_key = '1e832c3fb8f1f922610f136fab1f1056'
base_url = f'http://api.weatherstack.com/current?access_key={api_key}&query='

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = ""
    city = ""
    if request.method == 'POST':
        city = request.form['city']
        response = requests.get(base_url + city)
        weather_celsius = response.json()['current']['temperature']
        weather_fahrenheit = celsius_to_fahrenheit(weather_celsius)
        weather = f"{weather_celsius}°C / {weather_fahrenheit}°F"
    return render_template("index.html", city=city, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
