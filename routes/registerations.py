from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserOut, UserCreate, UserBase, UserProfile, ResReturn
from sqlalchemy.orm import Session
from db import get_db
from models import User, Event, Registration
from core.security import hash_password, verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/registrations', tags=["Resistrations"])

@router.post('/register', response_model=ResReturn)
def register(id:int, user: User = Depends(get_current_user), db:Session=Depends(get_db)):
    event = db.query(Event).filter(Event.id==id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Event Not found"
        )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User Not found"
        )
    
    res = Registration(user_id=user.id, event_id=event.id)
    db.add(res)
    db.commit()
    db.refresh(res)
    return res

@router.delete("/unregister/{event_id}", status_code=204)
def unregister_event(event_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    registration = db.query(Registration).filter(
        Registration.event_id == event_id,
        Registration.user_id == user.id
    ).first()
    
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="You are not registered for this event"
        )
    
    db.delete(registration)
    db.commit()
    return {"detail": "Unregistered from event successfully"}