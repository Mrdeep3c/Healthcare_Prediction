import streamlit as st
from PIL import Image

st.title("Body Mass Index (BMI) 🧮")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.write("BMI is a measurement of a person's leanness or corpulence based on their height and weight, and is intended to quantify tissue mass.")

age = st.number_input("Enter Age", min_value=0, step=1)
sex = st.radio("Select Sex", ["Male", "Female"], index=None)
height = st.number_input("Enter Height (m)", min_value=1.00, step=0.001)
weight = st.number_input("Enter weight (kg)")

bmi = weight/(height * height)

st.write("Your BMI is: ", bmi)

img1 = Image.open("bmitable.png")
st.write("This is the World Health Organization's (WHO) recommended body weight based on BMI values for adults. It is used for both men and women, age 20 or older.")
st.image(img1, caption="BMI Table", width=800)

img1 = Image.open("bmichart.gif")
st.write("This is a graph of BMI categories based on the World Health Organization data. The dashed lines represent subdivisions within a major categorization.")
st.image(img1, caption="BMI Table", width=800)

