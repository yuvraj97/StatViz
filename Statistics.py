import os
import streamlit as st
import numpy as np
import SessionState
import success
from auth.utils import read_JSON
from auth.login import alreadyLoggedIn, logout_button, login

def clear(elements):
    #print("        - clear(elements)")
    for element in elements:
        element.empty()

def initializeID(state, CURRENTLY_LOGIN_JSON):
    #print("  initializeID(state, CURRENTLY_LOGIN_JSON)")
    if state.ID == None:
        state.ID = "123kjgg4"#SessionState.get_ID()
        state.url = st.experimental_get_query_params()
        #print("        * ID: ", state.ID)
        #print("        * url: ", str(state.url))
        return
    #print("  ID already initialized!")


def main(GlobalElements):
    LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","login.json")
    CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","currently-loggedin.json")
    LOGIN_JSON = read_JSON(LOGIN_JSON_PATH)
    CURRENTLY_LOGIN_JSON = read_JSON(CURRENTLY_LOGIN_JSON_PATH)
    state = SessionState.get_state()
    state.experimental_rerun = False

    #state.ID_TAKEN
    #state.ID
    #state.SET_TOTAL_RELOADS
    #state.TOTAL_RELOADS
    #state.OTP
    #state.FIRSTOTPSENT
    #state.FIRST_INCORRECT_OTP
    #state.INCORRECT_OTP

    initializeID(state, CURRENTLY_LOGIN_JSON)
    
    if(state.SET_TOTAL_RELOADS!=True):
        #print("  Initialized state.TOTAL_RELOADS = 0")
        state.SET_TOTAL_RELOADS = True
        state.TOTAL_RELOADS = 0
    state.TOTAL_RELOADS += 1
    
    #print(f"=====================START [{state.TOTAL_RELOADS}]=====================")
    access_granted, email = alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON)
    #print("      - RETURNED FROM alreadyLoggedIn()")
    #print("          * access_granted: ", access_granted)
    #print("          * email: ", email)
    elements = []
    if(not access_granted):
        access_granted, email, elements = login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, True, GlobalElements)
        #print("      - RETURNED FROM login()")
        #print("          * access_granted: ", access_granted)
        #print("          * email: ", email)
        if(access_granted): state.experimental_rerun = True
    if(access_granted):
        logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON, GlobalElements)

    success.main([],email, state, GlobalElements)
    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    #state.sync()
    if(state.experimental_rerun): 
        st.experimental_rerun()
    #print(f"======================END [{state.TOTAL_RELOADS}]======================")

if __name__ == '__main__':
    #print("================ Statistics.py [START] ================")
    GlobalElements = []
    st.sidebar.title("[QuantML](https://quantml.org)")
    #try:
    main(GlobalElements)
    #except:
    #    clear(GlobalElements)
    #    st.error("""Unexpected error Occured please try refreshing page "CTRL + R" of "F5"     
    #    If problem still there please contact **support@quantml.org**
    #    """)
    #print("================ Statistics.py  [END]  ================")