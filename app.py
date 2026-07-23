import streamlit as st

st.set_page_config(page_title="My Homepage", page_icon="🙂", layout="centered")

st.markdown(
    """
    <style>
    .block-container { padding-top: 3rem; max-width: 700px; }
    .name { font-size: 2.2rem; font-weight: 700; margin-bottom: 0; }
    .tagline { font-size: 1.1rem; color: #888; margin-top: 0.2rem; }
    .avatar-placeholder {
        width: 180px; height: 180px; border-radius: 50%;
        background: linear-gradient(135deg, #6a8dff, #a06afe);
        display: flex; align-items: center; justify-content: center;
        font-size: 3rem; color: white; font-weight: 700;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- 프로필 사진 ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    uploaded = st.file_uploader("프로필 사진 업로드", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    if uploaded is not None:
        st.image(uploaded, width=180)
    else:
        st.markdown('<div class="avatar-placeholder">사진</div>', unsafe_allow_html=True)
        st.caption("위에서 사진을 업로드하면 프로필 사진으로 표시됩니다.")

st.markdown("---")

# ---- 자기소개 ----
st.markdown('<p class="name">이름을 입력하세요</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">한 줄 소개를 입력하세요</p>', unsafe_allow_html=True)

st.write("")
st.subheader("소개")
st.write(
    "여기에 자기소개 내용을 작성하세요. 어떤 일을 하고 있는지, "
    "관심 분야는 무엇인지, 어떤 사람인지 자유롭게 적어보세요."
)

st.write("")
st.subheader("연락처")
st.write("이메일: your-email@example.com")
