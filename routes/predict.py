from flask import Blueprint, request, jsonify
import joblib
import numpy as np

predict_blueprint = Blueprint('predict', __name__)

# Load model and encoder
rf_model = joblib.load("predictors/rf_model.pkl")
encoder = joblib.load("predictors/label_encoder.pkl")

@predict_blueprint.route('/predict-risk', methods=['POST'])
def predict_risk():
    try:
        data = request.json
        features = [
            data['attendance'],
            data['assignment_score'],
            data['exam_score']
        ]
        features = np.array(features).reshape(1, -1)
        pred = rf_model.predict(features)[0]
        label = encoder.inverse_transform([pred])[0]

        return jsonify({"risk_level": label}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
