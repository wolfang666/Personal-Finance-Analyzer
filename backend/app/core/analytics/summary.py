from app.core.db.queries import(
    monthly_spend,
    category_spend,
    top_merchants
)

def add_percentages(amount_dict: dict) -> dict:
    """
    Converts {key: amount} into
    {key: {amount, percentage}}
    """
    total = abs(sum(amount_dict.values()))

    if total == 0:
        return {
            k: {"amount": v, "percentage": 0.0}
            for k, v in amount_dict.items()
        }

    return {
        k: {
            "amount": v,
            "percentage": round(abs(v) / total * 100, 2)
        }
        for k, v in amount_dict.items()
    }

def build_summary_from_db(conn, user_id):
    monthly = monthly_spend(conn, user_id)
    category = category_spend(conn, user_id)
    merchants = top_merchants(conn, user_id)

    return {
        "monthly_spend": monthly,
        "category_spend": add_percentages(category),
        "top_merchants": add_percentages(merchants)
    }