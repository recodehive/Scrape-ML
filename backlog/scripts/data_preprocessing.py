import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def remove_duplicates(data):
    return data.drop_duplicates()

def handle_missing_values(data):
    data = data.replace('', np.nan)
    return data

def normalize_text(data, column):
    data[column] = data[column].str.lower().str.replace('[^a-z0-9]', ' ')
    return data

def clean_data(data):
    data = remove_duplicates(data)
    data = handle_missing_values(data)
    data = normalize_text(data, 'user_review')
    return data

def preprocess_data(file_path):
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    return cleaned_data

if __name__ == "__main__":
    input_file = '../data_scrapped/data.csv'
    output_file = '../data_scrapped/cleaned_data.csv'
    cleaned_data = preprocess_data(input_file)
    cleaned_data.to_csv(output_file, index=False)