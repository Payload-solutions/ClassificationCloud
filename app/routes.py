from app import *
import pandas as pd
from flask import (
    jsonify,
    request
)
import unittest
# from app.model import (
#     YogurtData
# )
# from app.Schema import (
#     yogurt_schemas,
#     yogurt_schema
# )
from pprint import pprint


# @app.cli.command()
# def tst():
#     tests = unittest.TestLoader().discover("tests")
#     unittest.TextTestRunner().run(tests)


@app.errorhandler(400)
def not_allowed(error):
    return jsonify({
        "message": "error by {}".format(str(error)),
        "error_type": "not allowed",
        "status_code": 400
    })


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "message": "error by {}".format(str(error)),
        "error_type": "unauthorized",
        "status_code": 401
    })


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "message": "error by {}".format(str(error)),
        "error_type": "forbidden",
        "status_code": 403
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "error by {}".format(str(error)),
        "error_type": "not found",
        "status_code": 404
    })


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "message": "error by {}".format(str(error)),
        "error_type": "method not allowed  ",
        "status_code": 405
    })


@app.errorhandler(406)
def not_acceptable(error):
    return jsonify({
        "message": "error by {}".format(str(error)),
        "error_type": "not acceptable",
        "status_code": 406
    })


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "message": "error by {}".format(str(error)),
        "error_type": "internal server error",
        "status_code": 500
    })




@app.route("/bacteria")
def bacteria():
	"""presenting growth bacteria in 24 hours """
	data = pd.read_csv("data/growth_curve.csv")
	elements = [{"id": index+1, "bacteria": value, "time": time_} 
                for index, (value, time_) in 
                enumerate(zip(
                    data["growth_log"].to_list(), 
                    data["time"].to_list()
                    )
                )
            ]
	return jsonify({
		"content": len(elements),
		"datas": elements,
                "bacteria": data["growth_log"].to_list(),
                "time": data["time"].to_list()
	})



