# app/modules/user/schemas/department.py
from datetime import date, datetime, timezone
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.modules.treasury.models.individual_ctcs import GenderEnum, CivilStatusEnum

class IndividualCTCBase(BaseModel):
    ctc_number: str
    year: int
    place_of_issue: str
    date_issued: datetime
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    tin: Optional[int] = None
    address: str
    gender: GenderEnum
    citizenship: str
    civil_status: CivilStatusEnum
    icr_number: Optional[str] = None
    date_of_birth: date
    place_of_birth: str
    height_cm: Optional[int] = None
    weight_kg: Optional[float] = None
    occupation: Optional[str] = None
    basic_community_tax: float = 5.00
    taxable_gross: float
    taxable_salary: float
    taxable_income: float
    interest: float = 0.00

class IndividualCTCCreate(IndividualCTCBase):
    created_by: int
    # created_at: datetime
    # last_modified: datetime
    # created_at: Optional[datetime] = datetime.now(timezone.utc)
    # last_modified: Optional[datetime] = datetime.now(timezone.utc)

class IndividualCTCUpdate(IndividualCTCBase):
    ctc_number: Optional[str] = None
    year: Optional[int] = None
    place_of_issue: Optional[str] = None
    date_issued: Optional[datetime] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    tin: Optional[int] = None
    address: Optional[str] = None
    gender: Optional[GenderEnum] = None
    citizenship: Optional[str] = None
    civil_status: Optional[CivilStatusEnum] = None
    icr_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    place_of_birth: Optional[str] = None
    height_cm: Optional[int] = None
    weight_kg: Optional[float] = None
    occupation: Optional[str] = None
    basic_community_tax: Optional[float] = 5.00
    taxable_gross: Optional[float] = None
    taxable_salary: Optional[float] = None
    taxable_income: Optional[float] = None
    interest: Optional[float] = 0.00
    # last_modified: Optional[datetime] = datetime.now(timezone.utc)

class IndividualCTCResponse(IndividualCTCBase):
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