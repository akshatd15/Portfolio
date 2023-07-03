import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image(r"images\main_photo.jpg")

with col2:
    st.title("Akshat Baliyan")
    content = """Hi, I am Akshat Baliyan! I am a python programmer , a ML engineer and an AI engineer 
    """
    st.info(content)

st.write("Below you can find some of the appsI have built in Python. Feel free to contact me!")

col3, empty_col, col4 = st.columns([2,1,2])
df = pandas.read_csv("data.csv",sep=";")


with col3:
    for index, row in df[1:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        img = row["image"]
        st.image(f"images\{img}")
        link=row["url"]
        st.write(f"[Source Code]({link})")

with col4:
    for index, row in df[4:7].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        img = row["image"]
        st.image(f"images\{img}")
        link=row["url"]
        st.write(f"[Source Code]({link})")

col5, empty_col_2, col6 = st.columns([2,1,2])


st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

with col5:
    st.header("Ongoing")
    for index, row in df[7:8].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        img = row["image"]
        st.image(f"images\{img}")
        link=row["url"]
        st.write(f"[Source Code]({link})")