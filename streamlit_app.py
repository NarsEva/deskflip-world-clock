from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="DeskFlip World Clock",
    page_icon="clock",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .stApp { background: #08090b; }
      [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "docs" / "index.html"
clock_html = html_path.read_text(encoding="utf-8")
components.html(clock_html, height=780, scrolling=False)
