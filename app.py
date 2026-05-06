import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AgroPredict IA",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Eliminar todos los márgenes y padding de Streamlit
st.markdown("""
    <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {
            padding: 0 !important;
        }
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header[data-testid="stHeader"] {
            display: none !important;
        }
        .stApp {
            margin: 0 !important;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1080, scrolling=False)
