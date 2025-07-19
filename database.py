# task is to create various models in SQLAlchemy for ORM-based interaction with PostgreSQL
# we have three models named User, Room and Message
# for User, we have user_id, username, hashed_pass, role, dob, date_created
# for Room, we have room_id, description, no_of_messages, date_created, participants
# for Message, we have message_id, text, date, 
# we have to define various relationships between the models 


# for realtions we have,
# for a user can send many message but a message can only be sent by a user (user(1) ------> message(many))
# for a room can have many message but a message can only be in a room  (room(1) ------> message(many))
# for a room can have multiple user and a user can be involved in multiple room  (room(many) ------> user(many))


# import all the necessary libraries
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine, Table, JSON      # JSON for list
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# define a base class which all the models will inherit 
Base = declarative_base()

# handle many to many relationship
room_members = Table(
    'room_members',
    Base.metadata,
    Column('user_id', ForeignKey('user.user_id'), primary_key=True),
    Column('room_id', ForeignKey('room.room_id'), primary_key=True)
)


# user table 
class User(Base):
    __tablename__ = 'user'      # name of the table

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_pass = Column(String, nullable=False)
    role = Column(String, nullable=False, default='user')
    dob = Column(DateTime, nullable=True)
    date_created = Column(DateTime, default=datetime.utcnow)

    # one to many realtion ==> user --> message
    messages = relationship('Message', back_populates='sender')

    # many to many ==> user --> room
    rooms = relationship('Room', back_populates='members', secondary=room_members)


# message table
class Message(Base):
    __tablename__ = 'message'

    message_id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    # Foreign keys
    sender_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    room_id = Column(Integer, ForeignKey('room.room_id'), nullable=False)

    # back references
    sender = relationship('User', back_populates='messages')
    room = relationship('Room', back_populates='messages')


# room table
class Room(Base):
    __tablename__ = 'room'

    room_id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=True)
    no_of_messages = Column(Integer)
    date_created = Column(DateTime, default=datetime.utcnow)
    participants = Column(JSON)

    # one to many ==> Room --> Message
    messages = relationship('Message', back_populates='room')

    # many to many ==> Room --> User
    members = relationship('User', back_populates='rooms', secondary=room_members, cascade="all, delete")
