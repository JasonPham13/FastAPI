from fastapi import APIRouter, Response, Depends, status
from repository import user_repository
from sqlalchemy.orm import Session
from db_config import get_db
from schemas import UserModel

router = APIRouter(
    prefix = "/users/v1",
    tags = ["users"]
)


@router.get("/", response_description="Displays all users", description="Retrieves all users", response_model=list[UserModel])
def get_users(response: Response, db: Session = Depends(get_db)):
    return_value = user_repository.get_all_users(db)
    response.status_code = status.HTTP_200_OK
    return return_value


@router.get("/username}", response_description="Displays user by username", description="Retrieves user by username", response_model=UserModel)
def get_by_username(username: str, response: Response, db: Session = Depends(get_db)):
    return_value = user_repository.get_by_username(db, username)
    response.status_code = status.HTTP_200_OK
    return return_value