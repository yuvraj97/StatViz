import streamlit as st
import SessionState
def set_cookie(name, value):
    st.markdown(f"""<div id="set-quantml-cookie" name="{name}" value="{value}"></div>""", 
    unsafe_allow_html=True)