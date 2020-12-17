import streamlit as st
import SessionState
def initialize():
    st.write(222)
    st.sidebar.markdown("""
    <div id="set-quantml-cookie" name="theme" value="light"></div>
    """, unsafe_allow_html=True)

def set_cookie(name, value):
    st.markdown(f"""<div id="set-quantml-cookie" name="{name}" value="{value}"></div>""", 
    unsafe_allow_html=True)

st.write(SessionState.get_cookie('theme'))