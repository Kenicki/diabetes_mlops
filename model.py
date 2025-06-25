import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Step 1: Load the dataset
data = pd.read_csv('diabetes.csv')

# Step 2: Separate features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Step 3: Split the dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 5: Save the model
joblib.dump(model, 'model.joblib')

print("✅ Model trained and saved as model.joblib")
