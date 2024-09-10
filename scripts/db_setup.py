import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy import text

#  load environment variable from env file

load_dotenv()

# get individual variables


DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')

# constructing the database URL

DATABASE_URL= f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class DataLoading:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        # Create an SQLAlchemy engine
        engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/telecom_db')
        
        # Define the SQL query
        query = text('SELECT * FROM xdr_data;')
        
        # Execute the query and load data into a DataFrame
        try:
            with engine.connect() as connection:
                result = connection.execute(query)
                df = pd.DataFrame(result.fetchall())
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of an error
        
        return df
    def get_customer_engagement_clusters(self):
        # Create an SQLAlchemy engine
        engine = create_engine(DATABASE_URL)
        
        # Define the SQL query
        query = text('SELECT * FROM customer_engagement_clusters;')
        
        # Execute the query and load data into a DataFrame
        try:
            with engine.connect() as connection:
                result = connection.execute(query)
                df = pd.DataFrame(result.fetchall())
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of an error
        
        return df
    def get_user_experiance_clusters(self):
        # Create an SQLAlchemy engine
        engine = create_engine(DATABASE_URL)
        
        # Define the SQL query
        query = text('SELECT * FROM "self.user_experiance_clusters";')
        
        # Execute the query and load data into a DataFrame
        try:
            with engine.connect() as connection:
                result = connection.execute(query)
                df = pd.DataFrame(result.fetchall())
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of an error
        
        return df

