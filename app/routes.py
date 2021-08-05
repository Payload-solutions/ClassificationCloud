from app import app
from flask import (
    jsonify
)


@app.route("/classification", methods=["GET", "POST"])
def classification():
    return jsonify({
        "message": "the url is working now"
    })