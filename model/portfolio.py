from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model import Base


class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    quantity = Column(Float)
    price = Column(Float)

    # Define a new column to store the user ID
    user_id = Column(Integer, ForeignKey('users.id'))

    # Define a relationship with the User class
    user = relationship("Users", back_populates="portfolio")