from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserOut, UserCreate, UserBase, UserProfile
from sqlalchemy.orm import Session
from db import get_db
from models import User
from core.security import hash_password, verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/auth', tags=["Auth"])

@router.post('/register', response_model=UserOut)
def register_user(data:UserCreate , db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email==data.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    
    hashed_password = hash_password(data.password)
    new_user = User(username = data.username, hashed_password=hashed_password, email=data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login')
def register_user(data:OAuth2PasswordRequestForm=Depends() , db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email==data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong Password"
        )
    
    access_token = create_access_token(data={"sub":str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UserProfile)
def get_me(user: User = Depends(get_current_user)):
    return user