# from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
# from sqlalchemy.orm import Session
# from typing import List
# from database.schemes import UserOut, UserCreate
#
# router = APIRouter( prefix="/users", tags=["Users"])
#
#
# # Create a new user
# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
# async def create_users(user: UserCreate, db: Session = Depends(database.get_db)):
#
#     hashed_password = utils.hash_password(user.password)
#     user.password = hashed_password
#     NewUser = models.User(**user.dict())
#     db.add(NewUser)
#     db.commit()
#     db.refresh(NewUser)
#
#     return NewUser
#
#
