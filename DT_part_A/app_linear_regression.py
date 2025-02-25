from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the Linear Regression model
try:
    linear_model = joblib.load('linear_regression_model.pkl')
    print("Linear Regression model loaded successfully!")
except Exception as e:
    print(f"Error loading Linear Regression model: {e}")
    exit(1)

# Define the default route to show model details
@app.route('/')
def model_info():
    # Hardcoded accuracy (replace with the actual accuracy from training)
    model_accuracy = 44.00  # Replace with the accuracy calculated during training
    return jsonify({
        "model_id": "linear_regression_model",
        "model_type": "Linear Regression",
        "accuracy": f"{model_accuracy}%",  # Display accuracy instead of MSE
        "status": "success"
    })

# Define the prediction route
@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Get input features as query parameters
        sepal_length = float(request.args.get('sepal_length', type=float))
        sepal_width = float(request.args.get('sepal_width', type=float))
        petal_length = float(request.args.get('petal_length', type=float))

        # Check if all required features are provided
        if None in [sepal_length, sepal_width, petal_length]:
            return jsonify({"error": "Please provide all 3 features: sepal_length, sepal_width, petal_length."}), 400

        # Prepare input data
        input_data = np.array([[sepal_length, sepal_width, petal_length]])

        # Make prediction using the Linear Regression model
        prediction = linear_model.predict(input_data)[0]

        # Return the prediction
        return jsonify({
            "model_id": "linear_regression_model",
            "prediction": f"{prediction:.4f}",  # Format prediction to 4 decimal places
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": str(e), "status": "failure"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)  # Use port 5003 for Linear Regression model