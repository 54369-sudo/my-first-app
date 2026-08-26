import streamlit as st

# ส่วนที่ 1 หัวข้อหน้าเว็บ (Title สีแดง)
st.markdown("# :red[🏋️ คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

# ส่วนที่ 2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

# ส่วนที่ 3 ปุ่มและการคำนวณ
if st.button("คำนวณค่า BMI"):
    # แปลงส่วนสูงจากเซนติเมตรเป็นเมตร
    height_m = height_cm / 100
    
    # คำนวณค่า BMI
    bmi = weight / (height_m ** 2)
    
    st.write(f"### ค่า BMI ของคุณคือ: **{bmi:.2f}**")
    
    # การแปลผลตามเงื่อนไข
    if bmi < 18.5:
        st.warning("ผอม")
    elif 18.5 <= bmi < 23.0:
        st.success("สุขภาพดี")
    elif 23.0 <= bmi < 25.0:
        st.info("ท้วม")
    else:
        st.error("อ้วน")

# เส้นกั้นและแสดงข้อมูลผู้จัดทำ
st.divider()
st.write("ชื่อ-สกุล: กฤตยชญ์ อุ่นคำ | เลขที่: 22 | ห้อง: 402")
