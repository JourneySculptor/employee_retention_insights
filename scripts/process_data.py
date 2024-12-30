from data_processing import load_and_preprocess_data, add_satisfaction_per_hour, add_interaction_features

# Path to raw dataset
file_path = "data/raw/employee_attrition_data.csv"

# Preprocess data and add features
df = load_and_preprocess_data(file_path)
df = add_satisfaction_per_hour(df)
df = add_interaction_features(df)

# Save processed dataset to the correct directory
processed_file_path = "data/processed/employee_attrition_data_processed.csv"
df.to_csv(processed_file_path, index=False)

print(f"Processed dataset saved to {processed_file_path}")
