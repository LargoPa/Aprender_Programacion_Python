import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

host = os.getenv("HOST_NAME")
port = os.getenv("PORT")
database = os.getenv("DB_NAME")
user = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

# Cambia la URL para MySQL
database_url = f"mysql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(database_url)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()
