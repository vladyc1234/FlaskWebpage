from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request
import logging
from databaseModel.model import db, WeatherForecast
from utils.utils import get_city_name, get_request_from_api, add_entry_to_database, update_database, \
    check_internet_connection
import os

app = Flask(__name__)

# Setup logger
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/yourapp.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('YourApp startup')


API_KEY = 'c9e7fb3a081a40cc9a9155106242102'
WEATHER_API_URL = 'http://api.weatherapi.com/v1/forecast.json'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Global variables
global params

# Main logic
@app.route('/', methods=['GET', 'POST'])
def home():

    # Create database
    db.create_all()

    forecast = None
    city_name = ''

    # Check internet connection first
    if not check_internet_connection(app):
        error_message = "No internet connection. Please check your connection and try again."
        return render_template('error_template.html', error=error_message)

    # Check if User has entered something in the form
    if request.method == 'POST':

        city_name, error_message = get_city_name(app)
        if error_message:
            return render_template('index.html', error=error_message)

        app.logger.info('Requested data from html form successfully')

        params = {
            'key': API_KEY,
            'q': city_name,
            'days': 3,# numbers of days to check forecast
        }

        response, error_message = get_request_from_api(app, WEATHER_API_URL, params)
        if error_message:
            return render_template('index.html', error=error_message, popup=True)

        app.logger.info('Requested data from html form successfully')

        if response.status_code == 200:
            app.logger.info('Fetched data from API successfully')
            forecast_data = response.json()['forecast']['forecastday']

            # Check API data - If it already exists in the DB update it - If it doesn't exist add it
            for day in forecast_data:
                existing_entry = WeatherForecast.query.filter_by(date=day['date'], city=city_name).first()
                if existing_entry:
                    existing_entry.max_temp = day['day']['maxtemp_c']
                    existing_entry.min_temp = day['day']['mintemp_c']
                    existing_entry.total_precip = day['day']['totalprecip_mm']
                    existing_entry.sunrise = day['astro']['sunrise']
                    existing_entry.sunset = day['astro']['sunset']
                else:
                    new_entry = WeatherForecast(
                        date=day['date'],
                        city=city_name,
                        max_temp=day['day']['maxtemp_c'],
                        min_temp=day['day']['mintemp_c'],
                        total_precip=day['day']['totalprecip_mm'],
                        sunrise=day['astro']['sunrise'],
                        sunset=day['astro']['sunset']
                    )

                    success, error_message = add_entry_to_database(app, db.session, new_entry)
                    if not success:
                        return render_template('some_template.html', error=error_message)

            success, error_message = update_database(app, db.session)
            if not success:
                return render_template('some_template.html', error=error_message)

            app.logger.info('Made changes to database successfully')
            forecast = forecast_data

    return render_template('index.html', forecast=forecast, city_name=city_name)

if __name__ == '__main__':
    app.run(debug=True)
