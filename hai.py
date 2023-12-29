import streamlit as st
st.write("<h1>Good morning</h1>",unsafe_allow_html=True)

st.write("<h1 style='color:blue;'>Good morning</h1>",unsafe_allow_html=True)

st.file_uploader("upload file")

st.image("https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*")
st.video("https://youtu.be/AGBjI0x9VbM?si=M34MEMScBz7EjkKe")
img = st.file_uploader("Upload image")
st.image(img)
