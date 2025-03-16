import streamlit as st
import file_handler  # Importing the file handler module
import data_processor  # Importing the data processing module

st.title("Streamlit Modular File Handling")

# Upload file
df = file_handler.upload_file()

# Process and display data
if df is not None:
    df = data_processor.process_data(df)
    st.dataframe(df)  # Show processed data

    # Download processed file
    file_handler.download_file(df)
