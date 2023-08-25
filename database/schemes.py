from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Union, Annotated
from fastapi.param_functions import Form



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserCreateForm:

    def __init__(
        self,
        full_name: Annotated[str, Form()],
        username: Annotated[str, Form()],
        email: Annotated[EmailStr, Form()],
        password: Annotated[str, Form()]
    ):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password

    def dict(self):
        return {
            "full_name": self.full_name,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

class UserOut(BaseModel):
    id: int
    created_at: datetime
    email: EmailStr

    class Config:
        from_attributes = True

class ApiRequest(BaseModel):
    start_date: str
    end_date: str

class ApiResponse(BaseModel):
    CountDeposit: float
    SumDepositAmount: float
    WithdrawalCount: float
    WithdrawalAmount: float
    NetDepositAmount: float
    CountTotalBalance: float
    SumTotalBalance: float
    SumSportTotalBetAmount: float
    SumSportRealMoneyWonAmount: float
    SportsBookInvoice: float
    SumCasinoTotalBetAmount: float
    SumCasinoRealMoneyWonAmount: float
    CasinoInvoice: float
    PaymentCommission: float
    AffiliateCommission: float
    ProviderCommission: float
    TotalInvoice: float