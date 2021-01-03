import os
import streamlit as st
from auth.resetPassword import resetPassword
from auth.utils import hashPasswd, write_JSON

LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "login.json")
CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "currently-loggedin.json")

def alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON):
    ID = state.ID
    if ID in CURRENTLY_LOGIN_JSON:
        return True, CURRENTLY_LOGIN_JSON[ID]
    else:
        return False, None

def verifyEmail(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

def initializeLogin(state, LOGIN_JSON, sidebar):
    with st.sidebar.beta_expander("Login", expanded=False) if sidebar else st.beta_expander("Login", expanded=False):
        email = st.text_input('Enter your E-mail', value="name@example.com")
        email = email.lower()

        if email == "name@example.com" or email.replace(' ', '') == "":
            pass
        elif not verifyEmail(email):
            st.markdown(f'<blockquote class="error">"<b>{email}</b>" is <b>not</b> a valid email address</blockquote>', unsafe_allow_html=True)
            return False, email
        elif email not in LOGIN_JSON:
            from auth.patreonAPI import get_patreon_data
            users = get_patreon_data()
            if email in users:
                st.markdown("""
                <blockquote class="success">
                    It's your first Login.<br>
                    So let's Create a Password.
                </blockquote>""", unsafe_allow_html=True)
                LOGIN_JSON[email] = {
                    "login": "false",
                    "pass": "None",
                    "OTP_COUNT": 0,
                    "OTP_LIMIT_REACH_TIME": {
                        "year": 0,
                        "month": 0,
                        "day": 0,
                        "hour": 0,
                        "minute": 0,
                        "second": 0
                    },
                    "ID": "None"
                }
                resetPassword(state, email, LOGIN_JSON)
            else:
                msg = f"""
                                       <b>{email}</b> is not registered as a <b><a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">patreon</a></b><br>
                                       This app is under development, once it's concluded it will be available to everyone.<br>
                                       To get <b>early access</b> to this app, <b>Join us at <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">patreon</a></b>
                                    """
                st.markdown(f'<blockquote class="warning">{msg}</blockquote>', unsafe_allow_html=True)
        elif email in LOGIN_JSON:
            if LOGIN_JSON[email]['pass'] == "None":
                st.markdown("""
                <blockquote class="success>
                    It's your first Login so let's Create a Password.
                </blockquote>""", unsafe_allow_html=True)
                resetPassword(state, email, LOGIN_JSON)
            else:
                password = st.text_input("Password", type="password")
                if password == '':
                    pass
                elif hashPasswd(password) == LOGIN_JSON[email]['pass']:
                    return True, email
                else:
                    incorrectPassword_warn = st.empty()
                    incorrectPassword_warn.warning("Incorrect Password")
                    status = st.checkbox("Reset Password")
                    if status:
                        incorrectPassword_warn.empty()
                        if resetPassword(state, email, LOGIN_JSON):
                            return True, email
    return False, email

def onLoginUpdateJSON(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    ID = state.ID
    prev_ID = LOGIN_JSON[email]["ID"]
    if prev_ID in CURRENTLY_LOGIN_JSON:
        del CURRENTLY_LOGIN_JSON[prev_ID]
    CURRENTLY_LOGIN_JSON[ID] = email
    LOGIN_JSON[email]["login"] = "true"
    LOGIN_JSON[email]["ID"] = ID

def login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, sidebar):
    access_granted, email = initializeLogin(state, LOGIN_JSON, sidebar)
    if access_granted:
        onLoginUpdateJSON(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        write_JSON(CURRENTLY_LOGIN_JSON, CURRENTLY_LOGIN_JSON_PATH)
    return access_granted, email


def logout(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    LOGIN_JSON[email]["login"] = "false"
    LOGIN_JSON[email]["ID"] = "None"
    del CURRENTLY_LOGIN_JSON[state.ID]

def logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    status = st.sidebar.button("Logout")
    if status:
        logout(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        write_JSON(CURRENTLY_LOGIN_JSON, CURRENTLY_LOGIN_JSON_PATH)
        state.experimental_rerun = True
