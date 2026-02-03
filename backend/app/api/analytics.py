from fastapi import APIRouter
from app.core.dependencies import get_finance_service

router = APIRouter()

@router.get("/summary/{user_id}")
def summary(user_id: str):
    service = get_finance_service()
    return service.get_summary(user_id)