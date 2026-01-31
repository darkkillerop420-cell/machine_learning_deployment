from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# --- 1. LOAD THE BRAIN (Model) ---
# We load this outside the function so it only happens once (faster)
try:
    model = joblib.load('logistic_regression_model.joblib')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# --- 2. HOME ROUTE ---
@app.route('/')
def home():
    return "Voter Detective API is Live & Ready!"

# --- 3. PREDICTION ROUTE (The Smart Part) ---
@app.route('/predict', methods=['POST'])
def predict():
    # Safety Check: Did the model load?
    if not model:
        return jsonify({'error': 'Model failed to load on server'}), 500

    try:
        # Get the data from the user
        data = request.get_json()
        
        # Convert JSON to DataFrame (This is what your model expects)
        # IMPORTANT: The JSON keys must match the columns you trained on!
        input_data = pd.DataFrame([data])
        
        # Ask the model for a prediction
        prediction = model.predict(input_data)
        
        # Return the answer (0 or 1)
        return jsonify({'prediction': int(prediction[0])})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- 4. START THE SERVER ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
