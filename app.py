import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="El Umbral",
    page_icon="○",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Ocultar el chrome de Streamlit para experiencia inmersiva
st.markdown("""
<style>
  #MainMenu, header, footer { visibility: hidden; }
  [data-testid="stAppViewContainer"] { background: #0c0906; padding: 0; }
  [data-testid="stVerticalBlock"]    { gap: 0 !important; padding: 0 !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { display: block; }
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "umbral_web.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=740, scrolling=False)
