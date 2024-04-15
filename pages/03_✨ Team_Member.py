import streamlit as st
from PIL import Image

st.title("Team Members ✨")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.title(" ")

img1 = Image.open("ayush.jpg")
col1, col2 = st.columns(2)
with col1:
    st.image(img1, caption="Ayush Yadav", width=300)
with col2:
    st.title("Ayush Yadav")
    st.write("Team Leader")
    st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic")

st.title(" ")

img2 = Image.open("deepak.jpg")
col1, col2 = st.columns(2)
with col1:
    st.title("Deepak Kumar ")
    st.write("Team member")
    st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic")
with col2:
    st.image(img2, caption="Deepak Kumar", width=300)

st.title(" ")

img3 = Image.open("akash.jpg")
col1, col2 = st.columns(2)
with col1:
    st.image(img3, caption="Akash Pandey", width=300)
with col2:
    st.title("Akash Pandey")
    st.write("Team Member")
    st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic")

st.title(" ")

img4 = Image.open("yuvraj.jpg")
col1, col2 = st.columns(2)
with col1:
    st.title("Yuvraj Anand")
    st.write("Team member")
    st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic")
with col2:
    st.image(img4, caption="Yuvraj Anand", width=300)


