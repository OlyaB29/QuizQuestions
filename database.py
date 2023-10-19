from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

# DB_USER=os.getenv("DB_USER")
# DB_PASSWORD=os.getenv("DB_PASSWORD")
# DB_NAME=os.getenv("DB_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")

# DATABASE_URL = 'postgresql+psycopg2://{}:{}@localhost:5432/{}'.format(DB_USER, DB_PASSWORD, DB_NAME)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
