from app import app
from flask import (
    jsonify,
    request
)
import unittest


@app.cli.command()
def tst():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.route("/classification", methods=["GET", "POST"])
def classification():
    if request.method == "POST":
        features_data = request.json["features_data"]
        target_data = request.json["target_data"]
    else:
        pass
