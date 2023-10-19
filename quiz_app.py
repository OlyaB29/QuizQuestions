import uvicorn
from fastapi import FastAPI
import router
from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router.router)


if __name__ == '__main__':
    uvicorn.run(
        'quiz_app:app',
        host='0.0.0.0',
        port=8080,
        reload=True
    )
