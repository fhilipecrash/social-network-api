from fastapi import FastAPI, APIRouter
from api.routers import users, posts

app = FastAPI(
    docs_url="/api/docs",
    title="Mini Social Media API",
    description="An example of a mini social media API",
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

prefix_router = APIRouter(prefix="/api")

prefix_router.include_router(users.router)
prefix_router.include_router(posts.router)

app.include_router(prefix_router)
