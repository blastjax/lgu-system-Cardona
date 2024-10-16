# app/modules/treasury/models/individual_ctcs.py

from datetime import datetime, timezone
from sqlalchemy import CheckConstraint, Column, Date, DateTime, Float, Integer, SmallInteger, String, ForeignKey, UniqueConstraint, Enum, func
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class GenderEnum(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"

class CivilStatusEnum(enum.Enum):
    SINGLE = "Single"
    MARRIED = "Married"
    WIDOWED = "Widowed"
    LEGALLY_SEPARATED = "Legally Separated"

class IndividualCTC(Base):
    __tablename__ = "individual_ctcs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ctc_number = Column(String, index=True)
    year = Column(SmallInteger)
    place_of_issue = Column(String)
    date_issued = Column(DateTime(timezone=True))
    last_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String, nullable=True)
    tin = Column(Integer, nullable=True)
    address = Column(String)
    gender = Column(Enum(GenderEnum))
    citizenship = Column(String)
    civil_status = Column(Enum(CivilStatusEnum))
    icr_number = Column(String, nullable=True)
    date_of_birth = Column(Date)
    place_of_birth = Column(String)
    height_cm = Column(SmallInteger, nullable=True)
    weight_kg = Column(Float, nullable=True)
    occupation = Column(String, nullable=True)
    basic_community_tax = Column(Float, default=5.00)
    taxable_gross = Column(Float)
    taxable_salary = Column(Float)
    taxable_income = Column(Float)
    interest = Column(Float, default=0.00)
    created_by = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)  # Automatically set created_at
    last_modified = Column(DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # creator = relationship("User", back_populates="individual_ctcs")
    # corporation_ctcs = relationship("CorporationCTC", back_populates="user")
    # miscellaneous_transactions = relationship("MiscellaneousTransaction", back_populates="user")
    # signatories = relationship("Signatory", back_populates="user")

    __table_args__ = (
        UniqueConstraint('ctc_number', name='uk_ctc_number'),
        CheckConstraint('year >= 1900 AND year <= 2999', name='ck_year'),
    )