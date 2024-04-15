import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.title("About Us :eyes:")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.write("The goal of this project is to build a predictive model that can estimate the medical insurance costs for individuals based on their age, gender, BMI, smoking status, and other related factors. The dataset used in this project contains information about medical insurance costs for a group of people based on these factors.")
medical_df = pd.read_csv('insurance.csv')

with st.expander("🔎 Dataframe Preview"):
    st.write(medical_df)

st.title("About the Dataset")
st.markdown("Age: Age of the insured person (numeric)")
st.markdown("Sex: Gender of the insured person (categorical: male/female)")
st.markdown("BMI: Body mass index of the insured person (numeric)")
st.markdown("Children: Number of children covered by the insurance plan (numeric)")
st.markdown("Smoker: Whether or not the insured person is a smoker (categorical: yes/no)")
st.markdown("Region: Region where the insured person resides (categorical: northeast/northwest/southeast/southwest)")
st.markdown("Charges: The insurance charges/costs billed to the insured person (numeric)")


col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots(figsize=(2,2))

    sns.countplot(x=medical_df.age, ax=ax)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    plt.title(f"Count Plot of Age vs Count", fontsize=6)
    plt.xlabel("Age", fontsize=5)
    plt.ylabel("Count", fontsize=5)

    st.pyplot(fig)


    fig, ax = plt.subplots(figsize=(2,2))

    sns.countplot(x=medical_df.children, ax=ax)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    plt.title(f"Count Plot of Children vs Count", fontsize=6)
    plt.xlabel("Children", fontsize=5)
    plt.ylabel("Count", fontsize=5)

    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(2,2))

    sns.countplot(x=medical_df.sex, ax=ax)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    plt.title(f"Count Plot of Sex vs Count", fontsize=6)
    plt.xlabel("Sex", fontsize=5)
    plt.ylabel("Count", fontsize=5)

    st.pyplot(fig)


    fig, ax = plt.subplots(figsize=(2,2))

    sns.countplot(x=medical_df.smoker, ax=ax)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    plt.title(f"Count Plot of Smoker vs Count", fontsize=6)
    plt.xlabel("Smoker", fontsize=5)
    plt.ylabel("Count", fontsize=5)

    st.pyplot(fig)

with col3:
    fig, ax = plt.subplots(figsize=(2,2))

    sns.countplot(x=medical_df.bmi, ax=ax)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    plt.title(f"Count Plot of BMI vs Count", fontsize=6)
    plt.xlabel("Bmi", fontsize=5)
    plt.ylabel("Count", fontsize=5)

    st.pyplot(fig)


    fig, ax = plt.subplots(figsize=(2,2))

    sns.countplot(x=medical_df.region, ax=ax)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    plt.title(f"Count Plot of Region vs Count", fontsize=6)
    plt.xlabel("Region", fontsize=5)
    plt.ylabel("Count", fontsize=5)

    st.pyplot(fig)


