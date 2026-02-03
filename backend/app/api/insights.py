from fastapi import APIRouter
from app.core.dependencies import get_finance_service


router = APIRouter()

@router.get("/insights/{user_id}")
def insights(user_id: str):
    service = get_finance_service()
    text = service.get_insights(user_id)
    return {"insights": text}
