import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import os
import plotly.graph_objs as go
from azure.storage.blob import BlobServiceClient
from io import BytesIO

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
    db = os.environ.get('DB')
        
    # Create an engine to connect to your PostgreSQL database
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db}')
        
    # Connect to the engine
    conn = engine.connect()

    # Execute SQL statement and fetch the result into a Pandas DataFrame
    df = pd.read_sql_query(sql_statement, conn)
    
    # Close connection
    conn.close()

    # Fetch and return the result
    return df


def download_image_blob(blob_name):
    blob_string = os.environ.get('BLOB_STRING')
    blob_container_name = os.environ.get('BLOB_CONTAINER_NAME')

    blob_service_client = BlobServiceClient.from_connection_string(blob_string)
    blob_client = blob_service_client.get_blob_client(container=blob_container_name, blob=blob_name)
    blob_data = blob_client.download_blob().readall()
    return blob_data

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
    fig.update_layout(title='Population Trend', xaxis_title='Year', yaxis_title='Population',height=300)

    # Specify x-axis tick values to show only integer years
    fig.update_xaxes(tickmode='array', tickvals=df['year'].unique(), tickformat='d')
    
    # Display the Plotly line plot
    st.plotly_chart(fig)

    # Download image blob
    blob_name = f'maps/{province}.jpeg'
    image_data = download_image_blob(blob_name)

    # Display image
    st.subheader("Province Map:")
    st.image(BytesIO(image_data),height=300)

    # # Display Plotly chart and image side by side
    # col1, col2 = st.columns([1, 1])  # Split the layout into two columns
    # with col1:
    #     st.plotly_chart(fig)  # Display Plotly chart in the first column
    # with col2:
    #     st.subheader("Province Map:")
    #     st.image(BytesIO(image_data))  # Display image in the second column

if __name__ == "__main__":
    main()
