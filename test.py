from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Fetch Data
google = session.query(Company).filter_by(name="Google").first()
alice = session.query(Dev).filter_by(name="Alice").first()
bob = session.query(Dev).filter_by(name="Bob").first()

# Test give_freebie
google.give_freebie(alice, "T-shirt", 20, )

# Test received_one
print(f"Alice received T-shirt: {alice.received_one('T-shirt')}")  # Should print True

# Test oldest_company
oldest = Company.oldest_company(session)
print(f"Oldest Company: {oldest.name} (Founded: {oldest.founding_year})")  # Should print Apple

# Test give_away
freebie = session.query(Freebie).filter_by(item_name="Sticker").first()
alice.give_away(bob, freebie,)
print(f"Bob received Sticker: {bob.received_one('Sticker')}")  # Should print True

# Test print_details
print(freebie.print_details())  # Should print Bob owns a Sticker from Google
