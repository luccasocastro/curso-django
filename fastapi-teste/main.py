from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from models import Roles, User, Gender, UserUpdateRequest

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
async def root():
    return {'message':'Hello Wolrd!'}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def remove_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exists'
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id:UUID, user_update:UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exists'
    )