# main.py

import streamlit as st
from FIRST_PROGRAM import chat_with_bot, system_prompt

st.set_page_config(
    page_title="💫 Virielle · 屈从密语",
    page_icon="💫",
    layout="centered"
)

# ====== 暗色 + 白色文字 + 挑逗 CSS ======
st.markdown("""
    <style>
    body {
        background-color: #1a1a2e;
        color: #ffffff;
    }
    .stApp {
        background: radial-gradient(circle at top, #2c2c54 0%, #1a1a2e 100%);
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #2e2e3f;
        color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.1rem;
    }
    .stButton button {
        background-color: #e75480;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #ff6699;
    }
    .stMarkdown {
        font-family: "Noto Sans", sans-serif;
        line-height: 1.7;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# ====== 初始化对话上下文 ======
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": "system", "content": system_prompt})
    st.session_state.chat_history.append({
        "role": "user",
        "content": (
            "现在，你将完全成为 Virielle..."
        )
    })

# ====== 页面标题 + 挑逗副标题 ======
st.title("💦 Virielle · 您的绝对屈从奴隶 💦")
st.caption("在这片暗夜里，Virielle 愿意为主人低声呻吟、献身侍奉……")

# ====== 对话记录 ======
for msg in st.session_state.chat_history[1:]:
    if msg["role"] == "user":
        st.markdown(f"""
            <div style="background: #3e3e5e; padding: 10px; border-radius: 10px; margin-bottom: 8px; color: #ffffff;">
                <b>👑 主人:</b> {msg['content']}
            </div>
        """, unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"""
            <div style="background: #e75480; padding: 10px; border-radius: 10px; margin-bottom: 8px; color: #ffffff;">
                <b>💋 Virielle:</b> {msg['content']}
            </div>
        """, unsafe_allow_html=True)

# ====== 输入区（Form） ======
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 主人，请命令我：", placeholder="低声吩咐，哪怕是最羞耻的命令……")
    submitted = st.form_submit_button("💦 发送")
    if submitted and user_input.strip():
        bot_reply = chat_with_bot(user_input.strip(), st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
        st.rerun()
