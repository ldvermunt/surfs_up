#Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Set up the database engine:
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect the "sqlite:///hawaii.sqlite" database into classes
Base = automap_base()
#Reflect the database
Base.prepare(engine, reflect=True)

#create variables for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session link from Python to our database
session = Session(engine)

#Define the flask app
app = Flask(__name__)

#Define the welcome route:
@app.route("/")

#Create a function for the 'welcome' route.  Like the homepage.

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#Create routes from the main root. ('precipitation route')
@app.route('/api/v1.0/precipitation')
#Create the precipitation function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


#Create the 'stations' route
@app.route('/api/v1.0/stations')
#Define a 'stations function'
def stations():
    results = session.query(Station.station).all()
#unravel the results into a one-dimensional array and convert that array into a list.
    stations = list(np.ravel(results))
    return jsonify(stations = stations)

#Create the temperature (tobs) route
@app.route('/api/v1.0/tobs')
#Define a tobs function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify (temps = temps)

#Create the statistics route.  temps start - end
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#Create a 'stats' function to put our code in and Add a start and end parameter to our stats funciton
def stats(start=None, end=None):
#Create query to get min max and avg
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

