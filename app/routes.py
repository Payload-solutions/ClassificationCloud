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


@app.route("/", methods=["GET", "POST"])
def classification():

    if request.method == "GET":
        return jsonify({
            "message": "testing"
        })
    else:
        pass

