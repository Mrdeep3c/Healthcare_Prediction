import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import streamlit as st
import altair as alt


medical_df = pd.read_csv('insurance.csv')

medical_df.replace({'sex':{'male':0,'female':1}},inplace=True)
medical_df.replace({'smoker':{'yes':0,'no':1}},inplace=True)
medical_df.replace({'region':{'southeast':0,'southwest':1,'northwest':2,'northeast':3}},inplace=True)


X= medical_df.drop('charges',axis=1)
y = medical_df['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)
lg = LinearRegression()
lg.fit(X_train,y_train)
y_pred = lg.predict(X_test)
r2_score(y_test,y_pred)

#web app
st.set_page_config(page_title="Medical", page_icon=":ambulance:", layout="wide")

st.title("Medical Insurance Prediction :health_worker::medical_symbol: ")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.write("Medical insurance is one of the most crucial aspects of healthcare, and machine learning techniques can play a significant role in analyzing and predicting medical insurance costs. ")

col1, col2 = st.columns(2)

columns = medical_df.columns.tolist()

with col1:
    st.write("")
    st.write(medical_df.head())

with col2:
    x_axis = st.selectbox("Select the X-axis", options=columns + ["None"], index=None)
    y_axis = st.selectbox("Select the Y-axis", options=columns + ["None"], index=None)

    plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]

    selected_plot = st.selectbox("Select a Plot", options=plot_list, index=None)

#button to generaate plots
if st.button("Generate Plot"):

    fig, ax = plt.subplots(figsize=(10,4))

    if selected_plot == "Line Plot":
        sns.lineplot(x=medical_df[x_axis], y=medical_df[y_axis], ax=ax)
    
    elif selected_plot == "Bar Chart":
        sns.barplot(x=medical_df[x_axis], y=medical_df[y_axis], ax=ax)
    
    elif selected_plot == "Scatter Plot":
        sns.scatterplot(x=medical_df[x_axis], y=medical_df[y_axis], ax=ax)
    
    elif selected_plot == "Distribution Plot":
        sns.histplot(medical_df[x_axis], kde=True, ax=ax)
    
    elif selected_plot == "Count Plot":
        sns.countplot(x=medical_df[x_axis], ax=ax)

    #adjust label sizes
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    #title axes labels
    plt.title(f"{selected_plot} of {x_axis} vs {y_axis}", fontsize=12)
    plt.xlabel(x_axis, fontsize=10)
    plt.ylabel(y_axis, fontsize=10)

    st.pyplot(fig)


age = st.text_input("Enter Age")
sex = st.selectbox("Select Sex", ["Male", "Female"])
bmi = st.text_input("Enter BMI")
children = st.number_input("Enter Number of Children", min_value=0, step=1)
smoker = st.selectbox("Are you a smoker?", ["Yes", "No"])
region = st.selectbox("Select Region", ["Southeast", "Southwest", "Northwest", "Northeast"])

if st.button("Predict"):
    try:
        sex_val = 0 if sex == "Male" else 1
        smoker_val = 0 if smoker == "Yes" else 1
        region_val = {"Southeast": 0, "Southwest": 1, "Northwest": 2, "Northeast": 3}[region]
        
        features = [float(age), sex_val, float(bmi), children, smoker_val, region_val]
        
        prediction = lg.predict([features])
        
        st.write("Predicted Medical Insurance for this person is :", prediction[0])
    except ValueError:
        st.write("Please enter valid numerical values for Age and BMI.")


