
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


router.get("/general-situation")
async def get_general_situation(request: Request):
    pass

router.get("/affiliates")
async def get_affiliates(request: Request):
    pass

router.get("/natural-members")
async def get_natural_members(request: Request):
    pass