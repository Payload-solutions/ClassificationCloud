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




# Normal methods

# @app.route("/", methods=["GET"])
# def index():

#     data = YogurtData.query.all()
#     elements = yogurt_schemas.dump(data)

#     return jsonify(elements)


# @app.route("/one_data/<index>", methods=["GET"])
# def get_one_feature(index):
#     data = YogurtData.query.get(index)
#     return yogurt_schema.jsonify(data)


# @app.route("/new_feature", methods=["POST"])
# def new_feature():
#     try:
        
#         # data = {
#         #     "streptococcus_initial_strain_cfu_ml":3.683,
#         #     "lactobacillus_initial_strain_cfu_ml":4.6979999999999995,
#         #     "ideal_temperature_c":41.681999999999995,
#         #     "minimum_milk_proteins":2.67,
#         #     "titratable_acidity":1.001,
#         #     "pH_milk_sour_":4.577,
#         #     "fat_milk_over_100mg_":3.8438,
#         #     "quality_product":"Regular yogurt",
#         #     "lactobacillus_final_cfu_ml":9.56,
#         #     "streptococcus_final_cfu_ml":7.86,
#         #     "quality_product_":2,
#         # }
#         print(request.json)
#         data_insertion = request.json
#         new_insertion = YogurtData(
#                 float(data_insertion["streptococcus_initial_strain_cfu_ml"]),
#                 float(data_insertion["lactobacillus_initial_strain_cfu_ml"]),
#                 float(data_insertion["ideal_temperature_c"]),
#                 float(data_insertion["minimum_milk_proteins"]),
#                 float(data_insertion["titratable_acidity"]),
#                 float(data_insertion["pH_milk_sour_"]),
#                 float(data_insertion["fat_milk_over_100mg_"]),
#                 (data_insertion["quality_product"]),
#                 float(data_insertion["lactobacillus_final_cfu_ml"]),
#                 float(data_insertion["streptococcus_final_cfu_ml"]),
#                 int(data_insertion["quality_product_"])
#         )
#         db.session.add(new_insertion)
#         db.session.commit()
#         return jsonify({
#             "message": "saved into database successfully"
#         })
#     except Exception as e:
#         print(str(e))
#         return jsonify({
#             "message": "Error by: {}".format(str(e))
#         })

# @app.route("/new_features", methods=["POST"])
# def new_features():
#     try:
#         pass
#     except Exception as e:
#         return jsonify({
#             "message": "Error by: {}".format(str(e))
#         })



@app.route("/bacteria")
def bacteria():
	"""presenting growth bacteria in 24 hours """
	data = pd.read_csv("data/growth_curve.csv")
	# elements = [{"bacteria": value, "time": data} for value, data in zip(dataset.growth_log.to_list(), dataset.time.to_list())]
	elements = [{"id": index+1, "bacteria": value, "time": time_} for index, (value, time_) in enumerate(zip(data["growth_log"].to_list(), data["time"].to_list()))]
	return jsonify({
		"content": len(elements),
		"datas": elements,
                "bacteria": data["growth_log"].to_list(),
                "time": data["time"].to_list()
	})



