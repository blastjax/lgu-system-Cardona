# app/modules/user/schemas/corporation_ctc.py
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from app.modules.treasury.models.corporation_ctcs import OrganizationTypeEnum

class CorporationCTCBase(BaseModel):
    ctc_number: str
    year: int
    place_of_issue: str
    date_issued: datetime
    business_name: str
    tin: Optional[int] = None
    business_address: str
    date_of_registration: date
    organization_type: OrganizationTypeEnum
    place_of_incorporation: str
    nature_of_business: str
    basic_community_tax: float = 500.00
    taxable_assessed_value: float
    taxable_gross: float
    interest: float = 0.00

class CorporationCTCCreate(CorporationCTCBase):
    created_by: int
    # created_at: datetime
    # last_modified: datetime
    # created_at: Optional[datetime] = datetime.now(timezone.utc)
    # last_modified: Optional[datetime] = datetime.now(timezone.utc)

class CorporationCTCUpdate(CorporationCTCBase):
    ctc_number: Optional[str] = None
    year: Optional[int] = None
    place_of_issue: Optional[str] = None
    date_issued: Optional[datetime] = None
    business_name: Optional[str] = None
    tin: Optional[int] = None
    business_address: Optional[str] = None
    date_of_registration: Optional[date] = None
    organization_type: Optional[OrganizationTypeEnum] = None
    place_of_incorporation: Optional[str] = None
    nature_of_business: Optional[str] = None
    basic_community_tax: Optional[float] = 500.00
    taxable_assessed_value: Optional[float] = None
    taxable_gross: Optional[float] = None
    interest: Optional[float] = 0.00
    # last_modified: Optional[datetime] = datetime.now(timezone.utc)

class CorporationCTCResponse(CorporationCTCBase):
    id: int
    created_by: int
    created_at: datetime
    last_modified: datetime

    model_config = {
        'from_attributes': True,  # Enables attribute-based validation in Pydantic v2
        "use_enum_values": True,
        'json_encoders': {
            datetime: lambda v: v.isoformat(),  # Serialize datetime to ISO format
            date: lambda v: v.isoformat()  # Serialize date to ISO format
        }
    }