from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql.functions import func
from database.db import SessionLocal, engine, Base
from database.models import Users
from database.schemes import UserCreateForm
from datetime import datetime
from typing import List, Union
import time
from functools import wraps

def get_user_by_username(username: str):

    with SessionLocal() as session:
        try:
            user = session.query(Users).filter(Users.username == username).first()
            if not user:
                return None
            return user
        except Exception as e:
            print(e)
            return None

def create_user(user: UserCreateForm):

    with SessionLocal() as session:

        try:

            NewUser = Users(**user.dict())
            session.add(NewUser)
            session.commit()
            session.refresh(NewUser)

            return NewUser
        except Exception as e:
            print(e)
            return None


def profiler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

# SELECT
#     SUM("CountDeposit") AS "CountDeposit",
#     SUM("SumDepositAmount") AS "SumDepositAmount",
#     SUM("WithdrawalCount") AS "WithdrawalCount",
#     SUM("WithdrawalAmount") AS "WithdrawalAmount",
#     SUM("NetDepositAmount") AS "NetDepositAmount",
#     SUM("CountTotalBalance") AS "CountTotalBalance",
#     SUM("SumTotalBalance") AS "SumTotalBalance",
#     SUM("SumSportTotalBetAmount") AS "SumSportTotalBetAmount",
#     SUM("SumSportRealMoneyWonAmount") AS "SumSportRealMoneyWonAmount",
#     SUM("SportsBookInvoice") AS "SportsBookInvoice",
#     SUM("SumCasinoTotalBetAmount") AS "SumCasinoTotalBetAmount",
#     SUM("SumCasinoRealMoneyWonAmount") AS "SumCasinoRealMoneyWonAmount",
#     SUM("CasinoInvoice") AS "CasinoInvoice",
#     SUM("PaymentCommission") AS "PaymentCommission",
#     SUM("AffiliateCommission") AS "AffiliateCommission",
#     SUM("ProviderCommission") AS "ProviderCommission",
#     SUM("TotalInvoice") AS "TotalInvoice"
# FROM
#     public."GeneralSituationDashboard"
# WHERE
#     "Date" >= '2023-08-18' AND "Date" <= '2023-08-24';

@profiler
def get_sum(table, columns: list[str], start_date: datetime, end_date: datetime) -> dict:
    with SessionLocal() as session:
        try:
            # Dynamically build the aggregation part of the query
            aggregation_functions = [func.sum(getattr(table, col)).label(col) for col in columns]

            results = session.query(*aggregation_functions).filter(
                table.Date >= start_date,
                table.Date <= end_date
            ).one()  # Using one() to retrieve a single result directly

            # Map results to column names
            return {column: getattr(results, column) for column in columns}

        except Exception as e:
            raise e
