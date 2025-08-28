from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserOut, UserCreate, UserBase, EventBase
from sqlalchemy.orm import Session
from db import get_db
from models import User, Event
from core.security import hash_password, verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/user', tags=['User'])

@router.get('/profile', response_model=UserOut)
def create_event(id:int, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User do not exists"
        )
    return user