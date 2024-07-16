from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth


# creating database tables, not required if using alembic does not cause code break
# models.Base.metadata.create_all(bind=database.engine)
# fastapi instance
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

""" API Routes """
@app.get("/")
async def root():
    return {"message": "Hello World"}
