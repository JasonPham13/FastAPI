import uvicorn
from fastapi import FastAPI, Response, status, Depends
from db import user_db
from db_config import engine
from repository import user_repository
from sqlalchemy.orm import Session
from db_config import get_db
from router import app_router, users_router


app = FastAPI(
    title="Jason's-FastAPI",
    description="This is the swagger spec for my FastApi",
    version='1.0.0'
)

app.include_router(app_router.router)
app.include_router(users_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)







# @app.get('/dbsetup')
# def create_db(db: Session = Depends(get_db)):
#       user_db.Base.metadata.drop_all(engine)
#       user_db.Base.metadata.create_all(engine)
#       user_repository.add_user_td(db)
#       response_text = '{"message": "Database created." }'
#       response = Response(content=response_text, status_code=200, media_type= 'application/json')
#       return response