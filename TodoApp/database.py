from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# This is the correct connection string for the PostgreSQL server we set up
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456781@localhost:5432/todoapp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
















































