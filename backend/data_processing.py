# import pandas as pd

# def convert_csv_to_excel(csv_file, excel_file):
#     df = pd.read_csv(csv_file)
#     df.to_excel(excel_file, index=False)

# def convert_csv_to_json(csv_file, json_file):
#     df = pd.read_csv(csv_file)
#     df.to_json(json_file, orient='records', lines=True)


import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_csv_to_excel(csv_file, excel_file, sheet_name='Sheet1'):
    """
    Convert a CSV file to an Excel file.

    Parameters:
        csv_file (str): The path to the CSV file.
        excel_file (str): The path where the Excel file will be saved.
        sheet_name (str): The name of the sheet in the Excel file. Default is 'Sheet1'.
    """
    try:
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file '{csv_file}' not found.")
        
        df = pd.read_csv(csv_file)
        df.to_excel(excel_file, index=False, sheet_name=sheet_name)
        logging.info(f"Successfully converted '{csv_file}' to '{excel_file}'.")

    except Exception as e:
        logging.error(f"Error converting '{csv_file}' to Excel: {e}")
        raise

def convert_csv_to_json(csv_file, json_file, orient='records', lines=True):
    """
    Convert a CSV file to a JSON file.

    Parameters:
        csv_file (str): The path to the CSV file.
        json_file (str): The path where the JSON file will be saved.
        orient (str): The format of the JSON output. Default is 'records'.
        lines (bool): Whether to write JSON objects line by line. Default is True.
    """
    try:
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file '{csv_file}' not found.")
        
        df = pd.read_csv(csv_file)
        df.to_json(json_file, orient=orient, lines=lines)
        logging.info(f"Successfully converted '{csv_file}' to '{json_file}'.")

    except Exception as e:
        logging.error(f"Error converting '{csv_file}' to JSON: {e}")
        raise

# if __name__ == "__main__":
#     # Example usage for testing
#     try:
#         convert_csv_to_excel('output.csv', 'data.xlsx')
#         convert_csv_to_json('output.csv', 'data.json')
#     except Exception as e:
#         logging.error(f"Processing failed: {e}")
