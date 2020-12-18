import streamlit as st
from uuid import uuid4
from SessionState import get_cookie

def set_cookie(name, value):
    print("set_cookie:: ", name, " : ", value)
    st.markdown(f"""<div id="set-quantml-cookie" name="{name}" value="{value}"></div>""",
                unsafe_allow_html=True)

def get_ID(CURRENTLY_LOGIN_JSON):
    id = get_cookie("quantml-ID")
    if id is not None: return id
    id = uuid4()
    while id in CURRENTLY_LOGIN_JSON:
        id = uuid4()
    set_cookie("quantml-ID", id)
    return id