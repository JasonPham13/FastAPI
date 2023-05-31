from fastapi import FastAPI, Response, status

app = FastAPI(
    title="Jason's-FastAPI",
    description="This is the swagger spec for my FastApi",
    version='1.0.0'
)




@app.get("/", tags=['welcome'], response_description="Displays welcome message")
async def welcome(response: Response):
        response.status_code = status.HTTP_200_OK
        return {"message":  "Hello, welcome to Jason's API"}
