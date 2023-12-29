import streamlit as st
st.write("<h1>Good morning</h1>",unsafe_allow_html=True)

st.write("<h1 style='color:blue;'>Good morning</h1>",unsafe_allow_html=True)

st.file_uploader("upload file")

st.image("https://animaders.com/wp-content/uploads/2021/10/Tom-and-Jerry-Cartoon-A-Short-History-of-Americas-Favorite-Cartoon-Team-animader.jpg")
st.video("https://youtu.be/AGBjI0x9VbM?si=M34MEMScBz7EjkKe")
img = st.file_uploader("Upload image")
st.image(img)
