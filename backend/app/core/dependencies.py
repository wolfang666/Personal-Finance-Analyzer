from app.core.db.sqlite import get_connection
from app.core.llm.loader import load_llm
from app.core.services.finance_service import FinanceService

_service = None

def get_finance_service():
    global _service
    if _service is None:
        conn = get_connection()
        llm = load_llm()
        _service = FinanceService(conn, llm)
    return _service
