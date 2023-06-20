import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images\photo.jpg")

with col2:
    st.title("Akshat Baliyan")
    content = """Hi, I am Akshat Baliyan! I am a python programmer , a ML engineer and an AI engineer 
    """
    st.info(content)
