from flask import Flask, jsonify, request
import uuid
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Satellite Service",
        "status": "running"
    })


@app.route("/satellites", methods=["GET"])
def get_satellites():
    satellites = [
        {
            "satellite_id": "SAT-001",
            "name": "EarthWatch-1",
            "status": "active"
        },
        {
            "satellite_id": "SAT-002",
            "name": "EarthWatch-2",
            "status": "active"
        },
        {
            "satellite_id": "SAT-003",
            "name": "EarthWatch-3",
            "status": "maintenance"
        }
    ]

    return jsonify(satellites)


@app.route("/request-image", methods=["POST"])
def request_image():
    data = request.get_json()

    satellite_id = data.get("satellite_id", "SAT-001")
    location = data.get("location", "Unknown")

    image_id = "IMG-" + str(uuid.uuid4())[:8]

    response = {
        "image_id": image_id,
        "satellite_id": satellite_id,
        "location": location,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "requested"
    }

    return jsonify(response), 201


@app.route("/monitor", methods=["POST"])
def monitor():
    data = request.get_json()

    satellite_id = data.get("satellite_id", "SAT-001")
    location = data.get("location", "Unknown")

    # Call Image Service through Docker network
    image_response = requests.post(
        "http://image-service:5001/images",
        json={
            "satellite_id": satellite_id,
            "location": location
        }
    )

    image_result = image_response.json()

    return jsonify({
        "satellite_id": satellite_id,
        "location": location,
        "image_processing": image_result
    }), image_response.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
