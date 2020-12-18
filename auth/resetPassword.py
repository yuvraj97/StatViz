import os
import streamlit as st
from auth.otp import askForOTP, verifyOTP
from auth.utils import write_JSON, hashPasswd

LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "login.json")
CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "currently-loggedin.json")


def updateNewPassword(state, email, LOGIN_JSON, password):
    # print("\t Updating Password")
    LOGIN_JSON[email]['pass'] = hashPasswd(password)
    write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
    state.experimental_rerun = True
    # print("\t ======DONE======")
    # print("")


def newPasswordOTPConfirmed(state, email, LOGIN_JSON):
    # print("\t New Password")
    # print("\t \t OTP is verified")
    newPassword = st.text_input("New Password", type="password")
    confirmPassword = st.text_input("Confirm Password", type="password")
    if newPassword == "" or confirmPassword == "":
        # print("\t \t \t Password not Entered (empty)")
        pass
    elif newPassword != confirmPassword:
        st.warning("Password doesn't match please enter again.")
        # print("\t \t \t Incorrect Password")
    elif newPassword == confirmPassword:
        updateNewPassword(state, email, LOGIN_JSON, newPassword)
        st.success("Successfully Updated Your Password")
        # print("\t \t \t Successfully Updated the Password")
        # print("\t \t \t ======DONE======")
        # print("")
        return True
    # print("\t \t \t ======FAILED======")
    # print("")
    return False


def resetPassword(state, email, LOGIN_JSON):
    # print("\t Reset Password")
    # print("OTP_COUNT",LOGIN_JSON[email]["OTP_COUNT"])
    status, stlog = askForOTP(state, email, LOGIN_JSON)
    # print("OTP_COUNT",LOGIN_JSON[email]["OTP_COUNT"])
    if status:
        if state.OTP_VERIFIED or verifyOTP(state, email, LOGIN_JSON):
            if newPasswordOTPConfirmed(state, email, LOGIN_JSON):
                return True
    else:
        st.warning(stlog)
    # print("")
    return False
