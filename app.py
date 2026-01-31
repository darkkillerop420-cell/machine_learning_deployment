from flask import Flask, request, jsonify
import joblib
import pandas as pd
import joblib



app = Flask(__name__)
preprocessing_metadata = {
    'median_age': median_age,
    'feature_columns': X.columns.tolist()
}

joblib.dump(preprocessing_metadata, 'preprocessing_metadata.joblib')
print("Preprocessing metadata saved successfully as 'preprocessing_metadata.joblib'")
# Initialize the Flask app


# Load the trained model and preprocessing metadata
model = joblib.load('logistic_regression_model.joblib')
preprocessing_metadata = joblib.load('preprocessing_metadata.joblib')
…
    # Return the prediction as a JSON response
    return jsonify({'prediction': int(prediction[0])})

# This part is for running the app. In a typical deployment, a WSGI server would manage this.
 if __name__ == '__main__':
     app.run(debug=True)
