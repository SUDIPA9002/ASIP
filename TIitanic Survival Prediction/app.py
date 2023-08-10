from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('trained_model.pkl')

# Define a function to preprocess the input data
def preprocess_input(input_data):
    # Preprocess the input data (make sure it matches the format used during training)
    input_df = pd.DataFrame(input_data, index=[0])  # Add 'index=[0]' to set a single row index
    input_df.replace({'Sex': {'male': 0, 'female': 1}, 'Embarked': {'S': 0, 'C': 1, 'Q': 2}}, inplace=True)
    return input_df

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        input_data = request.form.to_dict()

        # Preprocess the input data
        input_df = preprocess_input(input_data)

        # Make predictions using the loaded model
        predictions = model.predict(input_df)

        # Convert predictions to human-readable format (e.g., 'Survived' or 'Not Survived')
        results = []
        for prediction in predictions:
            if prediction == 0:
                results.append('Not Survived')
            else:
                results.append('Survived')

        return render_template('index.html', results=results)

    except Exception as e:
        return render_template('index.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
