#Import Required Modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Define base class
Base = declarative_base()


#Define company model
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)

    freebies = relationship('Freebie', backref='company')

    #Company methods
    def give_freebie(self, dev, item_name, value):
        """Give a freebie to a developer."""
        return Freebie(item_name=item_name, value=value, dev=dev, company=self)

    @classmethod
    def oldest_company(cls, session):
        """Find the oldest company."""
        return session.query(cls).order_by(cls.founding_year).first()

#Define Dev model
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    freebies = relationship('Freebie', backref='dev')
#Dev methods
    def received_one(self, item_name):
        """Check if a dev received a specific freebie."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        """Give a freebie to another developer."""
        if freebie in self.freebies:
            freebie.dev = dev

#Define Freebie
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    def print_details(self):
        """Print freebie details."""
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
