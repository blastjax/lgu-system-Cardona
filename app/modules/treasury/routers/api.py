# app/modules/treasury/routers/api.py

from fastapi import APIRouter
from app.modules.treasury.controllers import *

router = APIRouter()

router.include_router(individual_ctc_router, prefix="/ctc/individual", tags=["Treasury - Individual CTC"])
router.include_router(corporation_ctc_router, prefix="/ctc/corporation", tags=["Treasury - Corporation CTC"])