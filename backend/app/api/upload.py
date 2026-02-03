from fastapi import APIRouter, UploadFile, File
from app.core.ingestion.gpay import parse_gpay_pdf
from app.core.ingestion.pipeline import ingest_transactions

router = APIRouter()


@router.post("/upload/gpay")
async def upload_gpay_pdf(
    file: UploadFile = File(...),
    user_id: str = "default",
):
    pdf_bytes = await file.read()

    transactions = parse_gpay_pdf(pdf_bytes)

    inserted = ingest_transactions(
        user_id=user_id,
        transactions=transactions,
    )

    return {
        "status": "success",
        "inserted": inserted,
    }
