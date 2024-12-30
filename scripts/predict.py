import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Function to train and evaluate a logistic regression model
def train_and_evaluate_model(df):
    """
    Train and evaluate a logistic regression model to predict employee attrition.
    
    Args:
        df (pd.DataFrame): The preprocessed dataset.
        
    Returns:
        LogisticRegression: The trained logistic regression model.
    """
    # Select features and target variable
    X = df[['Age', 'Gender', 'Years_at_Company', 'Satisfaction_Level', 'Average_Monthly_Hours']]
    y = df['Attrition']

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    return model


