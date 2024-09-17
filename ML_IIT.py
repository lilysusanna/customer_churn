# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:05:13 2022

@author: Lily, Ajay, Baseet, Adithya, Sudhanshu
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
import StandardScaler


st.title('Welcome To Churn Prediction')

st.sidebar.header('User Input Parameters')


def user_input_features():
    vm = st.sidebar.radio("Voice mail plan", ["Yes", "No"])

    ip = st.sidebar.selectbox("International plan", ["Yes", "No"])

    vm = 1 if vm == 'Yes' else 0
    ip = 1 if ip == 'Yes' else 0

    im = st.sidebar.number_input("International mins", min_value=0, max_value=25, value=0)
    cs = st.sidebar.number_input("Customer service calls", min_value=0, max_value=10, step=1)
    ic = st.sidebar.number_input("International calls", min_value=0, max_value=20, step=1)
    tc = st.sidebar.number_input("Total Charge", min_value=0, max_value=100, step=0)
    al = st.sidebar.number_input("account_length", min_value=0, max_value=250, step=0)
    dm = st.sidebar.number_input("day_mins", min_value=0, max_value=350, step=0)
    em = st.sidebar.number_input("evening_mins", min_value=0.0, max_value=370.0, step=0.0)
    nm = st.sidebar.number_input("night_mins", min_value=23.2, max_value=400.0, step=0.0)
    dc = st.sidebar.number_input("day_calls", min_value=0, max_value=180, step=0)
    ec = st.sidebar.number_input("evening_calls", min_value=0, max_value=180, step=0)
    nc = st.sidebar.number_input("night_calls", min_value=0, max_value=180, step=0)


    new = {
        'voice_mail_plan': vm,
        'international_plan': ip,
        'International_mins': im,
        'customer_service_calls': cs,
        'international_calls': ic,
        'Total Charge': tc,
        'account_length' : al,
        'day_mins' : dm,
        'evening_mins' : em,
        'night_mins' : nm,
        'day_calls' : dc,
        'evening_calls' : ec,
        'night_calls' : nc
    }
    features = pd.DataFrame(new, index=[0])
    return features


df = user_input_features()


with open(file="scaler.pkl", mode="rb") as s:
    scaler = pickle.load(s)
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

st.write(scaled_df)



with open(file="ML_IIT.pkl", mode="rb") as f:
    model = pickle.load(f)


st.write("Model loaded")

result = model.predict(scaled_df)
st.subheader('Predicted Result')

if st.button('Predict'):
    if result[0] == 0:
        st.write("Customer will not Churn")
    else:
        st.write("Customer will Churn")
