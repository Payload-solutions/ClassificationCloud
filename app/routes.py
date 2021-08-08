from app import app

from flask import (
    jsonify,
    request
)
import unittest
from app.model import (
    YogurtData
)
from app.Schema import (
    yogurt_schemas,
    yogurt_schema
)

@app.cli.command()
def tst():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def method_not_allowed(error):
    return jsonify({
        "message": "error by: {} ".format(str(error)),
        "status_code": 405
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "Error by: {}".format(str(error)),
        "status_code": 404
    })


@app.route("/", methods=["GET"])
def index():

    if request.method == "GET":
        data = YogurtData.query.all()
        elements = yogurt_schemas.dump(data)
        
        return jsonify(elements)


@app.route("/one_data/<index>", methods=["GET"])
def get_one_feature(index):
    data = YogurtData.query.get(index)
    return yogurt_schema.jsonify(data)