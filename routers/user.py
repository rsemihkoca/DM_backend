from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from database.schemes import UserCreateForm, UserOut, User
from database import crud
from lib.oauth2 import get_password_hash, get_current_active_user
from typing import List, Annotated

router = APIRouter( prefix="/users", tags=["Users"])


# Create a new user
@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_users(request: Request, user: Annotated[UserCreateForm, Depends()], current_user: Annotated[User, Depends(get_current_active_user)]):

    #check if user already exists
    result = crud.get_user_by_username(user.username)
    if result:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    NewUser = crud.create_user(user)

    if NewUser is None:
        raise HTTPException(status_code=400, detail="User already exists")

    return NewUser


