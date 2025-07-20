# Group B — Chat Room Management API with FastAPI & PostgreSQL

A RESTful API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** that supports chat room management, message exchange, and member handling.

---

## Features

- User and Room-based structure
- Send and retrieve messages in a room
- Add/remove users to/from chat rooms (Many-to-Many)
- Sample database seeding
- Database clearing functionality

---

## 📂 Project Structure

    Group-B  
    ├── main.py      # sample data entry intot eh database  
    ├── database.py  # DB connection + modelling database  
    ├── requirements.txt  # install required packages  

## Running the Application

1. Clone the repository  

        git clone https://github.com/your-username/Group-B.git  
        cd Group-B 

3. Setup virtual environment  

        python -m venv venv  
        source venv/bin/activate  # On Windows: venv\Scripts\activate  

4. Install required dependencies  

       pip install -r requirements.txt  

5. Configure PostgreSQL  

       DATABASE_URL = "postgresql://username:password@localhost/dbname"  

7. Run the server  

        python main.py
