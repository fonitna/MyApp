import streamlit as st

st.set_page_config(page_title="My Multi-page App", layout="wide")

st.title("🏠 หน้าหลัก")
st.write("### **Boot Camp:** Data Science and Machine Learning")
st.write("##### 7 Day Intensive Hands-on Workshop")
st.write("### **Day 1:** การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("คลิกเพื่อดูความลับ"):
    st.balloons()
    st.success("ยินดีด้วย! คุณเจอความลับแล้ว")

if st.button("ไปที่หน้าที่สอง"):
    st.switch_page("pages/second_page.py")
