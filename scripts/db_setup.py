from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

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


# create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# create a session
SessionalLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# create a base class for our models
Base = declarative_base()