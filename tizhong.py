import streamlit as st

st.title("BMI 计算器")


weight = st.number_input("请输入你的体重(单位:kg)", min_value=0.0, max_value=300.0, value=50.0, step=0.1)
height = st.number_input("请输入你的身高(单位:m)",  min_value=0.0, max_value=2.5, value=1.70, step=0.01)


if st.button("开始计算"):

    bmi = weight / (height ** 2)
    

    st.write(f"您的BMI为: {bmi:.2f}")
    

    if bmi < 18.5:
        st.warning("💀")
    elif bmi < 25:
        st.success("您的身体很健康！")
    else:
        st.error("🐖")
