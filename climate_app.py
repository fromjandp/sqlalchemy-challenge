# #######################################
# Imports
# #######################################

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import numpy as np
import datetime as dt
from flask import Flask, jsonify

# #######################################
# Database setup
# #######################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# #######################################
# Reflet Database into ORM classes
# #######################################

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# print(Base.classes.keys())

# Save references to the class measures
measurement = Base.classes.measurement

# Save references to the class stations
station = Base.classes.station

# ######################################
# Flask setup
# #######################################

app = Flask(__name__)

# #######################################
# Flask Routes
# #######################################

@app.route("/")
def home_page():
    return (
        f"Welcome to the Climate App API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#
# preciptation api
#

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)
    
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= prev_year)
    
    session.close()
    
    # date is the key and the precipitation is the value
    selected_precipitation  = {date: prcp for date, prcp in results}

    # Create a dictionary from the rows of data, and append to a list all_precipitation

    return jsonify(selected_precipitation)

#
# stations api
#

@app.route("/api/v1.0/stations")
def stations():

    session = Session(engine)
    
    all_stations = []
    all_stations = session.query(station.station).all()
 
    session.close()
    
    return jsonify(all_stations)

#
# tobs api
#

@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)
    
    start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date >= start_date).all()

    session.close()

    temperatures = list(np.ravel(results))
   
    return jsonify(temperatures)

# #######################################
# Call the main Development Flask Server
# #######################################

if __name__ == "__main__":
        app.run(debug=True)  

