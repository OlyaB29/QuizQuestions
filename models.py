from sqlalchemy import Integer, Column, String, Text, DateTime
from database import Base
from datetime import datetime


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, unique=True)
    body = Column(Text, nullable=False)
    answer = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.now)

