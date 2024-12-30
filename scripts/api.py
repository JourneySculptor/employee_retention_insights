from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from scripts.model_training import train_model

# Initialize FastAPI application
app = FastAPI()

# Define input data schema
class EmployeeData(BaseModel):
    Age: int
    Gender: int
    Satisfaction_Hours: float
    Salary_Rank: str
    Department_Attrition_Rate: float
    Satisfaction_Tenure: float
    Satisfaction_Per_Hour: float

# Load the dataset and train the model
df = pd.read_csv("data/processed/employee_attrition_data_processed.csv")
model = train_model(df)

@app.get("/")
def health_check():
    """
    Check if the API is running successfully.
    """
    return {"message": "API is running successfully"}

@app.post("/predict")
def predict_attrition(employee_data: EmployeeData):
    """
    Predict attrition based on input data.
    
    Args:
        employee_data (EmployeeData): Input data from the user.
    Returns:
        dict: Prediction result (Yes/No).
    """
    if model is None:
        return {"error": "Model is not loaded or initialized."}

    # 1) Make DataFrame from request
    input_data = pd.DataFrame([employee_data.dict()])

    # 2) Apply the same one-hot encoding as training
    input_data = pd.get_dummies(input_data, columns=["Salary_Rank"], drop_first=True)

    # 3) Align columns with the trained model
    training_cols = model.get_booster().feature_names
    for col in training_cols:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[training_cols]

    # 4) Predict and return
    prediction = model.predict(input_data)[0]
    return {"Attrition Prediction": "Yes" if prediction == 1 else "No"}
