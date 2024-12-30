import sys
import os
import pandas as pd
from scripts.feature_importance import calculate_feature_importance

# Add project root to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules and functions
from scripts.data_processing import load_and_preprocess_data, add_satisfaction_per_hour
from scripts.export import export_data
from scripts.analytics import calculate_attrition_rate_by_department, export_department_statistics
from scripts.visualizations import plot_attrition_by_department, plot_high_salary_attrition
from scripts.filtering import filter_by_salary, filter_by_department
from scripts.model_training import train_model 

# Main function to run the project
def main():
    # File paths
    data_path = "data/raw/employee_attrition_data.csv"
    processed_output_path = "data/processed/employee_attrition_data_processed.csv"
    analytics_output_path = "data/processed/department_statistics.csv"
    high_salary_output_path = "data/processed/high_salary_employees.csv"
    sales_department_output_path = "data/processed/sales_department_employees.csv"
    high_salary_plot_path = "data/processed/high_salary_attrition_plot.png"
    department_plot_path = "data/processed/department_attrition_rate_plot.png"

    # Load and preprocess data
    df = load_and_preprocess_data(data_path)

    # Add the new feature to the dataset
    df = add_satisfaction_per_hour(df)

    # Export processed data
    export_data(df, processed_output_path, file_format="csv")

    # Calculate and export department statistics
    department_stats = calculate_attrition_rate_by_department(df)
    export_department_statistics(department_stats, analytics_output_path)

    # Visualize department-wise attrition rate
    plot_attrition_by_department(department_stats, output_path=department_plot_path)

    # Filter employees with a salary above 70,000
    high_salary_df = filter_by_salary(df, salary_threshold=70000)
    print("\nEmployees with salary above 70,000:")
    print(high_salary_df.head())
    export_data(high_salary_df, high_salary_output_path, file_format="csv")

    # Visualize attrition rate for high salary employees
    plot_high_salary_attrition(df, salary_threshold=70000, output_path=high_salary_plot_path)

    # Filter employees in the Sales department
    sales_department_df = filter_by_department(df, department_name="Sales")
    print("\nEmployees in the Sales department:")
    print(sales_department_df.head())
    export_data(sales_department_df, sales_department_output_path, file_format="csv")

    # Train and evaluate the attrition prediction model with XGBoost
    print("\nTraining Attrition Prediction Model:")
    train_model(df)  

    # Display new features
    print("\nNew Features Created:")
    print(df[["Satisfaction_Hours", "Salary_Rank"]].head())

    # Calculate and display feature importance
    print("\nCalculating Feature Importance:")
    calculate_feature_importance(df)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("scripts.api:app", host="127.0.0.1", port=8000, reload=True)


