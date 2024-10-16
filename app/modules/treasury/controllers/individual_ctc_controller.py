# app/modules/treasury/controllers/individual_ctc_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.treasury.models.individual_ctcs import IndividualCTC
from app.modules.treasury.schemas.individual_ctc import IndividualCTCCreate, IndividualCTCResponse, IndividualCTCUpdate
from app.utils.response_helper import success_response, error_response, handle_error
from app.utils.helpers import create, serialize_params, update

router = APIRouter()

@router.get("/", response_model=list[IndividualCTCResponse])
def get_all_individual_ctcs(db: Session = Depends(get_db)):
    try:
        ctcs = db.query(IndividualCTC).all()
        return success_response(
            message="Individual CTCs retrieved successfully",
            data=[serialize_params(IndividualCTCResponse.model_validate(individual_ctc).model_dump()) for individual_ctc in ctcs]
        )
    except Exception as e:
        return handle_error(e, IndividualCTC)

@router.get("/{id}", response_model=IndividualCTCResponse)
def get_individual_ctc_by_id(id: int, db: Session = Depends(get_db)):
    try:
        individual_ctc = db.query(IndividualCTC).filter(IndividualCTC.id == id).first()
        if not individual_ctc:
            return error_response(error=f"Individual CTC with id {id} not found", status_code=404)

        return success_response(
            message="Individual CTC retrieved successfully",
            data=serialize_params(IndividualCTCResponse.model_validate(individual_ctc).model_dump())
        )
    except Exception as e:
        return handle_error(e, IndividualCTC)

@router.post("/", response_model=IndividualCTCResponse, status_code=201)
def create_individual_ctc(individual_ctc: IndividualCTCCreate, db: Session = Depends(get_db)):
    try:
        db_individual_ctc = create(db, IndividualCTC, individual_ctc)
        response_data = IndividualCTCResponse.model_validate(db_individual_ctc).model_dump()
        return success_response(
            message="Individual CTC created successfully",
            data=serialize_params(response_data)
        )
    except Exception as e:
        return handle_error(e, IndividualCTC)

@router.put("/{id}", response_model=IndividualCTCResponse)
def update_individual_ctc(id: int, individual_ctc: IndividualCTCUpdate, db: Session = Depends(get_db)):
    try:
        db_individual_ctc = update(db, IndividualCTC, id, individual_ctc)
        if not db_individual_ctc:
            return error_response(error=f"Individual CTC with id {id} not found", status_code=404)
        return success_response(
            message="Individual CTC updated successfully",
            data=serialize_params(IndividualCTCResponse.model_validate(db_individual_ctc).model_dump())
        )
    except Exception as e:
        return handle_error(e, IndividualCTC)

@router.delete("/{id}", status_code=204)
def delete_individual_ctc(id: int, db: Session = Depends(get_db)):
    db_individual_ctc = db.query(IndividualCTC).filter(IndividualCTC.id == id).first()
    if not db_individual_ctc:
        return error_response(error=f"Individual CTC with id {id} not found", status_code=404)
    db.delete(db_individual_ctc)
    db.commit()
    return success_response(message="Individual CTC deleted")
