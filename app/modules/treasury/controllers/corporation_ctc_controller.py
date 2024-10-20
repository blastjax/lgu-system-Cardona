# app/modules/treasury/controllers/corporation_ctc_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.treasury.models.corporation_ctcs import CorporationCTC
from app.modules.treasury.schemas.corporation_ctc import CorporationCTCCreate, CorporationCTCResponse, CorporationCTCUpdate
from app.utils.response_helper import success_response, error_response, handle_error
from app.utils.helpers import create, serialize_params, update

router = APIRouter()

@router.get("/", response_model=list[CorporationCTCResponse])
def get_all_corporation_ctcs(db: Session = Depends(get_db)):
    try:
        ctcs = db.query(CorporationCTC).all()
        return success_response(
            message="Corporation CTCs retrieved successfully",
            data=[serialize_params(CorporationCTCResponse.model_validate(corporation_ctc).model_dump()) for corporation_ctc in ctcs]
        )
    except Exception as e:
        return handle_error(e, CorporationCTC)

@router.get("/{id}", response_model=CorporationCTCResponse)
def get_corporation_ctc_by_id(id: int, db: Session = Depends(get_db)):
    try:
        corporation_ctc = db.query(CorporationCTC).filter(CorporationCTC.id == id).first()
        if not corporation_ctc:
            return error_response(error=f"Corporation CTC with id {id} not found", status_code=404)

        return success_response(
            message="Corporation CTC retrieved successfully",
            data=serialize_params(CorporationCTCResponse.model_validate(corporation_ctc).model_dump())
        )
    except Exception as e:
        return handle_error(e, CorporationCTC)

@router.post("/", response_model=CorporationCTCResponse, status_code=201)
def create_corporation_ctc(corporation_ctc: CorporationCTCCreate, db: Session = Depends(get_db)):
    try:
        db_corporation_ctc = create(db, CorporationCTC, corporation_ctc)
        response_data = CorporationCTCResponse.model_validate(db_corporation_ctc).model_dump()
        return success_response(
            message="Corporation CTC created successfully",
            data=serialize_params(response_data)
        )
    except Exception as e:
        return handle_error(e, CorporationCTC)

@router.put("/{id}", response_model=CorporationCTCResponse)
def update_corporation_ctc(id: int, corporation_ctc: CorporationCTCUpdate, db: Session = Depends(get_db)):
    try:
        db_corporation_ctc = update(db, CorporationCTC, id, corporation_ctc)
        if not db_corporation_ctc:
            return error_response(error=f"Corporation CTC with id {id} not found", status_code=404)
        return success_response(
            message="Corporation CTC updated successfully",
            data=serialize_params(CorporationCTCResponse.model_validate(db_corporation_ctc).model_dump())
        )
    except Exception as e:
        return handle_error(e, CorporationCTC)

@router.delete("/{id}", status_code=204)
def delete_corporation_ctc(id: int, db: Session = Depends(get_db)):
    db_corporation_ctc = db.query(CorporationCTC).filter(CorporationCTC.id == id).first()
    if not db_corporation_ctc:
        return error_response(error=f"Corporation CTC with id {id} not found", status_code=404)
    db.delete(db_corporation_ctc)
    db.commit()
    return success_response(message="Corporation CTC deleted")
