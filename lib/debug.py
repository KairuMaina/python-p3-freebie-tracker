from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

dev = session.query(Dev).first()
company = session.query(Company).first()
freebie = session.query(Freebie).first()

ipdb.set_trace()
