from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

# User schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    email:str
    password: str

class EventType(str, Enum):
    hackathon = "hackathon"
    coding_contest = "coding contest"
    competition = "competition"

class EventBase(BaseModel):
    title: str
    description: str | None = None
    start_datetime: datetime
    end_datetime: datetime
    location: str
    typeof: EventType   # 👈 automatic validation
    rules: str

class EventOut(EventBase):
    id:int

class RegistrationOut(BaseModel):
    id: int
    user: UserBase
    
class UserEvent(UserBase):
    id:int

class EventOutThis(EventOut):
    creator:UserEvent
    registrations: list[RegistrationOut]

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    location: Optional[str] = None
    typeof: Optional[str] = None
    rules: Optional[str] = None

class UserOut(BaseModel):
    id:int
    username:str
    events_created: list[EventBase] = []
    events: list[EventBase] = []

class UserProfile(UserOut):
    email:str

class ResReturn(BaseModel):
    user:UserBase
    event:EventBase