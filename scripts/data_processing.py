import pandas as pd

# Function to load and preprocess the dataset
def load_and_preprocess_data(file_path):
    """
    Load the dataset, preprocess data, and add new features.
    
    Args:
        file_path (str): Path to the dataset file.
    
    Returns:
        pd.DataFrame: Preprocessed dataset with new features.
    """
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Remove unnecessary column
    df = df.drop(columns=["Employee_ID"])
    
    # Encode gender as 0 (Male) and 1 (Female)
    df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
    
    # Create new feature Satisfaction_Hours
    df["Satisfaction_Hours"] = df["Satisfaction_Level"] * df["Average_Monthly_Hours"]
    
    # Categorize Salary into Salary_Rank
    df["Salary_Rank"] = pd.cut(
        df["Salary"],
        bins=[0, 50000, 80000, float("inf")],
        labels=["Low", "Medium", "High"]
    )

    # Create a new feature Satisfaction_Tenure
    df["Satisfaction_Tenure"] = df["Satisfaction_Level"] * df["Years_at_Company"]

    # Create a new feature Department_Attrition_Rate
    department_attrition_rate = df.groupby("Department")["Attrition"].mean()
    df["Department_Attrition_Rate"] = df["Department"].map(department_attrition_rate)
    
    # Add a new feature: Department_Satisfaction_Impact
    df["Department_Satisfaction_Impact"] = (
        df["Department_Attrition_Rate"] * df["Satisfaction_Level"]
    )
    return df

# Create a new feature Satisfaction_Per_Hour
def add_satisfaction_per_hour(df):
    """
    Add a new feature Satisfaction_Per_Hour to measure efficiency.

    Args:
        df (pd.DataFrame): Original dataset.

    Returns:
        pd.DataFrame: Dataset with the new feature added.
    """
    df["Satisfaction_Per_Hour"] = df["Satisfaction_Level"] / df["Average_Monthly_Hours"]
    return df

# Add interaction features
def add_interaction_features(df):
    """
    Add interaction features to the dataset.

    Args:
        df (pd.DataFrame): Preprocessed dataset.

    Returns:
        pd.DataFrame: Dataset with interaction features added.
    """
    # Interaction between age and satisfaction level
    df["Age_Satisfaction"] = df["Age"] * df["Satisfaction_Level"]

    # Interaction between salary and years at the company
    df["Salary_Tenure"] = df["Salary"] * df["Years_at_Company"]

    return df

