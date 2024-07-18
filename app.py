import streamlit as st
from pages import (
    
    visualize_data,
    filing_qa,
    financial_overview,
)

st.set_page_config(page_title="Financial Analysis Tool", page_icon=":chart_with_upwards_trend:")

# Sidebar Navigation
st.sidebar.title("Financial Analysis Tool")
page = st.sidebar.selectbox(
    "Select a Page",
    [
        "Home",
        "Visualize Data",
        "Q&A with Filing",
        "Financial Overview",
    ],
)

# Page Display
if page == "Home":
    st.title("Welcome to the Financial Analysis Tool")
    st.write("""
        This tool allows you to:
        - Upload financial filings for analysis.
        - Visualize financial data in various formats.
        - Perform Q&A with uploaded filings.
        - Conduct stock analysis.
        - Get an overview of financial data.
        
        Use the sidebar to navigate to different pages of the application.
    """)

elif page == "Visualize Data":
    visualize_data.app()
elif page == "Q&A with Filing":
    filing_qa.app()

elif page == "Financial Overview":
    financial_overview.app()
