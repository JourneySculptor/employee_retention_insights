import pandas as pd

# Calculate attrition rate by department
def calculate_attrition_rate_by_department(df):
    """
    Calculate and rank attrition rates by department.
    
    Args:
        df (pd.DataFrame): The dataset containing employee information.
    
    Returns:
        pd.DataFrame: A DataFrame containing departments and their attrition rates.
    """
    # Group by department and calculate attrition rate
    department_stats = df.groupby("Department")["Attrition"].mean().reset_index()
    department_stats.columns = ["Department", "Attrition Rate"]

    # Convert attrition rate to percentage
    department_stats["Attrition Rate"] = department_stats["Attrition Rate"] * 100

    # Sort by attrition rate in descending order
    ranked_departments = department_stats.sort_values(by="Attrition Rate", ascending=False)
    return ranked_departments

# Export department statistics to a CSV file
def export_department_statistics(department_stats, output_path):
    """
    Export department statistics to a CSV file.
    
    Args:
        department_stats (pd.DataFrame): DataFrame containing department statistics.
        output_path (str): Path to save the exported CSV file.
    """
    department_stats.to_csv(output_path, index=False)
    print(f"Department statistics exported successfully to {output_path}")
