from models import Question
from schemas import QuestionCreate, QuestionSchema
from sqlalchemy.orm import Session
from sqlalchemy import desc
import requests


def run_create(questions_num: int, db: Session) -> QuestionSchema:
    to_add = questions_num
    # Запускаем функцию для создания наших вопросов пока не получим нужное количество новых для нас вопросов
    while to_add > 0:
        added_count = create_questions(to_add, db)
        to_add -= added_count

    # Получаем из базы последний добавленный вопрос
    last_question = db.query(Question).order_by(desc(Question.date)).first()
    return last_question


def create_questions(num: int, db: Session) -> int:
    api_questions = requests.get("https://jservice.io/api/random?count={}".format(num)).json()
    # Создаем список объектов Pydantic, отбирая изполученных по api вопросов те, которых еще нет у нас в базе
    new_questions = [
        QuestionCreate(code=question["id"], body=question["question"], answer=question["answer"])
        for question in api_questions if not existed_question(question["id"], db)]
    # Формируем список объектов нашей модели и добавляем их в базу
    new_questions = [Question(code=question.code, body=question.body, answer=question.answer) for question in
                     new_questions]
    db.add_all(new_questions)
    db.commit()

    return len(new_questions)


# Проверка наличия в базе вопроса с данным кодом
def existed_question(code: int, db: Session) -> bool:
    question = db.query(Question).filter(Question.code == code).first()
    return True if question else False
