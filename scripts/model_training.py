import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def train_model(df):
    """
    Train an XGBoost model to predict attrition and evaluate its performance.

    Args:
        df (pd.DataFrame): Processed dataset.

    Returns:
        model: Trained XGBoost model.
    """
    # Define features to use for training
    features = [
        "Age", "Gender", "Satisfaction_Hours", "Salary_Rank",
        "Department_Attrition_Rate", "Satisfaction_Tenure", "Satisfaction_Per_Hour"
    ]
    # Prepare feature matrix X and target vector y
    X = pd.get_dummies(df[features], drop_first=True)
    y = df["Attrition"]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the XGBoost model
    model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train)

    # Evaluate the model's performance
    y_pred = model.predict(X_test)
    print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # Return the trained model for use in predictions
    return model
