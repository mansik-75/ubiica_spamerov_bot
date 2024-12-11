import datetime

from sqlalchemy import Column, BigInteger, String, DateTime

from service.database import Base


class CorrectUser(Base):
    __tablename__ = 'correct_user'

    id = Column(BigInteger, primary_key=True, index=True)
    chat_id = Column(BigInteger)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
