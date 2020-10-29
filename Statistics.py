import os
import streamlit as st
import numpy as np
import SessionState
import success
from auth.utils import read_JSON
from auth.login import alreadyLoggedIn, logout_button, login

def clear(elements):
    for element in elements:
        element.empty()

def initializeID(state, CURRENTLY_LOGIN_JSON):
    if state.ID_TAKEN == None:
        print("Initializing ID")
        state.ID_TAKEN = True
        for i in range(100):
            #print(f"itter: {i}")
            state.ID = str(np.random.randint(0,2147483646))
            if(state.ID not in CURRENTLY_LOGIN_JSON):
                break


def main(GlobalElements):
    LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","login.json")
    CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","currently-loggedin.json")
    LOGIN_JSON = read_JSON(LOGIN_JSON_PATH)
    CURRENTLY_LOGIN_JSON = read_JSON(CURRENTLY_LOGIN_JSON_PATH)
    state = SessionState.get_state()
       
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
        state.SET_TOTAL_RELOADS = True
        state.TOTAL_RELOADS = 0
    state.TOTAL_RELOADS += 1
    
    print(f"=====================START [{state.TOTAL_RELOADS}]=====================")
    access_granted, email = alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON)
    elements = []
    if(not access_granted):
        access_granted, email, elements = login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, True, GlobalElements)
    if(access_granted):
        st.sidebar.info('''Don\'t refresh this page   
                           Use "R" to rerun''')
        logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON, GlobalElements)

    success.main([],email, state, GlobalElements)
    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()
    print(f"======================END [{state.TOTAL_RELOADS}]======================")

if __name__ == '__main__':
    GlobalElements = []
    st.sidebar.title("[QuantML](https://quantml.org)")
    #try:
    main(GlobalElements)
    #except:
    #    clear(GlobalElements)
    #    st.error("""Unexpected error Occured please try refreshing page "CTRL + R" of "F5"     
    #    If problem still there please contact **support@quantml.org**
    #    """)