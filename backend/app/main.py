from fastapi import FastAPI
from app.core.db.sqlite import get_connection
from app.core.llm.loader import load_llm
from app.core.services.finance_service import FinanceService
from app.api.analytics import router as analytics_router
from app.api.insights import router as insights_router
from app.api.upload import router as upload_router
from app.api.corrections import router as correction_router
from app.api.merchants import router as merchants_router



app = FastAPI(title="Personal Finance Analyzer")

conn = get_connection()
llm = load_llm()
finance_service =  FinanceService(conn, llm)

app.include_router(analytics_router)
app.include_router(insights_router)
app.include_router(upload_router)
app.include_router(correction_router)
app.include_router(merchants_router)