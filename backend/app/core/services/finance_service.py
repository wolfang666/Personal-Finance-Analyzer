from app.core.analytics.summary import build_summary_from_db
from app.core.llm.insights import generate_llm_insights


class FinanceService:
    def __init__(self,conn,llm):
        self.conn = conn
        self.llm = llm
    
    def get_summary(self,user_id: str) -> dict:
        return build_summary_from_db(self.conn, user_id)
    
    def get_insights(self,user_id: str) -> dict:
        summary = self.get_summary(user_id)
        return generate_llm_insights(self.llm,summary)
    
    