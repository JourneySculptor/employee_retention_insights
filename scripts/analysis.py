import pandas as pd
import matplotlib.pyplot as plt

# Load and preprocess the dataset
def load_and_preprocess_data(file_path):
    """Load dataset and preprocess it by removing unnecessary columns and encoding gender."""
    df = pd.read_csv(file_path)
    df = df.drop(columns=["Employee_ID"])
    df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
    return df

# Visualize attrition distribution
def visualize_attrition_distribution(df):
    """Create a bar chart showing attrition distribution."""
    attrition_counts = df["Attrition"].value_counts()
    plt.figure(figsize=(6, 4))
    attrition_counts.plot(kind='bar', color=['lightgreen', 'tomato'])
    plt.title("Attrition Distribution (Stayed vs Left)")
    plt.xlabel("Attrition (0 = Stayed, 1 = Left)")
    plt.ylabel("Number of Employees")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Visualize average years at company by attrition
def visualize_average_years(df):
    """Create a bar chart showing average years at company for each attrition category."""
    avg_years_at_company = df.groupby('Attrition')['Years_at_Company'].mean()
    plt.figure(figsize=(6, 4))
    avg_years_at_company.plot(kind='bar', color=['lightgreen', 'tomato'])
    plt.title("Average Years at Company by Attrition")
    plt.xlabel("Attrition (0 = Stayed, 1 = Left)")
    plt.ylabel("Average Years")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Visualize satisfaction level distribution by attrition
def visualize_satisfaction_distribution(df):
    """Create histograms showing satisfaction level distribution for stayed and left employees."""
    bins = 20
    plt.figure(figsize=(10, 6))
    plt.hist(df[df['Attrition'] == 0]['Satisfaction_Level'], bins=bins, alpha=0.7, label='Stayed', color='skyblue', edgecolor='black')
    plt.hist(df[df['Attrition'] == 1]['Satisfaction_Level'], bins=bins, alpha=0.7, label='Left', color='tomato', edgecolor='black')
    plt.title("Satisfaction Level Distribution")
    plt.xlabel("Satisfaction Level")
    plt.ylabel("Number of Employees")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main function to run the analysis
def run_analysis():
    """Run all analysis and visualizations."""
    data_path = "data/raw/employee_attrition_data.csv"
    df = load_and_preprocess_data(data_path)
    visualize_attrition_distribution(df)
    visualize_average_years(df)
    visualize_satisfaction_distribution(df)

if __name__ == "__main__":
    run_analysis()
