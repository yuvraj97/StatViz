import os
from typing import Dict, Union

import streamlit as st
import SessionState
import success
from auth.utils import read_JSON
from auth.login import alreadyLoggedIn, logout_button, login
from themes import applyDarkTheme, applyLightTheme , mainStyle
from js import set_cookie, get_ID

def clear(elements):
    # print("        - clear(elements)")
    for element in elements:
        element.empty()


def initializeID(state, CURRENTLY_LOGIN_JSON):
    # print("  initializeID(state, CURRENTLY_LOGIN_JSON)")
    if state.ID is None:
        state.ID = get_ID(CURRENTLY_LOGIN_JSON)
        state.url = st.experimental_get_query_params()
        # print("        * ID: ", state.ID)
        # print("        * url: ", str(state.url))
        return
    # print("  ID already initialized!")


def main():
    LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "data", "login.json")
    CURRENTLY_LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "data", "currently-loggedin.json")
    LOGIN_JSON: Dict[str, Dict[str, Union[str, int, Dict[str, int]]]] = read_JSON(LOGIN_JSON_PATH)
    CURRENTLY_LOGIN_JSON: Dict[str, str] = read_JSON(CURRENTLY_LOGIN_JSON_PATH)
    state = SessionState.get_state()
    state.experimental_rerun = False
    state.theme = state.theme if state.theme is not None else SessionState.get_cookie("theme")
    state.isMobile = True if (SessionState.get_cookie("notDesktop") == "true") else False

    with st.sidebar.beta_expander("Settings", expanded=True if state.theme is None else False):
        if st.checkbox("Apply Dark Theme", True if state.theme == "dark" else False):
            if state.theme != "dark":
                set_cookie("theme", "dark")
            state.theme = "dark"
        else:
            if state.theme != "light":
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
    # state.SET_TOTAL_RELOADS
    # state.TOTAL_RELOADS
    # state.OTP
    # state.FIRSTOTPSENT
    # state.FIRST_INCORRECT_OTP
    # state.INCORRECT_OTP

    initializeID(state, CURRENTLY_LOGIN_JSON)

    if not state.SET_TOTAL_RELOADS:
        # print("  Initialized state.TOTAL_RELOADS = 0")
        state.SET_TOTAL_RELOADS = True
        state.TOTAL_RELOADS = 0
    state.TOTAL_RELOADS += 1

    # print(f"=====================START [{state.TOTAL_RELOADS}]=====================")
    access_granted, email = alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON)
    # print("      - RETURNED FROM alreadyLoggedIn()")
    # print("          * access_granted: ", access_granted)
    # print("          * email: ", email)
    if not access_granted:
        access_granted, email, elements = login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, True)
        # print("      - RETURNED FROM login()")
        # print("          * access_granted: ", access_granted)
        # print("          * email: ", email)
        if access_granted:
            # print("if(access_granted): ")
            state.experimental_rerun = True
    if access_granted:
        logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)

    success.main([], state)
    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    # state.sync()
    if state.experimental_rerun:
        st.experimental_rerun()
    # print(f"======================END [{state.TOTAL_RELOADS}]======================")


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
        "<h1 style='font-family:Arial;text-align:center;'><a href='https://quantml.org'>QuantML</a></h1>",
        unsafe_allow_html=True)
    st.sidebar.markdown("")
    # try:
    main()
    # except:
    #    error.markdown("""
    #    <blockquote class="error">
    #    Unexpected error Occurred please try refreshing page.
    #    <!--<span class="quant-bb">"CTRL + R"</span> or <span class="quant-bb">"F5"</span>-->
    #    </blockquote>
    #    """, unsafe_allow_html=True)
    # print("================ Statistics.py  [END]  ================")
