# app/modules/treasury/controllers/miscellaneous_transaction_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.treasury.models.miscellaneous_transactions import MiscellaneousTransaction
from app.modules.treasury.schemas.miscellaneous_transaction import MiscellaneousTransactionCreate, MiscellaneousTransactionResponse, MiscellaneousTransactionUpdate
from app.utils.response_helper import success_response, error_response, handle_error
from app.utils.helpers import create, serialize_params, update

router = APIRouter()

@router.get("/", response_model=list[MiscellaneousTransactionResponse])
def get_all_miscellaneous_transactions(db: Session = Depends(get_db)):
    try:
        ctcs = db.query(MiscellaneousTransaction).all()
        return success_response(
            message="Miscellaneous Transactions retrieved successfully",
            data=[serialize_params(MiscellaneousTransactionResponse.model_validate(miscellaneous_transaction).model_dump()) for miscellaneous_transaction in ctcs]
        )
    except Exception as e:
        return handle_error(e, MiscellaneousTransaction)

@router.get("/{id}", response_model=MiscellaneousTransactionResponse)
def get_miscellaneous_transaction_by_id(id: int, db: Session = Depends(get_db)):
    try:
        miscellaneous_transaction = db.query(MiscellaneousTransaction).filter(MiscellaneousTransaction.id == id).first()
        if not miscellaneous_transaction:
            return error_response(error=f"Miscellaneous Transaction with id {id} not found", status_code=404)

        return success_response(
            message="Miscellaneous Transaction retrieved successfully",
            data=serialize_params(MiscellaneousTransactionResponse.model_validate(miscellaneous_transaction).model_dump())
        )
    except Exception as e:
        return handle_error(e, MiscellaneousTransaction)

@router.post("/", response_model=MiscellaneousTransactionResponse, status_code=201)
def create_miscellaneous_transaction(miscellaneous_transaction: MiscellaneousTransactionCreate, db: Session = Depends(get_db)):
    try:
        db_miscellaneous_transaction = create(db, MiscellaneousTransaction, miscellaneous_transaction)
        response_data = MiscellaneousTransactionResponse.model_validate(db_miscellaneous_transaction).model_dump()
        return success_response(
            message="Miscellaneous Transaction created successfully",
            data=serialize_params(response_data)
        )
    except Exception as e:
        return handle_error(e, MiscellaneousTransaction)

@router.put("/{id}", response_model=MiscellaneousTransactionResponse)
def update_miscellaneous_transaction(id: int, miscellaneous_transaction: MiscellaneousTransactionUpdate, db: Session = Depends(get_db)):
    try:
        db_miscellaneous_transaction = update(db, MiscellaneousTransaction, id, miscellaneous_transaction)
        if not db_miscellaneous_transaction:
            return error_response(error=f"Miscellaneous Transaction with id {id} not found", status_code=404)
        return success_response(
            message="Miscellaneous Transaction updated successfully",
            data=serialize_params(MiscellaneousTransactionResponse.model_validate(db_miscellaneous_transaction).model_dump())
        )
    except Exception as e:
        return handle_error(e, MiscellaneousTransaction)

@router.delete("/{id}", status_code=204)
def delete_miscellaneous_transaction(id: int, db: Session = Depends(get_db)):
    db_miscellaneous_transaction = db.query(MiscellaneousTransaction).filter(MiscellaneousTransaction.id == id).first()
    if not db_miscellaneous_transaction:
        return error_response(error=f"Miscellaneous Transaction with id {id} not found", status_code=404)
    db.delete(db_miscellaneous_transaction)
    db.commit()
    return success_response(message="Miscellaneous Transaction deleted")
