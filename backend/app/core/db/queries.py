import sqlite3

def monthly_spend(conn: sqlite3.Connection, user_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m', timestamp), SUM(amount)
        FROM transactions
        WHERE user_id = ?
        GROUP BY 1
        ORDER BY 1
    """, (user_id,))
    return {row[0]: round(row[1], 2) for row in cursor.fetchall()}


def category_spend(conn: sqlite3.Connection, user_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE user_id = ?
        GROUP BY category
        ORDER BY SUM(amount)
    """, (user_id,))
    return {row[0]: round(row[1], 2) for row in cursor.fetchall()}

def top_merchants(conn: sqlite3.Connection, user_id, limit=5):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT merchant, SUM(amount)
        FROM transactions
        WHERE user_id = ?
        GROUP BY merchant
        ORDER BY SUM(amount)
        LIMIT ?
    """, (user_id, limit))
    return {row[0]: round(row[1], 2) for row in cursor.fetchall()}