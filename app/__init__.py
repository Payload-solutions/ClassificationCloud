from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root_payload:@localhost/PureMango'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

from app import routes