from fastapi import APIRouter
from pydantic import BaseModel
from app.core.db.sqlite import get_connection
from app.core.db.merchant_memory import correct_merchant

router = APIRouter()


class CorrectionRequest(BaseModel):
    user_id: str
    merchant: str
    category: str
    subcategory: str | None = None


@router.post("/correct")
def correct_transaction(req: CorrectionRequest):
    conn = get_connection()

    correct_merchant(
        conn=conn,
        user_id=req.user_id,
        merchant_text=req.merchant,
        correct_category=req.category,
        correct_subcategory=req.subcategory,
    )

    conn.close()

    return {"status": "success"}
