from flask import Blueprint, jsonify,request
import json
import os

cve_bp = Blueprint("cve", __name__)

@cve_bp.route("/api/cves", methods=["GET"])
def get_cves():

    data_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "sample_cves.json"
    )

    with open(data_path, "r") as file:
        cves = json.load(file)

    severity = request.args.get("severity")

    if severity:
        cves = [
            cve for cve in cves
            if cve["severity"].lower() == severity.lower()
        ]

    return jsonify(cves)