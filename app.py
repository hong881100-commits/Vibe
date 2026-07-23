from pathlib import Path

import streamlit as st

st.set_page_config(page_title="My Homepage", page_icon="🙂", layout="centered")

DEFAULT_PHOTO = Path(__file__).parent / "profile.jpg"

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
    .product-photo {
        width: 180px; height: 180px; border-radius: 16px;
        background: linear-gradient(135deg, #ffb86a, #ff6a9e);
        display: flex; align-items: center; justify-content: center;
        font-size: 4rem;
        margin: 0 auto;
    }
    .price { font-size: 1.4rem; font-weight: 700; text-align: center; margin-top: 0.5rem; }
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
    elif DEFAULT_PHOTO.exists():
        st.image(str(DEFAULT_PHOTO), width=180)
    else:
        st.markdown('<div class="avatar-placeholder">사진</div>', unsafe_allow_html=True)
        st.caption("위에서 사진을 업로드하면 프로필 사진으로 표시됩니다.")

st.markdown("---")

# ---- 자기소개 ----
st.markdown('<p class="name">홍지효</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">안녕하세요 홍지효 입니다 잘부탁드립니다</p>', unsafe_allow_html=True)

st.write("")
st.subheader("소개")
st.write(
    "여기에 자기소개 내용을 작성하세요. 어떤 일을 하고 있는지, "
    "관심 분야는 무엇인지, 어떤 사람인지 자유롭게 적어보세요."
)

st.write("")
st.subheader("연락처")
st.write("이메일: hong881100@gmail.com")

st.write("")
st.markdown("---")
st.subheader("말랑이 판매")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="product-photo">🧸</div>', unsafe_allow_html=True)
    st.caption("실제 상품 사진으로 교체 예정")

st.markdown('<p class="price">5,000원</p>', unsafe_allow_html=True)

st.write("**결제 방법**: 계좌이체 (현금)")
st.write("카카오뱅크 1111111111 (예금주: 홍지효)")
st.write("입금 확인 후 택배로 발송됩니다.")
st.caption("※ 예시로 등록된 계좌 정보입니다.")
