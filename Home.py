"""
app.py
"""
import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.set_page_config(
    page_title="PDF Summarization Comparison",
    layout="wide",
)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# Welcome to PDF Summarization! 👋")

st.markdown(
    """
    A specialized Streamlit application designed to boost your productivity by providing concise summaries of your PDF 
    documents. This app integrates two distinct LLMs — GPT-3.5 Turbo and GPT-4 — to deliver accurate and nuanced summaries.

    **How It Works:**\n
    **1. Upload Your PDFs:** Start by uploading a PDF document you need summarized. 
    
    **2. Summarization Models:**
    - GPT-3.5 Turbo
    - GPT-4

    **3. View and Compare Summaries:** The app processes your documents through both models separately and displays the summaries side-by-side, allowing you to compare and derive comprehensive insights swiftly.
    """
)

st.info("👈 Select **Summarize** from the sidebar to upload the PDF and get started!")
