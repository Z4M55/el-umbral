import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="El Umbral",
    page_icon="○",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Eliminar todo el chrome de Streamlit — experiencia inmersiva
st.markdown("""
<style>
  #MainMenu, header, footer { visibility: hidden; }
  [data-testid="stAppViewContainer"] { background: #0c0906; padding: 0; }
  [data-testid="stVerticalBlock"]    { gap: 0 !important; padding: 0 !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { display: block; border: none; }
</style>
""", unsafe_allow_html=True)

html_content = (Path(__file__).parent / "umbral_web.html").read_text(encoding="utf-8")
components.html(html_content, height=750, scrolling=False)
