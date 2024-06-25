# Import the dependencies.

import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import desc
from datetime import datetime, timedelta


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
station = base.classes.station
measurement = base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
app= Flask(__name__)
#################################################
   
#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """Homepage:
    List of all available routes:"""
    return

@app.route("/api/v1.0/precipitation")
@app.route("/api/v1.0/stations")
@app.route("/api/v1.0/tobs")
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")