"""Service to work with DB"""
import greenlet
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from config import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

session = scoped_session(SessionLocal, scopefunc=greenlet.getcurrent)
