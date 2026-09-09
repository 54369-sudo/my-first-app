import time
import streamlit as st

# หัวข้อโปรแกรมตามธีมเกมในใบงาน 2.3
st.title("⏱️ Quiz ENG MINGGARABA 👶🏿👶🏿👶🏿")

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state (10 ข้อ)
# ----------------------------------------------------
for i in range(1, 11):
    key = f"ans{i}_val"
    if key not in st.session_state:
        st.session_state[key] = ""


# ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    for i in range(1, 11):
        st.session_state[f"ans{i}_val"] = ""
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 2. ฟังก์ชัน MessageBox (Dialog) สรุปผลตามเกณฑ์ในใบงาน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(answers):
    st.balloons()
    score = 0

    # เฉลยคำตอบถูกต้อง 10 ข้อตามใบงาน 2.3
    correct_answers = [
        "dog",
        "cat",
        "elephant",
        "lion",
        "monkey",
        "chameleon",
        "flamingo",
        "hedgehog",
        "sloth",
        "hippopotamus",
    ]

    st.subheader("📝 ผลการตรวจคำตอบ")

    for i in range(10):
        u_ans = answers[i].strip().lower()
        c_ans = correct_answers[i]

        if u_ans == c_ans:
            st.success(f"✅ ข้อ {i+1}: ถูกต้อง ({c_ans})")
            score += 1
        else:
            st.error(
                f"❌ ข้อ {i+1}: ยังไม่ถูกต้อง (คุณตอบ '{u_ans}' | เฉลย '{c_ans}')"
            )

    st.divider()
    st.info(f"🏆 คุณได้คะแนนรวม: {score} / 10 คะแนน")

    # 📌 เกณฑ์ประเมินผู้เล่น (If-Else) ตามข้อความในเอกสารใบงาน 2.3
    if score >= 8:
        st.success("คือโหดคักแท้! คุณผ่านเกณฑ์ระดับ หัวจ่าย")
    elif score >= 6:
        st.info("ไอ้อ้วน 67 เก่งมาก")
    elif score >= 3:
        st.warning("ได้แค่นี้เหรอ")
    elif score >= 1:
        st.error("💩👈 # หมอตัดช้อย สก้อยกาเลย")
    else:
        st.error("เสปิร์ม 💩")


# ----------------------------------------------------
# 3. ปุ่มเริ่มเล่นเกม & ระบบจับเวลา (60 วินาที)
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ----------------------------------------------------
# 4. ช่องรับคำตอบ 10 ข้อ ตามรายการข้อคำถามในใบงาน
# ----------------------------------------------------
questions = [
    "ข้อ 1: 🐶",
    "ข้อ 2: 🐱",
    "ข้อ 3: 🐘",
    "ข้อ 4: 🦁",
    "ข้อ 5: 🐵",
    "ข้อ 6: 🦎",
    "ข้อ 7: 🦩",
    "ข้อ 8: 🦔",
    "ข้อ 9: 🦥",
    "ข้อ 10: 🦛",
]

user_answers = []
for i in range(10):
    ans = st.text_input(
        questions[i],
        value=st.session_state[f"ans{i+1}_val"],
        key=f"input_{i+1}",
    )
    user_answers.append(ans)
    st.session_state[f"ans{i+1}_val"] = ans

# ----------------------------------------------------
# 5. ปุ่มส่งคำตอบ & แสดง Popup Dialog
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(user_answers)

st.divider()
st.write("กลุ่ม3🧜🏿")
