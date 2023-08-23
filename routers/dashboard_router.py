from fastapi import FastAPI
import time
from . import models
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, get_db, table_exists
from .routers import post, user, auth, vote
from .configs import settings


models.Base.metadata.create_all(bind=engine) instead of sqlalchemy alembic does this

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


#Main route
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response