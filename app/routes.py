from app import app
from flask import (
    jsonify
)
import unittest


@app.cli.command()
def tst():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.route("/classification", methods=["GET", "POST"])
def classification():
    return jsonify({
        "message": "the url is working now"
    })
