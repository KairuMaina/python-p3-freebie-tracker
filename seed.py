from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

# Create Companies
google = Company(name="Google", founding_year=1998)
apple = Company(name="Apple", founding_year=1976)

# Create Devs
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# Commit companies and devs first to assign IDs
session.add_all([google, apple, alice, bob])
session.commit()

# Create Freebies
freebie1 = Freebie(item_name="Sticker", value=5, dev=alice, company=google)
freebie2 = Freebie(item_name="Mug", value=10, dev=bob, company=apple)

# Add Freebies
session.add_all([freebie1, freebie2])
session.commit()

print("Database seeded successfully!")
