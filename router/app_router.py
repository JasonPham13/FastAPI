from fastapi import APIRouter
from fastapi import Response, status

router = APIRouter()

@router.get("/", tags=['welcome'], response_description="Displays welcome message")
async def welcome(response: Response):
        response.status_code = status.HTTP_200_OK
        return {"message":  "Hello, welcome to Jason's API"}


@router.get("/health", tags=['health'], response_description="Retrieves health status of this application")
def health(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "OK" }
