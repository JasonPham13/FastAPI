from fastapi import FastAPI, Response, status, Depends
from db import user_db
from db_config import engine
from repository import user_repository
from sqlalchemy.orm import Session
from db_config import get_db

app = FastAPI(
    title="Jason's-FastAPI",
    description="This is the swagger spec for my FastApi",
    version='1.0.0'
)




@app.get("/", tags=['welcome'], response_description="Displays welcome message")
async def welcome(response: Response):
        response.status_code = status.HTTP_200_OK
        return {"message":  "Hello, welcome to Jason's API"}


@app.get("/health", tags=['health'], response_description="Retrieves health status of this application")
def health(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "OK" }


@app.get('/dbsetup')
def create_db(db: Session = Depends(get_db)):
      user_db.Base.metadata.drop_all(engine)
      user_db.Base.metadata.create_all(engine)
      user_repository.add_user_td(db)
      response_text = '{"message": "Database created." }'
      response = Response(content=response_text, status_code=200, media_type= 'application/json')
      return response