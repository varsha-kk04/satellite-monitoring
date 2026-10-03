from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Analysis Service",
        "status": "running"
    })


@app.route("/analyze", methods=["POST"])
def analyze_image():
    data = request.get_json()

    image_id = data.get("image_id", "IMG-UNKNOWN")
    change_percentage = float(data.get("change_percentage", 0))

    # Analyze image
    if change_percentage >= 30:
        analysis_result = "significant_change"
        risk_level = "high"
        alert_status = "critical_alert_generated"
        message = "Significant change detected."

    elif change_percentage >= 15:
        analysis_result = "moderate_change"
        risk_level = "medium"
        alert_status = "warning_generated"
        message = "Moderate change detected."

    else:
        analysis_result = "minor_change"
        risk_level = "low"
        alert_status = "no_alert"
        message = "Minor change detected."

    # Alert functionality is handled inside Analysis Service
    alert_result = {
        "alert_status": alert_status,
        "image_id": image_id,
        "risk_level": risk_level,
        "analysis_result": analysis_result,
        "message": message,
        "created_at": datetime.utcnow().isoformat()
    }

    result = {
        "image_id": image_id,
        "change_percentage": change_percentage,
        "analysis_result": analysis_result,
        "risk_level": risk_level,
        "analyzed_at": datetime.utcnow().isoformat(),
        "alert": alert_result
    }

    return jsonify(result), 200


@app.route("/health")
def health():
    return jsonify({
        "service": "Analysis Service",
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
