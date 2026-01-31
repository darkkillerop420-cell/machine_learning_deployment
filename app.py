from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(_name_)

# 1. LOAD THE MODEL ONCE (Global Scope)
# This prevents reloading the model on every request, which is faster.
try:
    # Load your model and metadata
    model = joblib.load('logistic_regression_model.joblib')
    preprocessing_metadata = joblib.load('preprocessing_metadata.joblib')
    print("Model and metadata loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return "Voter Detective API is Running!"

# 2. DEFINE THE PREDICTION ROUTE
# The logic you had on line 27 belongs INSIDE this function
@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        # Get JSON data sent from the frontend
        data = request.get_json()
        
        # Example: accessing data like data['age']
        # You need to adapt this part to match exactly what your model expects!
        # For now, I'm just showing how to structure the return.
        
        # prediction = model.predict([data_to_predict]) 
        # result = int(prediction[0])
        
        # Placeholder result for now so the code runs:
        result = 0 
        
        return jsonify({'prediction': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# 3. START THE SERVER
if _name_ == "_main_":
    # Render assigns a random port to the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
