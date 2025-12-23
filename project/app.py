import streamlit as st


# Page Config

st.set_page_config(page_title="AI Chatbot Mentor", layout="centered")

# Welcome Screen

st.title("👋 Welcome to AI Chatbot Mentor")
st.markdown(
    """
Your personalized AI learning assistant.

Please select a learning module to begin your mentoring session.
"""
)

# Module Selection

mentor_subject = st.selectbox(
    " Select a Learning Module",
    [
        "Python",
        "SQL",
        "Power BI",
        "Exploratory Data Analysis (EDA)",
        "Machine Learning (ML)",
        "Deep Learning (DL)",
        "Generative AI (Gen AI)",
        "Agentic AI"
    ]
)


# Start Session

if st.button(" Start Mentoring", use_container_width=True):
    st.session_state["mentor_subject"] = mentor_subject
    st.session_state["messages"] = []
    st.switch_page("pages/chat_page.py")
