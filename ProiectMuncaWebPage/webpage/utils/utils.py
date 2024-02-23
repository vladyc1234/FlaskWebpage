from flask import Flask, render_template, request
from sqlalchemy.exc import SQLAlchemyError
from requests import RequestException
import requests

def check_internet_connection(app, test_url='https://www.google.com'):
    """
    Checks if the Flask application has an internet connection.

    Parameters:
    - app: The Flask application object for logging purposes.
    - test_url: A URL to test the internet connection. Defaults to 'https://www.google.com'.

    Returns:
    - A boolean indicating if there is an internet connection.
    """
    try:
        response = requests.get(test_url, timeout=2)  # Timeout after 5 seconds
        if response.status_code == 200:
            return True  # Internet connection is available
    except RequestException as e:
        app.logger.error(f"Internet connection check failed: {e}")
    return False  # Internet connection is not available

def get_city_name(app):
    """
    Retrieves the city name from the form submitted via POST request.

    Parameters:
    - app: The Flask application object for logging purposes.

    Returns:
    - A tuple containing the city name and an optional error message. If an error occurs, the city name will be None.
    """
    try:
        city_name = request.form['city']
        return city_name, None
    except ValueError as e:
        app.logger.error(f"Error requesting data from form: {e}")
        error_message = "An error occurred while requesting data from the html form."
        return None, error_message

def get_request_from_api(app, api_url, params):
    """
    Sends a GET request to the specified API URL with the given parameters.

    Parameters:
    - app: The Flask application object for logging purposes.
    - api_url: The URL of the API endpoint.
    - params: A dictionary of parameters to be sent with the request.

    Returns:
    - A tuple containing the response object and an optional error message. If an error occurs, the response object will be None.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX or 5XX
        return response, None
    except RequestException as e:
        app.logger.error(f"Error fetching data from the API: {e}")
        error_message = "An error occurred while fetching data from the API."
        return None, error_message

def add_entry_to_database(app, db_session, new_entry):
    """
    Adds a new entry to the database and commits the transaction.

    Parameters:
    - app: The Flask application object for logging purposes.
    - db_session: The database session through which the operation will be performed.
    - new_entry: The new entry object to be added to the database.

    Returns:
    - A boolean indicating success (True) or failure (False) of the operation, and an optional error message.
    """
    if new_entry:
        try:
            db_session.add(new_entry)
            db_session.commit()
            return True, None  # Operation successful
        except SQLAlchemyError as e:
            db_session.rollback()
            app.logger.error(f"Failed adding object to database: {e}")
            error_message = "Failed to add object to database."
            return False, error_message
    else:
        app.logger.error(f"New_entry does not exits")
        error_message = "New_entry does not exits"
        return False, error_message

def update_database(app, db_session):
    """
    Commits the update to the database.

    Parameters:
    - app: The Flask application object for logging purposes.
    - db_session: The database session through which the operation will be performed.

    Returns:
    - A boolean indicating success (True) or failure (False) of the operation, and an optional error message.
    """
    try:
        db_session.commit()
        return True, None  # Operation successful
    except SQLAlchemyError as e:
        db_session.rollback()
        app.logger.error(f"Failed committing object to database: {e}")
        error_message = "Failed to commit changes to database"
        return False, error_message
