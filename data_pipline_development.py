import pandas as pd
def extract_data(file_path):
    df = pd.read_csv(file_path)
    print(" Data extracted.")
    return df
pipeline/transform.py
python
Copy
Edit
def transform_data(df):
    df_cleaned = df.dropna(subset=['age', 'salary'])  # Drop rows with missing age or salary
    df_cleaned['age'] = df_cleaned['age'].astype(int)
    df_cleaned['salary'] = df_cleaned['salary'].astype(float)
    print(" Data transformed.")
    return df_cleaned
pipeline/load.py
python
Copy
Edit
import sqlite3

def load_data(df, db_path="data/employees.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql('employees', conn, if_exists='replace', index=False)
    conn.close()
    print("Data loaded into SQLite DB.")
  run_pipeline.py
python
Copy
Edit
from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data
def run():
    print("Starting ETL pipeline...")
    
    # Step 1: Extract
    df = extract_data('data/sample_data.csv')
    
    # Step 2: Transform
    df_transformed = transform_data(df)
    
    # Step 3: Load
    load_data(df_transformed)
    
    print("ETL pipeline completed.")

if __name__ == "__main__":
    run()
How to Run
From the terminal:
bash
Copy
Edit
python run_pipeline.py
