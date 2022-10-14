import streamlit as st

readme = open("README.md", 'r')
st.markdown(readme.read(), unsafe_allow_html=True)
readme.close()