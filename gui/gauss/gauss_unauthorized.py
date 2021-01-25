from typing import Dict, Union
import streamlit as st
import os
from auth.utils import read_JSON
from auth.login import login

LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "..", "app-data", "app-login.json")
CURRENTLY_LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "..", "app-data", "app-currently-loggedin.json")
LOGIN_JSON: Dict[str, Dict[str, Union[str, int, Dict[str, int]]]] = read_JSON(LOGIN_JSON_PATH)
CURRENTLY_LOGIN_JSON: Dict[str, str] = read_JSON(CURRENTLY_LOGIN_JSON_PATH)

def main(state):
    access_granted, email = login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, False, login_heading="Login is required")
    if access_granted:
        # st.balloons()
        state.experimental_rerun = True

    st.markdown(f"""
    <blockquote class="warning">
        This app is under development so currently
        <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">patreons</a>
        that opt for Statistics App, are able to access all upcoming visualizations.<br>
        Once this Statistics App is concluded plan is to make all visualizations of this Statistics App to be available
        to everyone.<br>
        If you wish to support my work
        <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">Join us on patreon</a>,
        also opt for Statistics App to get access to all of the upcoming visualizations.<br>
    </blockquote>""", unsafe_allow_html=True)
    st.markdown("""Hope you enjoyed the app so far, now our next step is to eliminate <b>most</b> of our doubts regarding the 
    beauty of <b>Gaussian Distribution</b>.<br>
    When it came to Gaussian Distribution, what is the first thing that came into mind
    <a rel='noreferrer' target='_blank' href="https://read.quantml.org/statistics/central-limit-theorem/.">Central Limit Theorem</a>
    right.<br>
    In this section we will see some simulations and see how they results in a
    <a rel='noreferrer' target='_blank' href="https://read.quantml.org/statistics/gaussian-distribution/.">
    Gaussian Distribution</a>.<br>
    """, unsafe_allow_html=True)
    st.markdown("""
    Here we will simulate,    
    - Random walk $1\\text{D}$
    - Random walk $2\\text{D}$
    - Multiple Die Rolls
    """)
