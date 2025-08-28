from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Registrations
    events = relationship("Registration", back_populates="user", cascade="all, delete-orphan")
    
    # Events created by the user
    events_created = relationship("Event", back_populates="creator", cascade="all, delete-orphan")


class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    typeof = Column(String, nullable=False)
    rules = Column(String, nullable=False)
    
    creator_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))

    creator = relationship("User", back_populates="events_created")
    registrations = relationship(
        "Registration",
        back_populates="event",
        cascade="all, delete-orphan"
    )


class Registration(Base):
    __tablename__ = 'registrations'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    event_id = Column(Integer, ForeignKey('events.id', ondelete="CASCADE"))
    timestamp = Column(
        DateTime, 
        nullable=False, 
        default=datetime.utcnow,          # Python-side default
        server_default=func.now()         # DB-side default
    )
    
    user = relationship("User", back_populates="events")
    event = relationship("Event", back_populates="registrations")
