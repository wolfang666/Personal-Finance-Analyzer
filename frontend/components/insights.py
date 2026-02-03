import streamlit as st

def render_insights(text: str):
    st.subheader("AI-Generated Insights")
   
    st.markdown(
    f"""
   <div style="
    background-color:#f6f8fa;
    padding:10px;
    border-radius:8px;
    font-size:14px;
    line-height:1.4;
    max-height:220px;
    overflow:hidden;
    color:black;
    ">
    {text}
    </div>
    """,
    unsafe_allow_html=True
)

    
