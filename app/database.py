from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# --------------------------------------------------
# Load environment variables from a .env file
# Used to securely store sensitive settings like DATABASE_URL
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Get the database connection URL from the environment
# Example: sqlite:///./test.db or PostgreSQL URL
# --------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

# --------------------------------------------------
# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False} is specific to SQLite
# --------------------------------------------------
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# --------------------------------------------------
# Create a configured session class
# autocommit=False: you must explicitly commit
# autoflush=False: prevents automatic flushing of data
# --------------------------------------------------
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# --------------------------------------------------
# Base class for all ORM models
# All models will inherit from this to get table mapping features
# --------------------------------------------------
Base = declarative_base()

# --------------------------------------------------
# Dependency function for creating a database session
# Used with FastAPI's dependency injection
# Automatically closes session after request completes
# --------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide the session
    finally:
        db.close()  # Ensure the session is closed to free resources
