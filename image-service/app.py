from flask import Flask, jsonify, request
import uuid
from datetime import datetime
import random
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Image Service",
        "status": "running"
    })


@app.route("/images", methods=["POST"])
def create_image():
    data = request.get_json()

    satellite_id = data.get("satellite_id", "SAT-001")
    location = data.get("location", "Unknown")

    image_id = "IMG-" + str(uuid.uuid4())[:8]

    change_percentage = round(random.uniform(5, 40), 2)

    image = {
        "image_id": image_id,
        "satellite_id": satellite_id,
        "location": location,
        "timestamp": datetime.utcnow().isoformat(),
        "change_percentage": change_percentage,
        "status": "processed"
    }

    # Call Analysis Service through Docker network
    analysis_response = requests.post(
        "http://analysis-service:5002/analyze",
        json={
            "image_id": image_id,
            "change_percentage": change_percentage
        }
    )

    analysis_result = analysis_response.json()

    image["analysis"] = analysis_result

    return jsonify(image), 201


@app.route("/health")
def health():
    return jsonify({
        "service": "Image Service",
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
