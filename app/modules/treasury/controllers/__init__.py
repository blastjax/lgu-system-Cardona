# app/modules/treasury/controllers/__init__.py

from .individual_ctc_controller import router as individual_ctc_router
# Add more controller imports here as needed

__all__ = [
    "individual_ctc_router",
    # Add all router names here
]
