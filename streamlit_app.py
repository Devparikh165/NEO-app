import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://www.popsci.com/uploads/2022/10/31/NearEarthObject_40085801.jpg?auto=webp&width=1440&height=1080")
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Near Earth Object")
