from fastapi import FastAPI
from models import Base
from db import engine
from routes.auth import router as auth_router
from routes.event import router as event_router
from routes.user import router as user_router
from routes.registerations import router as res_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth_router)
app.include_router(event_router)
app.include_router(user_router)
app.include_router(res_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}