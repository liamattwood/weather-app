from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        unit = request.form['unit']
        api_key = "API KEY GOES HERE"

        # Make a GET request to the OpenWeatherMap API using metric units (Celsius)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the weather information
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']

            return render_template('index.html', city=city, weather=weather, temperature=temperature, unit=unit)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
