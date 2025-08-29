from fastapi import FastAPI
from models import Base
from db import engine
from routes.auth import router as auth_router
from routes.event import router as event_router
from routes.user import router as user_router
from routes.registerations import router as res_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

allowed_origins = [
    "https://juevents.web.app",  # your deployed frontend
    "http://localhost:5173",     # if testing locally with Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # only allow these origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(event_router)
app.include_router(user_router)
app.include_router(res_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}