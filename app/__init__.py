from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://payload:payload123@db:3306/YogurtQuality'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from app import routes
from app import model
from app import Schema