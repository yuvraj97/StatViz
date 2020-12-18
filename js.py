import streamlit as st
from uuid import uuid4
from SessionState import get_cookie


def set_cookie(name, value):
    print("set_cookie:: ", name, " : ", value)
    st.markdown(f"""<div id="set-quantml-cookie" name="{name}" value="{value}"></div>""",
                unsafe_allow_html=True)


def get_ID(CURRENTLY_LOGIN_JSON):
    quantml_id = get_cookie("quantml-ID")
    if quantml_id is not None: return quantml_id
    quantml_id = uuid4()
    while quantml_id in CURRENTLY_LOGIN_JSON:
        quantml_id = uuid4()
    set_cookie("quantml-ID", quantml_id)
    return quantml_id
