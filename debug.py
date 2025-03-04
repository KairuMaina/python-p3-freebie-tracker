from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb  # Import interactive debugging

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Load some test data
dev = session.query(Dev).first()
company = session.query(Company).first()
freebie = session.query(Freebie).first()

# Start debugging session
ipdb.set_trace()
