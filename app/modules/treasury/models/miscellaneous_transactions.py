# app/modules/treasury/models/miscellaneous_transactions.py

from datetime import datetime, timezone
from sqlalchemy import CheckConstraint, Column, Date, DateTime, Float, Integer, String, UniqueConstraint, Enum, func
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class FundCodeEnum(enum.Enum):
    CODE_100 = "100"
    CODE_200 = "200"
    CODE_300 = "300"

class PaymentModeEnum(enum.Enum):
    CASH = "Cash"
    CHECK = "Check"
    MONEY_ORDER = "Money Order"

class MiscellaneousTransaction(Base):
    __tablename__ = "miscellaneous_transactions"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    or_number = Column(String, index=True)
    payment_date = Column(Date)
    agency = Column(String, default="Municipality of Cardona")
    fund_code = Column(Enum(FundCodeEnum))
    payor_name = Column(String)
    total_amount = Column(Float)
    payment_mode = Column(Enum(PaymentModeEnum))
    drawee_bank = Column(String, nullable=True)
    payment_number = Column(String, nullable=True)
    txn_date = Column(Date, nullable=True)
    payors_money = Column(Float)
    change = Column(Float)
    remarks = Column(String, nullable=True)
    # status = Column(String)
    created_by = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)  # Automatically set created_at
    last_modified = Column(DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # creator = relationship("User", back_populates="individual_ctcs")
    # corporation_ctcs = relationship("CorporationCTC", back_populates="user")
    # miscellaneous_transactions = relationship("MiscellaneousTransaction", back_populates="user")
    # signatories = relationship("Signatory", back_populates="user")

    __table_args__ = (
        UniqueConstraint('or_number', name='uk_or_number'),
    )