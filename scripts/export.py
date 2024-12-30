import os

# Function to export the processed DataFrame
def export_data(df, output_path, file_format="csv"):
    """
    Export the DataFrame to a specified file format (CSV or Excel).

    Args:
        df (pd.DataFrame): DataFrame to export.
        output_path (str): Path to save the file.
        file_format (str): File format ("csv" or "excel"). Default is "csv".
    """
    if file_format == "csv":
        df.to_csv(output_path, index=False)
    elif file_format == "excel":
        df.to_excel(output_path, index=False, engin="openpyxl")
    else:
        raise ValueError("Unsupported file format. Choose 'csv' or 'excel'.")
    print(f"Data exported successfully to {output_path}")


