from flask import Flask, config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from config import Config
import pandas as pd



# def get_environment_config():
#     if Config.ENV == "TESTING":
#         return "config.TestingConfig"
    
#     elif Config.ENV == "DEVELOPMENT":
#         return "config.DevelopmentConfig"


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root_payload:@localhost/YogurtQuality'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config.from_object(get_environment_config())
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
CORS(app)

# @app.before_first_request
# def initialize_database():
#     db.create_all()
#     dataframe = pd.read_csv("app/classification_data.csv")
#     dataframe.to_sql(name = "features_data", if_exists="replace", con=db.engine, index=True)


from app import routes
# from app import model
# from app import Schema


