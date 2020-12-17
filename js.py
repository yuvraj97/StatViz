import streamlit as st


def set_cookie(name, value):
    st.markdown(f"""<div id="set-quantml-cookie" name="{name}" value="{value}"></div>""",
                unsafe_allow_html=True)
