from datetime import datetime
from fastapi import HTTPException


def check_date_format(start_date: str, end_date: str) -> tuple:
    try:
        start_date_obj = datetime.strptime(start_date, '%d-%m-%y')
        end_date_obj = datetime.strptime(end_date, '%d-%m-%y')
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Expected format: '%d-%m-%y'")
    else:
        return start_date_obj, end_date_obj


def validate_date_order(start_date_obj: datetime, end_date_obj: datetime) -> bool:
    # Check if start_date > end_date
    if start_date_obj > end_date_obj:
        raise HTTPException(status_code=400, detail="start_date should not be greater than end_date")
    else:
        return True
