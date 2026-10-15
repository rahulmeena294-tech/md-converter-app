import streamlit as st
from pathlib import Path
import tempfile
from universal_converter import UniversalConverter

st.set_page_config(page_title="Universal MD Converter", page_icon="📝", layout="centered")

st.title("📝 Universal File to Markdown Converter")
st.write("Convert your Excel, Word, PDF, or text files into Markdown instantly.")

uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "xls", "csv", "docx", "pdf", "txt"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = Path(tmp.name)

    st.info(f"File uploaded: {uploaded_file.name}")

    if st.button("Convert to Markdown (.md)"):
        try:
            converter = UniversalConverter()
            out_path = converter.convert(tmp_path, output_format="md")
            
            with open(out_path, "r", encoding="utf-8") as f:
                md_text = f.read()

            st.success("Conversion successful!")
            st.download_button(
                label="📥 Download Converted Markdown File",
                data=md_text,
                file_name=f"{Path(uploaded_file.name).stem}_converted.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"Error during conversion: {e}")