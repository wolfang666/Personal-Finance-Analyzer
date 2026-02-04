from app.core.db.merchant_memory import (
    categorize_with_memory,
)
from app.core.db.sqlite import get_connection


def ingest_transactions(
    user_id: str,
    transactions: list[dict],
):
    """
    Ingests a list of transactions into the database.

    Each transaction dict must contain:
        - date
        - merchant
        - description
        - amount
    """

    conn = get_connection()
    cursor = conn.cursor()

    inserted = 0

    for tx in transactions:
        category, subcategory, confidence, method = categorize_with_memory(
            conn=conn,
            user_id=user_id,
            merchant_text=tx["merchant"],
            description_text=tx["description"],
        )
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    timestamp DATETIME,
    merchant TEXT,
    amount REAL,
    category TEXT,
    subcategory TEXT,
    confidence REAL,
    source TEXT
);
""")
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS merchant_memory (
    user_id TEXT,
    merchant TEXT,
    category TEXT,
    subcategory TEXT,
    confidence REAL,
    source TEXT,
    PRIMARY KEY (user_id, merchant)
);
""")
        cursor.execute(
            """
            INSERT OR IGNORE INTO transactions (
                user_id,
                timestamp,
                merchant,
                amount,
                category,
                subcategory,
                confidence,
                source
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                tx["date"],
                tx["merchant"],
                tx["amount"],
                category,
                subcategory,
                confidence,
                method,   # merchant_memory | cosine
            ),
        )

        inserted += 1

    conn.commit()
    conn.close()

    return inserted
