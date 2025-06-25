# 🩺 Diabetes Prediction Web App

This is a machine learning web application that predicts whether a patient is diabetic or not based on clinical data. It uses a Decision Tree Classifier trained on the Pima Indians Diabetes dataset.

## 🚀 Live App

👉 [Click here to try the app](https://diabetes-mlops-e9ga.onrender.com)


---

## 📊 Input Features

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

The model outputs:
- ✅ `Not Diabetic` or ❌ `Diabetic`

---

## 🧠 Machine Learning

- **Algorithm**: Decision Tree Classifier
- **Library**: `scikit-learn`
- **Model Training**: Trained using `train_test_split` on 80/20 split
- **Model Serialization**: Saved with `joblib`

---

## 🛠 Tech Stack

| Layer     | Tech               |
|-----------|--------------------|
| Language  | Python             |
| ML        | Scikit-learn       |
| Backend   | Flask              |
| Frontend  | HTML (Jinja2 Templating) |
| Hosting   | Render (Free Tier) |
| Version Control | Git + GitHub |

---

## 📦 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Kenicki/diabetes_mlops.git
cd diabetes-mlops

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate     # (Windows)
# source .venv/bin/activate  # (macOS/Linux)

# Install dependencies
pip install -r requirements.txt

# Train model (only once)
python model.py

# Run app
python app.py
