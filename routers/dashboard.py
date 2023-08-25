
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from lib.oauth2 import get_current_active_user
from database.schemes import UserOut, ApiRequest, ApiResponse
from database import crud
from database.models import GeneralSituationDashboard, AffiliateDashboard, NaturalMembersDashboard, Users

from routers.validators.dashboard import check_date_format, validate_date_order
from routers.operators.dashboard import remove_date_columns
router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/general-situation", dependencies=[Depends(get_current_active_user)], response_model=ApiResponse)
async def get_general_situation(request: Request, dates: ApiRequest):
    table = GeneralSituationDashboard

    # Check date format
    start_date_obj, end_date_obj = check_date_format(dates.start_date, dates.end_date)

    # Check if start_date > end_date
    assert validate_date_order(start_date_obj, end_date_obj) is True

    columns = remove_date_columns(table.get_column_names())

    try:
        result = crud.get_sum(table, columns, start_date_obj, end_date_obj)

        if result is None:
            raise HTTPException(status_code=404, detail="Sum not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return result

@router.get("/affiliates", dependencies=[Depends(get_current_active_user)], response_model=ApiResponse)
async def get_affiliates(request: Request, dates: ApiRequest):
    table = AffiliateDashboard

    # Check date format
    start_date_obj, end_date_obj = check_date_format(dates.start_date, dates.end_date)

    # Check if start_date > end_date
    assert validate_date_order(start_date_obj, end_date_obj) is True

    columns = remove_date_columns(table.get_column_names())

    try:
        result = crud.get_sum(table, columns, start_date_obj, end_date_obj)

        if result is None:
            raise HTTPException(status_code=404, detail="Sum not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return result

@router.get("/natural-members", dependencies=[Depends(get_current_active_user)], response_model=ApiResponse)
async def get_natural_members(request: Request, dates: ApiRequest):
    table = NaturalMembersDashboard

    # Check date format
    start_date_obj, end_date_obj = check_date_format(dates.start_date, dates.end_date)

    # Check if start_date > end_date
    assert validate_date_order(start_date_obj, end_date_obj) is True

    columns = remove_date_columns(table.get_column_names())

    try:
        result = crud.get_sum(table, columns, start_date_obj, end_date_obj)

        if result is None:
            raise HTTPException(status_code=404, detail="Sum not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return result