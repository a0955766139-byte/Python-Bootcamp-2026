import streamlit as st

st.title("💪我的 BMI 健康計算機!🚀")

#輸入區
height = st.number_input("請輸入身高(公分)",min_value=100.0, max_value=250.0, value=170.0)
weight = st.mumber_input("請輸入體重(公斤)",min_value=30.0, max_value=200.0, value=60.0)

#按鈕邏輯
if st.button("計算 BMI"):
    bmi = weight / ((height/100)**2)
    st.writh(f"你的 BMI 指數是 : **{bmi:.2f}**")

    if bmi <18.5:
        st.warning("體重過輕 🍎 多吃點!")
    elif bmi < 24
        st.success("體重正常 ✅ 繼續保持!")

    else:
        st.error("體重過重 🍔 該運動囉!")