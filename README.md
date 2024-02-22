# Flask Webpage

## Task 1:

### 1. Webpage Creation:
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

- Database Handling: It creates the necessary tables in the database if they don't exist already, using db.create_all(). It interacts with the database using SQLAlchemy ORM to check for existing entries and update them or add new entries.

- Main Logic: Defines a route / for handling both GET and POST requests.

  - GET Request: When the user visits the homepage, it renders the index.html template with an empty forecast and city name.

  - POST Request: When the user submits a form (presumably with a city name), it tries to fetch weather forecast data for that city from the WeatherAPI. If successful, it updates the database with the retrieved data or adds a new entry if it doesn't exist already. It then commits the changes to the database. If there's an error during any of these processes, it logs the error and renders an error message in the template.

## Task 2

### SQL query:

Using SQL queries and the following tables: Persons and Votes, generate these reports:
1. Create a report with the votes/qualities received for each person in each location.
2. Create a report with the votes on each country. For countries without votes, return 0.
The SQL queries for creating and inserting data in tables can be found below:

1. Persons
   
CREATE TABLE persons (
ID VARCHAR(20) PRIMARY KEY,
Status VARCHAR(10),
First_Name VARCHAR(50),
Last_Name VARCHAR(50),
Email_Address VARCHAR(100),
Locatie VARCHAR(50)
);

3. Votes
CREATE TABLE Votes (
ID INT PRIMARY KEY,
voting_date DATETIME,
chosen_person VARCHAR(20),
voter INT,
message VARCHAR(100),
valid BIT,
quality VARCHAR(20)
);

With the following insert queries:

Insert to persons:

INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('00108901', 'Active', 'Person', 'One', 'person.one@gfk.com', 'Germany');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('00108941', 'Active', 'Person', 'Two', 'person.two@gfk.com', 'France');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('00199990', 'Inactive', 'Person', 'Three', 'person.three@gfk.com', 'Brazil');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('01100003', 'Active', 'Person', 'Four', 'person.four@gfk.com', 'Hong Kong');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('03400110', 'Active', 'Person', 'Five', 'person.five@gfk.com', 'Germany');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('03400360', 'Active', 'Person', 'Six', 'person.six@gfk.com', 'France');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('03402059', 'Inactive', 'Person', 'Seven', 'person.seven@gfk.com', 'Brazil');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('03400565', 'Active', 'Person', 'Eight', 'person.eight@gfk.com', 'Hong Kong');
INSERT INTO persons (ID, Status, First_Name, Last_Name, Email_Address, Locatie)
VALUES ('03400436', 'Active', 'Person', 'Nine', 'person.nine@gfk.com', 'Hong Kong');

Insert to Votes:

INSERT INTO Votes (ID, Voting_date, chosen_person, voter, message, valid, quality)
VALUES (253, '2022-10-29 11:54:15', '03400110', 1, 'Vote 1', 1, 'entrepreneur');
INSERT INTO Votes (ID, Voting_date, chosen_person, voter, message, valid, quality)
VALUES (254, '2022-10-29 11:55:22', '03400360', 1, 'Vote 2', 0, 'entrepreneur');
INSERT INTO Votes (ID, Voting_date, chosen_person, voter, message, valid, quality)
VALUES (255, '2022-10-29 11:56:53', '03402059', 1, 'Vote 3', 1, 'partner');
INSERT INTO Votes (ID, Voting_date, chosen_person, voter, message, valid, quality)
VALUES (256, '2022-10-29 11:58:23', '03400565', 1, 'Vote 4', 1, 'developer');
INSERT INTO Votes (ID, Voting_date, chosen_person, voter, message, valid, quality)
VALUES (257, '2022-10-29 12:13:00', '03400436', 1, 'Vote 5', 1, 'developer');


