from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import os

db = SQLAlchemy()

class WeatherForecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    max_temp = db.Column(db.Float, nullable=False)
    min_temp = db.Column(db.Float, nullable=False)
    total_precip = db.Column(db.Float, nullable=False)
    sunrise = db.Column(db.String(50), nullable=False)
    sunset = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<WeatherForecast {self.city}, Date: {self.date}>'

