from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Connect to SQLite database
engine = create_engine('sqlite:///freebies.db')

# Create tables
Base.metadata.create_all(engine)

print("Database and tables created successfully!")
