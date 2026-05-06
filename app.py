import streamlit as st
import streamlit.components.v1 as components

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.set_page_config(page_title="AgroPredict IA", layout="wide")
components.html(html_content, height=900, scrolling=True)
