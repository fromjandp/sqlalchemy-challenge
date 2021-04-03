##################################
# Imports
##################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

##################################
# Database setup
##################################

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

##################################
# Reflet Database into ORM classes
##################################

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

##################################
# Flask setup
##################################

app = Flask(__name__)

##################################
# Flask Routes
##################################

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

@app.route("/api/v1.0/precipitation")

##################################
# Call the main app
##################################

if __name__ == "__main__":
    app.run(debug=True)    
