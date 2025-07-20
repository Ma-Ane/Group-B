# for database integration
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# import custom
from database import Base
from database import User, Room, Message, room_members 

# database declaration
DATABASE_URL = "postgresql://postgres:AnTIquE$$5@localhost:5432/sample_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

session = SessionLocal()


#sample example function
def sample_example():
    # create users for examples only and contains basic implementation
    # I haved used a simple example implementation with a random password and values which are supposed to be securely stored in the database
    user1 = User(user_id=1, username="John", hashed_pass='AdFi7h76nD', dob=datetime(2000, 7, 19, 15, 30), date_created=datetime(2020, 2, 10, 2, 20))
    user2 = User(user_id=2, username="Bob", hashed_pass='AdFi7h76nD', dob=datetime(2007, 1, 1, 20, 4), date_created=datetime(2020, 2, 10, 2 , 20))

    # create room
    room = Room(description='General room', no_of_messages=0, participants=[])

    # Add users to the room (many-to-many)
    room.members.append(user1)
    room.members.append(user2)

    # send a message
    msg = Message(text="Hello, everyone!", sender=user1, room=room)

    # add all the data in the database
    session.add_all([user1, user2, room, msg])
    session.commit()

    print("Sample data added successfully.")


# fetch data from the db
def fetch_data():
    # Fetch all messages in the room
    room_db = session.query(Room).filter_by(description="General room").first()
    if room_db:
        for msg in room_db.messages:
            print(f"{msg.sender.username} said: {msg.text}")
    else:
        print("Room named 'general' not found in the database.")



# clear db before starting test
def clear_db():
    # Clear the association table first
    session.execute(text('DELETE FROM room_members'))

    # Then clear child tables
    session.query(Message).delete()

    # Then parent tables
    session.query(Room).delete()
    session.query(User).delete()

    session.commit()
    print("Database cleared successfully.")



if __name__ == '__main__':
    clear_db()
    sample_example()
    fetch_data()

