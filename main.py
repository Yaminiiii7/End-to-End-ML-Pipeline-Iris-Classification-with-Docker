from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model
model = joblib.load("iris_classifier.pkl")  

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API"}

@app.get("/predict")
#POST /predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2
def predict_iris(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], 
                              columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    return {"predicted_class": prediction[0]}       
