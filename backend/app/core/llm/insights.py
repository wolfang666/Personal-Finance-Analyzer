from app.config import (
    LLM_TEMPERATURE,
    LLM_TOP_P,
    LLM_MAX_TOKENS
)


def build_prompt(summary: dict) -> str:
    """
    Generates natural language insights from precomputed financial summaries.
    The LLM is used ONLY for explanation, not computation.
    """

    
    if not summary or not any(summary.values()):
        return "No sufficient transaction data available to generate insights."

    return f"""
You are a financial analyst generating insights from precomputed data.

Rules:
- Do NOT mention that you are an AI or language model.
- Do NOT add disclaimers or generic financial advice.
- Do NOT explain general finance concepts.
- All numbers are already calculated.
- Analyze ONLY the data provided.
- Be concise, practical, and specific.
- Everything is in INR or Indian Rupee

Spending summary:

Monthly spending:
{summary.get("monthly_spend", {})}

Category-wise spending:
{summary.get("category_spend", {})}

Top merchants:
{summary.get("top_merchants", {})}

Task:
1. Summarize overall spending behavior.
2. Identify the dominant expense categories.
3. Point out any notable trends or concerns.
4. Keep the response within 4–6 sentences.
"""


def generate_llm_insights(llm,summary: dict):
    prompt=build_prompt(summary)
    response = llm(
        prompt,
        temperature = LLM_TEMPERATURE,
        top_p = LLM_TOP_P,
        max_tokens = LLM_MAX_TOKENS
    )
    return response["choices"][0]["text"].strip()
