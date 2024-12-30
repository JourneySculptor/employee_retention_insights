import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def calculate_feature_importance(df):
    """
    Calculate and plot feature importance using Random Forest.

    Args:
        df (pd.DataFrame): Dataset containing employee information.

    Returns:
        None
    """
    # Select features and target variable
    features = [
        "Age", "Gender", "Satisfaction_Hours", "Salary_Rank",
        "Department_Attrition_Rate", "Satisfaction_Tenure", "Satisfaction_Per_Hour"
    ]
    X = pd.get_dummies(df[features], drop_first=True)
    y = df["Attrition"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Calculate feature importance
    importances = model.feature_importances_
    feature_names = X.columns

    # Create a DataFrame for visualization
    importance_df = pd.DataFrame({"Feature": feature_names, "Importance": importances})
    importance_df = importance_df.sort_values(by="Importance", ascending=False)

    # Plot the feature importance
    plt.figure(figsize=(10, 6))
    plt.bar(importance_df["Feature"], importance_df["Importance"], color="skyblue")
    plt.title("Feature Importance")
    plt.xlabel("Features")
    plt.ylabel("Importance")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    print("\nFeature Importance:")
    print(importance_df)

# Example usage
if __name__ == "__main__":
    data_path = "data/processed/employee_attrition_data_processed.csv"
    df = pd.read_csv(data_path)
    calculate_feature_importance(df)
