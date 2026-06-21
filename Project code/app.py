from flask import Flask, render_template, request, jsonify
import pandas as pd
from joblib import load

app = Flask(__name__)
# Load the model trained with 4 features
model = load("random_forest_model_4_features.joblib")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check if the request is JSON (API call) or standard Form
        is_json = request.is_json
        
        feature_names = [
            'Flow Duration',
            'Total Fwd Packets',
            'Total Backward Packets',
            'Total Length of Fwd Packets'
        ]
        
        html_input_names = [
            "flow_duration",
            "total_fwd_packets",
            "total_backward_packets",
            "total_length_fwd_packets"
        ]

        feature_values = []
        
        if is_json:
            data = request.get_json() or {}
            for name in html_input_names:
                if name not in data:
                    return jsonify({"error": f"Missing field '{name}' in JSON payload. All 4 features are required."}), 400
                try:
                    feature_values.append(float(data[name]))
                except (ValueError, TypeError):
                    return jsonify({"error": f"Invalid numeric value for field '{name}'."}), 400
        else:
            for name in html_input_names:
                try:
                    feature_values.append(float(request.form[name]))
                except KeyError:
                    return f"Error: Missing form field '{name}'. Please provide all 4 feature inputs.", 400
                except ValueError:
                    return f"Error: Invalid input for '{name}'. Please enter a valid number.", 400

        # Construct a pandas DataFrame to match the trained model's feature names
        # This resolves the scikit-learn UserWarning about missing feature names
        input_df = pd.DataFrame([feature_values], columns=feature_names)
        prediction_raw = model.predict(input_df)[0]
        
        # Clean prediction output (formatting the en-dash encoding)
        prediction_cleaned = str(prediction_raw).replace("\u2013", "-")
        
        if is_json:
            return jsonify({
                "status": "success",
                "prediction": prediction_cleaned,
                "inputs": {html_input_names[i]: feature_values[i] for i in range(len(html_input_names))}
            })
            
        return render_template("index.html", prediction=prediction_cleaned)
        
    except Exception as e:
        if request.is_json:
            return jsonify({"status": "error", "message": str(e)}), 500
        return f"Error during prediction: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)