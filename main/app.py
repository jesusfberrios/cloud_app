import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import os
import plotly.graph_objs as go

# Define a list of provinces
provinces = ["Canada", "Newfoundland and Labrador", "Prince Edward Island", "Nova Scotia", "New Brunswick", "Quebec", "Ontario", "Manitoba", "Saskatchewan", "Alberta", "British Columbia", "Yukon", "Northwest Territories", "Nunavut"]

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

    # Execute SQL statement and fetch the result into a Pandas DataFrame
    df = pd.read_sql_query(sql_statement, conn)
    
    # Close connection
    conn.close()

    # Fetch and return the result
    return df


# Main Streamlit app
def main():
    st.title("Population Data by Province")
    
    # Province selection dropdown
    province = st.selectbox("Select a province:", provinces)
    
    # Generate SQL statement based on selected province
    sql_statement = generate_sql_statement(province)
    
    # Execute SQL statement and get the result as a DataFrame
    df = execute_sql_statement(sql_statement)
    
    # Plot the data using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['year'], y=df['population'], mode='lines+markers', name='Population'))
    fig.update_layout(title='Population Trend', xaxis_title='Year', yaxis_title='Population')
    
    # Display the Plotly line plot
    st.plotly_chart(fig)

    # Display result as a DataFrame
    st.subheader("Result:")
    st.write(df)

if __name__ == "__main__":
    main()
