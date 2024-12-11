"""Service to work with DB"""
import greenlet
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from config import DB_USER, DB_PASS, DB_HOST, BD_HOST, DB_NAME

# TODO: Move it to .env
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{BD_HOST}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

session = scoped_session(SessionLocal, scopefunc=greenlet.getcurrent)
