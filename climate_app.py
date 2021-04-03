# #######################################
# Imports
# #######################################

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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

#  print(Base.classes.keys())

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
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<end><br/>"
)

#
# preciptation api
#

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).all()

    session.close()

# Create a dictionary from the rows of data, and append to a list all_precipitation
    all_precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"]  = precipitation
        all_precipitation.append(precipitation_dict)
        
    
    return jsonify(all_precipitation)
#
# stations api
#

@app.route("/api/v1.0/stations")
def stations():
    return (
        f"stations path"
    )

#
# tobs api
#

@app.route("/api/v1.0/tobs")
def tobs():
    return (
        f"tobs path"
    )

# #######################################
# Call the main Development Flask Server
# #######################################

if __name__ == "__main__":
        app.run(debug=True)  

