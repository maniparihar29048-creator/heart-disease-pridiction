import joblib
import numpy as np

# Load Model and Scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Example Input Data
# Format:
# [age, sex, cp, trestbps, chol,
#  fbs, restecg, thalach, exang,
#  oldpeak, slope, ca, thal]

sample_data = np.array([
    [52, 1, 0, 125, 212,
     0, 1, 168, 0,
     1.0, 2, 2, 3]
])

# Scale Data
scaled_data = scaler.transform(sample_data)

# Predict
prediction = model.predict(scaled_data)

# Output Result
if prediction[0] == 1:
    print("Heart Disease Detected")
else:
    print("No Heart Disease")