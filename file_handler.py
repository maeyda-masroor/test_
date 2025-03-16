import streamlit as st
import pandas as pd

def upload_file():
    """Handles file upload and returns a DataFrame"""
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None

def download_file(df):
    """Provides a CSV download button"""
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Processed CSV",
        data=csv,
        file_name="processed_data.csv",
        mime="text/csv"
    )
