import pandas as pd

# Filter data based on salary threshold
def filter_by_salary(df, salary_threshold):
    """
    Filter employees with a salary above the given threshold.

    Args:
        df (pd.DataFrame): The dataset containing employee information.
        salary_threshold (int): Minimum salary threshold.

    Returns:
        pd.DataFrame: Filtered dataset.
    """
    return df[df["Salary"] > salary_threshold] 

# Filter data by departmet
def filter_by_department(df, department_name):
    """
    Filter employees in a specific department.

    Args:
        df (pd.DataFrame): The dataset containing employee information.
        department_name (str): The name of the department to filter.

    Returns:
        pd.DataFrame: Filtered dataset.
    """
    return df[df["Department"] == department_name]