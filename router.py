from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import QuestionSchema,InputSchema
import db_service

router = APIRouter()


@router.post('/create', response_model=QuestionSchema)
async def create(input: InputSchema, db: Session = Depends(get_db)):
    return db_service.run_create(input.questions_num, db)


