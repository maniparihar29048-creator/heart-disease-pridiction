import pandas as pd
import joblib

model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

sample_data = pd.DataFrame([[
    52,1,0,125,212,0,1,168,0,1.0,2,2,3
]], columns=[
    'age','sex','cp','trestbps','chol','fbs',
    'restecg','thalach','exang','oldpeak',
    'slope','ca','thal'
])

scaled_data = scaler.transform(sample_data)

prediction = model.predict(scaled_data)

if prediction[0] == 1:
    print("Heart Disease Detected")
else:
    print("No Heart Disease")
