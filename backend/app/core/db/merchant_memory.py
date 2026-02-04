from app.core.categorisation import categorize

def normalize_merchant(text: str) -> str:
    return text.lower().strip()

def lookup_merchant_memory(conn, user_id, merchant):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT category, subcategory, confidence, source
        FROM merchant_memory
        WHERE user_id = ? AND merchant = ?
        ORDER BY
          CASE source
            WHEN 'user' THEN 1
            ELSE 2
          END
        LIMIT 1
        """,
        (user_id, merchant),
    )
    return cursor.fetchone()


def store_merchant_memory(
    conn,
    user_id,
    merchant,
    category,
    subcategory,
    confidence,
    source,
):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT OR REPLACE INTO merchant_memory
        (user_id, merchant, category, subcategory, confidence, source)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            merchant,
            category,
            subcategory,
            confidence,
            source,
        ),
    )
    conn.commit()

def categorize_with_memory(
    conn,
    user_id,
    merchant_text,
    description_text,
    threshold=0.6,
):
    merchant_key = normalize_merchant(merchant_text)

    #Merchant memory lookup
    memory = lookup_merchant_memory(conn, user_id, merchant_key)
    if memory:
        category, subcategory, confidence, source = memory
        return category, subcategory, confidence, "merchant_memory"

    #Cosine similarity fallback
    category, subcategory, confidence = categorize(description_text)

    #Auto-learn only if confidence is high
    if confidence >= threshold:
        store_merchant_memory(
            conn,
            user_id,
            merchant_key,
            category,
            subcategory,
            confidence,
            source="system",
        )

    return category, subcategory, confidence, "cosine"


def correct_merchant(
    conn,
    user_id,
    merchant_text,
    correct_category,
    correct_subcategory=None,
):
    merchant_key = normalize_merchant(merchant_text)

    store_merchant_memory(
        conn,
        user_id,
        merchant_key,
        correct_category,
        correct_subcategory,
        confidence=1.0,
        source="user",
    )
