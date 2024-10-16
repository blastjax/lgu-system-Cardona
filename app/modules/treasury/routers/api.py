# app/modules/treasury/routers/api.py

from fastapi import APIRouter
from app.modules.treasury.controllers import *

router = APIRouter()

router.include_router(individual_ctc_router, prefix="/ctc/individual", tags=["Treasury - Individual CTC"])