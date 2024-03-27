import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import os

# Define a list of provinces
provinces = ["Ontario", "Quebec", "British Columbia", "Alberta", "Manitoba", "Saskatchewan", "Nova Scotia", "New Brunswick", "Prince Edward Island", "Newfoundland and Labrador"]

# Function to generate SQL statement based on selected province
def generate_sql_statement(province):
    return f"SELECT * FROM public.population WHERE geography = '{province}'"

# Function to execute SQL statement
def execute_sql_statement(sql_statement):
    
    # Retrieve database connection details from environment variables
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')
        
    # Create an engine to connect to your PostgreSQL database
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{username}')
        
    # Connect to the engine
    conn = engine.connect()

    # Execute SQL statement
    result = conn.execute(sql_statement)
    
    # Close connection
    conn.close()
    # Fetch and return the result
    return result.fetchall()


# Main Streamlit app
def main():
    st.title("Population Data by Province")
    
    # Province selection dropdown
    province = st.selectbox("Select a province:", provinces)
    
    # Generate SQL statement based on selected province
    sql_statement = generate_sql_statement(province)
    
    # Execute SQL statement
    result = execute_sql_statement(text(sql_statement))
    
    # Display result
    st.subheader("Result:")
    st.write(result)

if __name__ == "__main__":
    main()
