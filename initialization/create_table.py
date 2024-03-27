import os
import pandas as pd
from sqlalchemy import create_engine, text

def create_table_from_csv():

    # Retrieve database connection details from environment variables
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')
    
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv("population.csv")
    
    # Create an engine to connect to your PostgreSQL database
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{username}')
    
    # Connect to the engine
    conn = engine.connect()

    # Create a table named "population" using the DataFrame's schema
    df.to_sql('population', con=engine, if_exists='replace', index=False)
    
    print("Table 'population' created successfully in the 'canada' schema.")

    conn.close()
    print("Connection closed")

if __name__ == "__main__":
    create_table_from_csv()