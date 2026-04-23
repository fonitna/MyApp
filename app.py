import streamlit as st

st.set_page_config(page_title="My Multi-page App", layout="wide")

st.title("🏠 หน้าหลัก (Homepage)")
st.write("ยินดีต้อนรับเข้าสู่เว็บไซต์ที่สร้างด้วย Streamlit บน Colab ครับ")

st.info("👈 คุณสามารถคลิกเลือกหน้าที่ 2 ได้ที่แถบเมนูด้านซ้ายมือ")

if st.button("คลิกเพื่อดูความลับ"):
    st.balloons()
    st.success("ยินดีด้วย! คุณเจอความลับแล้ว")

if st.button("ไปที่หน้าที่สอง"):
    st.switch_page("pages/second_page.py")
