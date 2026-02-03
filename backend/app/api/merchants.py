from fastapi import APIRouter
from app.core.db.sqlite import get_connection

router = APIRouter()

@router.get("/merchants/{user_id}")
def list_merchants(user_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT DISTINCT merchant FROM transactions WHERE user_id = ? ORDER BY merchant""",
        (user_id,)
    )
    merchants = [row[0] for row in cursor.fetchall()]
    conn.close()
    return merchants
