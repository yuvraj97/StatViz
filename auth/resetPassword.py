import os
import streamlit as st
from auth.otp import askForOTP, verifyOTP
from auth.utils import write_JSON, hashPasswd

LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "login.json")
CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "currently-loggedin.json")

def updateNewPassword(state, email, LOGIN_JSON, password):
    LOGIN_JSON[email]['pass'] = hashPasswd(password)
    write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
    state.experimental_rerun = True

def newPasswordOTPConfirmed(state, email, LOGIN_JSON):
    newPassword = st.text_input("New Password", type="password")
    confirmPassword = st.text_input("Confirm Password", type="password")
    if newPassword == "" or confirmPassword == "":
        pass
    elif newPassword != confirmPassword:
        st.markdown(f'<blockquote class="warning">Password does not match, please try again.</blockquote>', unsafe_allow_html=True)
    elif newPassword == confirmPassword:
        updateNewPassword(state, email, LOGIN_JSON, newPassword)
        st.markdown(f'<blockquote class="success">Successfully Updated Your Password</blockquote>', unsafe_allow_html=True)
        return True
    return False

def resetPassword(state, email, LOGIN_JSON):
    status, stlog = askForOTP(state, email, LOGIN_JSON)
    if status:
        if state.OTP_VERIFIED or verifyOTP(state, email, LOGIN_JSON):
            if newPasswordOTPConfirmed(state, email, LOGIN_JSON):
                return True
    else:
        st.markdown(f'<blockquote class="warning">{stlog}</blockquote>', unsafe_allow_html=True)
    return False
