from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserOut, UserCreate, UserBase, EventBase, EventUpdate, EventOut, EventOutThis
from sqlalchemy.orm import Session
from db import get_db
from models import User, Event
from core.security import hash_password, verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional
from fastapi import Query
from datetime import datetime

router = APIRouter(prefix='/event', tags=['Event'])

@router.post('/create', response_model=EventOut)
def create_event(
    data: EventBase, 
    db: Session = Depends(get_db), 
    user: User = Depends(get_current_user)
):
    allowed_types = {"hackathon", "coding contest", "competition"}

    if data.typeof not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid event type. Allowed: {', '.join(allowed_types)}"
        )

    event = db.query(Event).filter(
        Event.title == data.title,
        Event.description == data.description
    ).first()

    if event:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Event already exists"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized"
        )

    event = Event(
        title=data.title,
        description=data.description,
        start_datetime=data.start_datetime,
        end_datetime=data.end_datetime,
        location=data.location,
        creator_id=user.id,
        typeof=data.typeof,
        rules=data.rules
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/all", response_model=list[EventOut])
def get_all_events(
    db: Session = Depends(get_db),
    location: Optional[str] = None,
    typeof: Optional[str] = Query(None, description="hackathon | coding contest | competition"),
):
    query = db.query(Event)

    if location is not None:
        query = query.filter(Event.location.ilike(f"%{location}%"))

    if typeof is not None:
        query = query.filter(Event.typeof.ilike(typeof))

    events = query.order_by(Event.start_datetime.asc()).all()
    return events


@router.get('/this', response_model=EventOutThis)
def get_event(id:int, db:Session=Depends(get_db)):
    event = db.query(Event).filter(Event.id==id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Event not found"
        )
    
    return event

@router.get("/current", response_model=list[EventOut])
def get_current_events(db: Session = Depends(get_db)):
    now = datetime.now()
    events = (
        db.query(Event)
        .filter(Event.start_datetime <= now, Event.end_datetime >= now)
        .order_by(Event.start_datetime.asc())
        .all()
    )
    return events


@router.get("/past", response_model=list[EventOut])
def get_past_events(db: Session = Depends(get_db)):
    now = datetime.now()
    events = (
        db.query(Event)
        .filter(Event.end_datetime < now)
        .order_by(Event.end_datetime.desc()) 
        .all()
    )
    return events

@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    if event.creator_id != user.id:  # only creator can delete
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this event"
        )
    
    db.delete(event)   # cascade kicks in here
    db.commit()
    return {"detail": "Event and its registrations deleted successfully"}

@router.patch("/edit/{event_id}")
def edit_event(
    event_id: int,
    event_update: EventUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(Event.id == event_id).first()
    
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    if event.creator_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to edit this event"
        )
    
    # apply only provided fields
    update_data = event_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(event, key, value)
    
    db.commit()
    db.refresh(event)
    return {"detail": "Event updated successfully", "event": event}
