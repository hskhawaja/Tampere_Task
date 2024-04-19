import streamlit as st
import asyncio
from openai import AsyncOpenAI
import PyPDF2
from io import BytesIO

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

try:
  client = AsyncOpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
  client = AsyncOpenAI()

st.set_page_config(
    page_title="PDF Summarization Comparison",
    layout="wide",
)

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("The Magic Happens Here! 🔥")

def read_pdf(file):
    try:
        # To read the PDF file
        file_reader = PyPDF2.PdfReader(BytesIO(file.getvalue()))
        num_pages = len(file_reader.pages)

        # To combine text of all pages
        all_text = ""
        for page_num in range(num_pages):
            page = file_reader.pages[page_num]
            all_text += page.extract_text() + "\n"  # Adding a newline after each page's text

        # Save combined text to a string (not displaying on web page)
        return all_text
    except Exception as e:
        st.error(f"Error reading file: {e}")

file = st.file_uploader("", type={"pdf"})

if file:
    data = read_pdf(file)

    col1, col2 = st.columns(2)

    gpt_response = col1.empty()
    claude_response = col2.empty()

    async def generate_summary(placeholder, model):
        stream = await client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Write a 200 word summary of the text below. The first line is a 2-3 word title with an emoji and then include 2 line breaks. For example 'TITLE <emoji> \n \n ' \n TEXT:\n {data}"},],
            stream=True
        )
        streamed_text = "# "
        async for chunk in stream:
            chunk_content = chunk.choices[0].delta.content
            if chunk_content is not None:
                streamed_text = streamed_text + chunk_content
                placeholder.info(streamed_text)

    async def main():
        await asyncio.gather(
            generate_summary(gpt_response, model="gpt-3.5-turbo"),
            generate_summary(claude_response, model="gpt-4")
        )

    if data:
        asyncio.run(main())

