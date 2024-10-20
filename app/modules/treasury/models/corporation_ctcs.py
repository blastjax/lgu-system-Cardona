# app/modules/treasury/models/corporation_ctcs.py

from datetime import datetime, timezone
from sqlalchemy import CheckConstraint, Column, Date, DateTime, Float, Integer, SmallInteger, String, ForeignKey, UniqueConstraint, Enum, func
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class OrganizationTypeEnum(enum.Enum):
    CORPORATION = "Corporation"
    ASSOCIATION = "Association"
    PARTNERSHIP = "Partnership"

class CorporationCTC(Base):
    __tablename__ = "corporation_ctcs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ctc_number = Column(String, index=True)
    year = Column(SmallInteger)
    place_of_issue = Column(String)
    date_issued = Column(DateTime(timezone=True))
    business_name = Column(String)
    tin = Column(Integer, nullable=True)
    business_address = Column(String)
    date_of_registration = Column(Date)
    organization_type = Column(Enum(OrganizationTypeEnum))
    place_of_incorporation = Column(String)
    nature_of_business = Column(String)
    basic_community_tax = Column(Float, default=500.00)
    taxable_assessed_value = Column(Float)
    taxable_gross = Column(Float)
    interest = Column(Float, default=0.00)
    # status = Column(String)
    created_by = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)  # Automatically set created_at
    last_modified = Column(DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # creator = relationship("User", back_populates="individual_ctcs")
    # corporation_ctcs = relationship("CorporationCTC", back_populates="user")
    # miscellaneous_transactions = relationship("MiscellaneousTransaction", back_populates="user")
    # signatories = relationship("Signatory", back_populates="user")

    __table_args__ = (
        UniqueConstraint('ctc_number', name='uk_corp_ctc_number'),
        CheckConstraint('year >= 1900 AND year <= 2999', name='ck_year'),
    )