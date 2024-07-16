import os
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor

from .config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# Connection sequence for sqlalchemy database url
# postgresql://<username>:<password>@<ip-address/host>/<database-name>
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

""" 
SQLAlchemy, Connecting to PostGres DB. To be used if one needs to query db with raw SQL
"""
HOST=os.getenv('HOST')
DATABASE_NAME=os.getenv('DATABASE_NAME')
USER=os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')

def ConnectDb():
    while True:
        try:
            conn = psycopg2.connect(host=HOST, database=DATABASE_NAME, user=USER, password=PASSWORD, cursor_factory=RealDictCursor)
            cursor = conn.cursor()
            print("Database connection was successful")
            break
        except Exception as error:
            print("Connection to database failed")
            print(f"error : {error}")
            time.sleep(2)