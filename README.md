# Flask Webpage

### Task 1:
1. Webpage Creation:
• Create a simple webpage with a textbox for entering a city name and a submit button.
• Upon submitting the city name, fetch the weather forecast for the next 3 days from the
www.weatherapi.com service using their API.
• Display the weather forecast for each day in a table format on the webpage.

### 3. Data Storage with any ORM:
• Use an ORM to create a SQLite database table to store the weather forecast data.
• The database table should have columns for date, city, max temperature, min temperature, total
precipitation, sunrise hour, and sunset hour and any other columns that are relevant to you.
• If a combination of date and city already exists in the database, the existing data should be replaced with
the new data.

### Requirements:
• Utilize Flask (or other libraries) for creating the webpage and handling form submissions.
• Use requests library for making API requests to www.weatherapi.com.
• Parse the API response to extract relevant weather forecast data.
• Utilize an ORM for database interactions and model creation.
• Implement error handling for API requests, database interactions, and webpage rendering.
• Upload the code on GITHUB.

## Implementation

### Operating System

- Windows 10 Pro (Version 22H2)

## Compiler

- Python 3.11

## IDE used

- Pycharm Community edition

## Packages:

- blinker==1.7.0
- certifi==2024.2.2
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- Flask==3.0.2
- Flask-SQLAlchemy==3.1.1
- greenlet==3.0.3
- idna==3.6
- itsdangerous==2.1.2
- Jinja2==3.1.3
- MarkupSafe==2.1.5
- requests==2.31.0
- SQLAlchemy==2.0.27
- typing_extensions==4.9.0
- urllib3==2.2.1
- Werkzeug==3.0.1

## How to use:

Simply introduce the desired city name in the displayed form and press the submit button, the page will display meteorological data for the next 3 days for the specified city

## Here's how the script works:

- Setup Logger: If the application is not in debug mode, it sets up a rotating file handler for logging. It logs messages of level INFO or higher to a file named yourapp.log in the logs directory.

- Configuration: It configures the Flask application and initializes the database with SQLAlchemy.

- Main Logic: Defines a route / for handling both GET and POST requests.

  -GET Request: When the user visits the homepage, it renders the index.html template with an empty forecast and city name.

  -POST Request: When the user submits a form (presumably with a city name), it tries to fetch weather forecast data for that city from the WeatherAPI. If successful, it updates the database with the retrieved data or adds a new entry if it doesn't exist already. It then commits the changes to the database. If there's an error during any of these processes, it logs the error and renders an error message in the template.

-Database Handling: It creates the necessary tables in the database if they don't exist already, using db.create_all(). It interacts with the database using SQLAlchemy ORM to check for existing entries and update them or add new entries.

-Run Application: Finally, it runs the Flask application if the script is executed directly.
