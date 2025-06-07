from .patient import router as patient_router
from .doctor import router as doctor_router

__all__ = [
    "patient_router",
    "doctor_router"
]
