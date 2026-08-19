import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "start" not in st.session_state:
    st.session_state.start = time.time()
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

# ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""      # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""      # เคลียร์ค่าช่องข้อ 2
    st.session_state.start = time.time() # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog

# ฟังก์ชัน MessageBox (Dialog) สรุปผล
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0
    
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    
    # ตรวจคำตอบ (ปรับเปลี่ยนคำตอบที่ถูกต้องได้ตามต้องการ)
    if u_ans1 == "apple":
        score += 1
    if u_ans2 == "banana":
        score += 1
        
    end_time = time.time()
    elapsed_time = round(end_time - st.session_state.start, 2)
    
    st.write(f"🎉 คุณได้คะแนน: **{score} / 2** คะแนน")
    st.write(f"⏱️ ใช้เวลาไปทั้งหมด: **{elapsed_time}** วินาที")
    
    if st.button("เล่นอีกครั้ง"):
        reset_game()
        st.rerun()

# --- ส่วนของการแสดงผล UI ---

# ช่องป้อนคำตอบ
ans1 = st.text_input("ข้อที่ 1: ผลไม้สีแดง (a_p_e)", value=st.session_state.ans1_val, key="input_ans1")
ans2 = st.text_input("ข้อที่ 2: ผลไม้สีเหลือง (b_n_n_a)", value=st.session_state.ans2_val, key="input_ans2")

col1, col2 = st.columns(2)

with col1:
    if st.button("ส่งคำตอบ", type="primary"):
        show_result_dialog(ans1, ans2)

with col2:
    if st.button("เริ่มใหม่"):
        reset_game()
        st.rerun()
