from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input from form
        values = [float(x) for x in request.form.values()]
        input_array = np.array([values])
        
        # Make prediction
        prediction = model.predict(input_array)
        result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'

        return render_template('index.html', prediction_text=f'Prediction: {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

# Run the app locally
if __name__ == '__main__':
    app.run(debug=True)

