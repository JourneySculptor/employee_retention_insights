import matplotlib.pyplot as plt

# Function to visualize attrition rate by department
def plot_attrition_by_department(department_stats, output_path=None):
    """
    Plot and optionally save the attrition rate by department.
    
    Args:
        department_stats (pd.DataFrame): DataFrame containing 'Department' and 'Attrition Rate'.
        output_path (str, optional): Path to save the plot. Defaults to None.
    """
    plt.figure(figsize=(8, 6))
    plt.bar(department_stats['Department'], department_stats['Attrition Rate'], color='skyblue')
    plt.title("Attrition Rate by Department")
    plt.xlabel("Department")
    plt.ylabel("Attrition Rate (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot if an output path is provided
    if output_path:
        plt.savefig(output_path)
    
    plt.show()

# Function to visualize attrition rate for high salary employ
def plot_high_salary_attrition(df, salary_threshold, output_path=None):
    """
    Visualize attrition rate for employees with high salaries.
    
    Args:
        df (pd.DataFrame): The dataset containing employee information.
        salary_threshold (int): The salary threshold to filter employees.
        output_path (str): Optional. Path to save the plot as an image file.
    """
    # Filter employees with salary above the threshold
    high_salary_df = df[df["Salary"] >= salary_threshold]

    # Calculate attrition rate
    attrition_rate = high_salary_df.groupby("Attrition").size()
    attrition_rate.index = ["Stayed", "Left"]

    # Plot the bar graph
    plt.figure(figsize=(6, 4))
    attrition_rate.plot(kind="bar", color=["lightgreen", "tomato"])
    plt.title(f"Attrition Rate for Employees with Salary >= {salary_threshold}")
    plt.xlabel("Attrition (0 = Stayed, 1 = Left)")
    plt.ylabel("Number of Employees")
    plt.xticks(rotation=0)
    plt.tight_layout()

    # Save or show the plot
    if output_path:
        plt.savefig(output_path)
        print(f"Plot saved successfully to {output_path}")
    else:
        plt.show()


