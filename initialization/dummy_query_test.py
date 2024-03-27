from sqlalchemy import create_engine, text

def send_dummy_query():

    # Retrieve database connection details from environment variables
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')

    # Create an engine to connect to your PostgreSQL database
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{username}')
    
    # Connect to the engine
    conn = engine.connect()
    
    # Execute a dummy query
    query = text("SELECT 1")
    result = conn.execute(query)
            
    # Fetch the result
    print("Dummy query result:", result.scalar())

    conn.close()
    print("Connection closed")

if __name__ == "__main__":
    send_dummy_query()