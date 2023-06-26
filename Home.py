import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image(r"images\photo1.jpg")

with col2:
    st.title("Akshat Baliyan")
    content = """Hi, I am Akshat Baliyan! I am a python programmer , a ML engineer and an AI engineer 
    """
    st.info(content)

st.write("Below you can find some of the appsI have built in Python. Feel free to contact me!")

col3, empty_col, col4 = st.columns([2,1,2])
df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        img = row["image"]
        st.image(f"images\{img}")
        link=row["url"]
        st.write(f"[Source Code]({link})")

with col4:
    for index, row in df[10:20].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        img = row["image"]
        st.image(f"images\{img}")
        link=row["url"]
        st.write(f"[Source Code]({link})")
