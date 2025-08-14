# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# قراءة الموديل المحفوظ
try:
    # تأكد إنك بتحاول تقرأ الموديل الجديد 'kmeans.pkl'
    loaded_model = joblib.load("kmeans.pkl")
    st.success("Model loaded successfully!")
except FileNotFoundError:
    # عدّل رسالة الخطأ لتكون أوضح وتتطابق مع اسم الملف الصحيح
    st.error("Error: The model file 'kmeans.pkl' was not found.")
    st.stop()

st.title("Customer Segmentation Application")
st.write("Enter the customer's spending data to find their segment.")

# قائمة بأسماء الأعمدة اللي الموديل بيشتغل عليها
features_columns = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']

# استقبال المدخلات من المستخدم لكل عمود
input_values = {}
for col in features_columns:
    input_values[col] = st.slider(f"Enter spending on {col}", min_value=0, max_value=100000, value=5000)

if st.button("Predict Customer Segment"):
    # تجهيز البيانات كـDataFrame
    input_data = pd.DataFrame([input_values])

    # بما إن الموديل هو K-Means ومُدرب بالفعل، بنستخدم .predict()
    # ده بيستخدم الموديل اللي اتعلّمه عشان يعمل تنبؤ على نقطة بيانات جديدة.
    prediction = loaded_model.predict(input_data)

    # عرض النتيجة
    st.header("Prediction Result")
    st.success(f"This customer belongs to Cluster: **{prediction[0]}**")
