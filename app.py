import streamlit as st
from pathlib import Path
import tempfile
from universal_converter import UniversalConverter

st.set_page_config(
    page_title="Universal MD Converter", 
    page_icon="📝", 
    layout="centered"
)

# Serve local icon file for PWABuilder manifest validation
icon_path = Path("icon.png")
if icon_path.exists():
    with open(icon_path, "rb") as f:
        st.image(f.read(), width=0) # Hidden or just loaded in context