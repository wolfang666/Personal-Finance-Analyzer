import camelot
import tempfile
import pandas as pd
import numpy as np
import re
from typing import List, Dict


def parse_gpay_pdf(pdf_bytes: bytes) -> List[Dict]:
    """
    Parses a GPay transaction PDF using Camelot and returns
    a list of normalized transaction dicts.
    """

    
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(pdf_bytes)
        pdf_path = tmp.name

    tables = camelot.read_pdf(
        pdf_path,
        pages="all",
        flavor="stream"
    )

    dfs = []

    for table in tables:
        df = table.df
        df.columns = df.iloc[0]   
        df = df[1:]               
        dfs.append(df)

    if not dfs:
        return []

    full_df = pd.concat(dfs, ignore_index=True)

    full_df.replace("", np.nan, inplace=True)

    merged_rows = []
    current = {}

    for _, row in full_df.iterrows():
        date = row.get("Date & time")
        details = row.get("Transaction details")
        amount = row.get("Amount")

        if pd.notna(amount):
            if current:
                merged_rows.append(current)

            current = {
                "date": date,
                "details": details,
                "amount": amount,
            }

    if current:
        merged_rows.append(current)

    tx_df = pd.DataFrame(merged_rows)

    
    tx_df = tx_df[
        tx_df["details"]
        .str.lower()
        .str.contains("paid to", na=False)
    ].reset_index(drop=True)

    
    tx_df["date"] = pd.to_datetime(
        tx_df["date"],
        format="%d %b, %Y",
        errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    transactions: List[Dict] = []

    for _, row in tx_df.iterrows():
        details = row["details"]

        
        merchant_match = re.search(r"paid to (.*)", details, re.I)
        merchant = merchant_match.group(1).strip() if merchant_match else "Unknown"

        
        amount = (
            row["amount"]
            .replace("₹", "")
            .replace(",", "")
            .strip()
        )

        try:
            amount = float(amount)   
        except ValueError:
            continue

        transactions.append({
            "date": row["date"],
            "merchant": merchant,
            "description": details,
            "amount": amount,
        })

    return transactions
