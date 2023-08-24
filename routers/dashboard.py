
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


router.get("/general-situation")
def get_general_situation():
    pass

router.get("/affiliates")
def get_affiliates():
    pass

router.get("/natural-members")
def get_natural_members():
    pass