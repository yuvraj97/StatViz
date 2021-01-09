import os
from typing import Dict, Union
import streamlit as st
import SessionState
import success
from auth.login import alreadyLoggedIn, logout_button, login
from auth.utils import read_JSON
from js import set_cookie, get_ID
from themes import applyDarkTheme, applyLightTheme, mainStyle


def initializeID(CURRENTLY_LOGIN_JSON):
    if state.ID is None:
        state.ID = get_ID(CURRENTLY_LOGIN_JSON)
        state.url = st.experimental_get_query_params()
        return

def main():
    LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "data", "login.json")
    CURRENTLY_LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "data", "currently-loggedin.json")
    LOGIN_JSON: Dict[str, Dict[str, Union[str, int, Dict[str, int]]]] = read_JSON(LOGIN_JSON_PATH)
    CURRENTLY_LOGIN_JSON: Dict[str, str] = read_JSON(CURRENTLY_LOGIN_JSON_PATH)
    state.experimental_rerun = False
    state.theme = state.theme if state.theme is not None else SessionState.get_cookie("theme")
    state.isMobile = True if (SessionState.get_cookie("notDesktop") == "true") else False

    with st.sidebar.beta_expander("Settings", expanded=True if state.theme is None else False):
        if st.checkbox("Apply Dark Theme", True if state.theme == "dark" else False):
            if state.theme != "dark":  # Theme Changed to dark
                state.experimental_rerun = True
                set_cookie("theme", "dark")
            state.theme = "dark"
        else:
            if state.theme != "light":  # Theme Changed to light
                state.experimental_rerun = True
                set_cookie("theme", "light")
            state.theme = "light"
        state.stSettings = {
            "seed-checkbox": st.empty(),
            "seed-number": st.empty(),
            "seed": None
        }

    if state.theme == "dark":
        applyDarkTheme()
    else:
        applyLightTheme()

    # state.ID_TAKEN
    # state.ID
    # state.OTP
    # state.FIRSTOTPSENT
    # state.FIRST_INCORRECT_OTP
    # state.INCORRECT_OTP

    initializeID(CURRENTLY_LOGIN_JSON)

    access_granted, email = alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON)
    if not access_granted:
        access_granted, email = login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, True)
        if access_granted:
            # st.balloons()
            state.experimental_rerun = True
    if access_granted:
        logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
        state.isLoggedIn = True
        state.email = email

    success.main(state)
    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    # state.sync()
    if state.experimental_rerun:
        st.experimental_rerun()

if __name__ == '__main__':
    st.set_page_config(
        # page_title="Statistics App - QuantML", 
        layout='centered',
        initial_sidebar_state='expanded'
    )
    error = st.empty()
    mainStyle()
    # print("================ Statistics.py [START] ================")
    st.sidebar.markdown(
        "<h1 style='font-family:Arial;text-align:center;'><a rel='noreferrer' target='_blank' href='https://quantml.org'>QuantML</a></h1><br>",
        unsafe_allow_html=True)

    state = SessionState.get_state()
    if state.experimental_rerun_main is None:
        state.experimental_rerun_main = True

    # noinspection PyBroadException
    try:
        main()
        state.experimental_rerun_main = True
    except Exception:
        if state.experimental_rerun_main:
            state.experimental_rerun_main = False
            st.experimental_rerun()
        error.markdown("""
        <blockquote class="error">
        Unexpected error occurred please <b>try refreshing page</b>.
        <!--<span class="quant-bb">"CTRL + R"</span> or <span class="quant-bb">"F5"</span>-->
        </blockquote>
        """, unsafe_allow_html=True)
    # print("================ Statistics.py  [END]  ================")
