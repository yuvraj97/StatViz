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
    cover_img = st.sidebar.empty()
    LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "..", "app-data", "app-login.json")
    CURRENTLY_LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "..", "app-data", "app-currently-loggedin.json")
    LOGIN_JSON: Dict[str, Dict[str, Union[str, int, Dict[str, int]]]] = read_JSON(LOGIN_JSON_PATH)
    CURRENTLY_LOGIN_JSON: Dict[str, str] = read_JSON(CURRENTLY_LOGIN_JSON_PATH)
    state.experimental_rerun = False
    state.url = state.url if state.url is not None else st.experimental_get_query_params()
    theme = SessionState.get_cookie("theme")
    if theme == "":
        return "first-load-failed"
    state.theme = state.theme if state.theme is not None else theme
    state.isMobile = True if (SessionState.get_cookie("notDesktop") == "true") else False

    with st.sidebar.beta_expander("Settings", expanded=True if state.theme is None else False):
        if st.checkbox("Apply Dark Theme", True if state.theme == "dark" else False):
            set_cookie("theme", "dark")  # Don't rerun to set cookies
            state.theme = "dark"
        else:
            set_cookie("theme", "light")  # Don't rerun to set cookies
            state.theme = "light"

        # noinspection PyUnresolvedReferences
        state.stSettings = {
            "seed-checkbox": st.empty() if state.stSettings is None else state.stSettings["seed-checkbox"],
            "seed-number": st.empty() if state.stSettings is None else state.stSettings["seed-number"],
            "seed": None if state.stSettings is None else state.stSettings["seed"],
            "logout": st.empty() if state.stSettings is None else state.stSettings["logout"]
        }

    cover_img.markdown(f"""
        <br><br>
        <a rel='noreferrer' target='_blank' href="https://www.quantml.org/"><img src="/{"img-dark" if state.theme == "dark" else "img"}/cover.webp" alt="QuantML" width="100%"></a><br>
        <br>""", unsafe_allow_html=True)

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
    #
    # initializeID(CURRENTLY_LOGIN_JSON)
    #
    # access_granted, email = alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON)
    # if not access_granted:
    #     access_granted, email = login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, True)
    #     if access_granted:
    #         # st.balloons()
    #         state.experimental_rerun = True
    # if access_granted:
    #     logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
    #     state.isLoggedIn = True
    #     state.email = email
    #     success.main(state, True)
    # else: success.main(state, False)
    success.main(state, True)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    # state.sync()
    if state.experimental_rerun:
        st.experimental_rerun()

if __name__ == '__main__':
    st.set_page_config(
        layout='centered',
        initial_sidebar_state='expanded'
    )
    error = st.empty()
    mainStyle()
    # print("================ Statistics.py [START] ================")

    state = SessionState.get_state()
    # if state.experimental_rerun_main is None:
    #     state.experimental_rerun_main = True

    # noinspection PyBroadException
    try:
        status = main()
        if status == "first-load-failed":
            st.info("Initializing...")
            import streamlit.components.v1 as components
            components.html("<script>parent.document.location.reload()</script>", height=0, width=0)
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
    # # print("================ Statistics.py  [END]  ================")
