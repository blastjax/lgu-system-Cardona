from fastapi import APIRouter
from app.modules.treasury.routers.api import router as treasury_router
# from app.modules.accounting.routers.api import router as accounting_router

router = APIRouter()

# Include module-specific routers with the module name as the prefix
router.include_router(treasury_router, prefix="/treasury")
# router.include_router(accounting_router, prefix="/accounting")
