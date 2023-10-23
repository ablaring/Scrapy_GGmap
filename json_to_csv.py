import pandas as pd

def json_to_csv(json_filepath, csv_filepath):
    # Read the JSON file into a DataFrame
    df = pd.read_json(json_filepath)

    # Write the DataFrame to a CSV file
    df.to_csv(csv_filepath, index=False)  # Set index=False to prevent writing row indices

# Specify the file paths
json_filepath = './data/boulangerie.json'  # Replace with your JSON file path
csv_filepath = './data/boulangerie.csv'   # Replace with your desired CSV file path

# Call the function
json_to_csv(json_filepath, csv_filepath)
