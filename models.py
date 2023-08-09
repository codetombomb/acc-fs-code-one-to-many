from sqlalchemy import Column, Integer, String, DateTime, func, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Owner(Base):
    __tablename__ = "owners"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Add pets attribute to get pets related to user
    
    
    def __repr__(self):
        return f"\n<Owner" \
            + f"id={self.id}, " \
            + f"username={self.username}, " \
            + f"email={self.email}, " \
            + f"created_at={self.created_at}, " \
            + f"updated_at={self.updated_at}" \
            + ">"
            
class Pet(Base):
    __tablename__ = "pets"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    color = Column(String)
    weight = Column(Float)
    
    # Add owner_id foreign key to pets
    
    
    def __repr__(self):
        return f"\n<Pet " \
            + f"id={self.id}, " \
            + f"name={self.name}, " \
            + f"species={self.species}, " \
            + f"breed={self.breed}, " \
            + f"age={self.age}, " \
            + f"color={self.color}, " \
            + f"weight={self.weight}" \
            + ">"
    
    





