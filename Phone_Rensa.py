import pandas as pd
import os

def clean_phone_data():
    # Define input and output file paths
    input_path = "exports/phonelists.csv"
    output_path = "exports/phonelists_cleaned.csv"

    # Check if the input file exists
    if not os.path.exists(input_path):
        return "Error: phonelists.csv not found. Please fetch the file first."

    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_path)

    # Ensure that the necessary columns exist in the file
    if "Country" not in df.columns or "ConsentToContact" not in df.columns:
        return "Error: Required columns are missing from the CSV file."

    # Filter the data: only keep rows where Country is "Sverige" and ConsentToContact is True
    df_cleaned = df[(df["Country"] == "Sverige") & (df["ConsentToContact"] == True)]

    # If no matching rows are found, return a message
    if df_cleaned.empty:
        return "No valid entries found (Sverige + ConsentToContact=true)."

    # If cleaned file already exists, skip saving to avoid overwriting
    if os.path.exists(output_path):
        return "Data already cleaned. Skipping."

    # Save the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_path, index=False)

    # Return success message
    return f"Data cleaned successfully. Saved to {output_path}"
