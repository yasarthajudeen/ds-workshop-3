from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load the Naive Bayes model
try:
    naive_bayes_model = joblib.load('naive_bayes_iris_model.pkl')  # Ensure this file exists in the same directory
    print("Naive Bayes model loaded successfully!")
except Exception as e:
    print(f"Error loading Naive Bayes model: {e}")
    exit(1)

# Define the default route to show model details
@app.route('/')
def model_info():
    # Hardcoded accuracy (replace with your actual accuracy)
    model_accuracy = 94.00  # Replace with the accuracy calculated during training
    return jsonify({
        "model_id": "naive_bayes_model",
        "model_type": "Naive Bayes",
        "accuracy": f"{model_accuracy}%",
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
        petal_width = float(request.args.get('petal_width', type=float))

        # Check if all required features are provided
        if None in [sepal_length, sepal_width, petal_length, petal_width]:
            return jsonify({"error": "Please provide all 4 features: sepal_length, sepal_width, petal_length, petal_width."}), 400

        # Prepare input data
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Make prediction using the Naive Bayes model
        prediction = naive_bayes_model.predict(input_data)[0]

        # Map the prediction to the corresponding class label (0: Setosa, 1: Versicolor, 2: Virginica)
        class_names = ['Setosa', 'Versicolor', 'Virginica']
        predicted_class = class_names[prediction]

        # Return the prediction
        return jsonify({
            "model_id": "naive_bayes_model",
            "prediction": predicted_class,
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": str(e), "status": "failure"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Use port 5001 for Naive Bayes model