# app/modules/user/schemas/miscellaneous_transaction.py
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from app.modules.treasury.models.miscellaneous_transactions import FundCodeEnum, PaymentModeEnum

class MiscellaneousTransactionBase(BaseModel):
    or_number: str
    payment_date: date
    agency: str = "Municipality of Cardona"
    fund_code: FundCodeEnum
    payor_name: str
    total_amount: float
    payment_mode: PaymentModeEnum
    drawee_bank: Optional[str] = None
    payment_number: Optional[str] = None
    txn_date: Optional[date] = None
    payors_money: float
    change: float
    remarks: Optional[str] = None

class MiscellaneousTransactionCreate(MiscellaneousTransactionBase):
    created_by: int
    # created_at: datetime
    # last_modified: datetime
    # created_at: Optional[datetime] = datetime.now(timezone.utc)
    # last_modified: Optional[datetime] = datetime.now(timezone.utc)

class MiscellaneousTransactionUpdate(MiscellaneousTransactionBase):
    or_number: Optional[str] = None
    payment_date: Optional[date] = None
    agency: Optional[str] = "Municipality of Cardona"
    fund_code: Optional[FundCodeEnum] = None
    payor_name: Optional[str] = None
    total_amount: Optional[float] = None
    payment_mode: Optional[PaymentModeEnum] = None
    drawee_bank: Optional[str] = None
    payment_number: Optional[str] = None
    txn_date: Optional[date] = None
    payors_money: Optional[float] = None
    change: Optional[float] = None
    remarks: Optional[str] = None
    # last_modified: Optional[datetime] = datetime.now(timezone.utc)

class MiscellaneousTransactionResponse(MiscellaneousTransactionBase):
    id: int
    created_by: int
    created_at: datetime
    last_modified: datetime

    model_config = {
        'from_attributes': True,  # Enables attribute-based validation in Pydantic v2
        "use_enum_values": True,
        'json_encoders': {
            datetime: lambda v: v.isoformat(),  # Serialize datetime to ISO format
        }
    }