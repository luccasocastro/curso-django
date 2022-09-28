from fastapi import FastAPI
from typing import List
from uuid import uuid4
from models import Roles, User, Gender

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name='Luccas',
        last_name='Souza', 
        gender=Gender.male, 
        roles=[Roles.admin]
        ),
    User(
        id=uuid4(),
        first_name='Nicolly',
        last_name='Cristina', 
        gender=Gender.female, 
        roles=[Roles.admin, Roles.student]
        )
]

@app.get("/")
def root():
    return {'message':'Hello Wolrd!'}

@app.get("/api/v1/users")
def fetch_users():
    return db;

@app.post("/api/v1/users")
def register_user(user: User):
    db.append(user)
    return {"id": user.id}
    