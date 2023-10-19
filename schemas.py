from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InputSchema(BaseModel):
    questions_num: int


class QuestionCreate(BaseModel):
    code: int
    body: str
    answer: str


class QuestionSchema(QuestionCreate):
    id: int
    date: datetime

    class Config:
        orm_mode = True
