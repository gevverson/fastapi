from sqlalchemy import Boolean,Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True)
    username=Column(String,unique=True,index=True)
    first_name=Column(String)
    last_name=Column(String)
    hashed_password=Column(String)
    is_active=Column(Boolean,default=True)
    phone_number=Column(String)
    address_id=Column(Integer,ForeignKey("address.id"),nullable=True)

    todos=relationship("Todos",back_populates="owner")
    
    # --- THIS IS THE FIX ---
    # You were missing this relationship. 
    # This links Users -> Address
    address = relationship("Address", back_populates="user")


class Todos(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    complete=Column(Boolean,default=False)
    owner_id=Column(Integer,ForeignKey("users.id"))

    owner=relationship("Users",back_populates="todos")


class Address(Base):
    __tablename__="address"

    id=Column(Integer,primary_key=True,index=True)
    address1=Column(String)
    address2=Column(String, nullable=True) # I made this nullable, in case address2 is optional
    city=Column(String)
    state=Column(String)
    country=Column(String)
    postalcode=Column(String)
    apt_num=Column(Integer)

    # --- THIS IS THE FIX ---
    # Renamed "user_address" to "user" to match the "address" relationship above
    # This links Address -> Users
    user = relationship("Users", back_populates="address")














