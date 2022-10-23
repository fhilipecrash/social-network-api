from fastapi import FastAPI, Depends, Request
from api.routers import users_router, posts_router
from fastapi.security import OAuth2PasswordBearer

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. Create, read, update, delete.",
    },
    {
        "name": "posts",
        "description": "Operations with posts. Create, read, update, delete.",
    }
]

app = FastAPI(
    root_path="/api/v1",
    openapi_tags=tags_metadata,
    title="Social Network API",
    description="An example of a mini social network API",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Fhilipe Coelho",
        "url": "https://github.com/fhilipecrash",
        "email": "fhilipecoelho.dev@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(users_router)
app.include_router(posts_router)


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}
