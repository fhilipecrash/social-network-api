from fastapi import FastAPI
from api.routers import users, posts

app = FastAPI(
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

app.include_router(users.router)
app.include_router(posts.router)
