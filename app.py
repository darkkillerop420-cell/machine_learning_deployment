from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# --- TEST ROUTE ---
@app.route('/')
def home():
    return "SUCCESS: The Voter Detective API is Live!"

# --- DUMMY PREDICTION ROUTE (No Model Needed) ---
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # We just take the input and return a fake result for now
        # This proves the SERVER works, even if the model isn't there yet.
        data = request.get_json()
        
        fake_prediction = 0
        if data and data.get('age', 0) > 100:
            fake_prediction = 1
            
        return jsonify({'prediction': fake_prediction, 'status': 'Model bypassed for testing'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
