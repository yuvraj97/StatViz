import os
import streamlit as st
from auth.resetPassword import resetPassword
from auth.utils import hashPasswd, write_JSON

LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "login.json")
CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data", "currently-loggedin.json")


def alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON):
    # print("\t Checking If already Logged in")
    ID = state.ID
    if ID in CURRENTLY_LOGIN_JSON:
        # print("\t \t Already Logged in")
        return True, CURRENTLY_LOGIN_JSON[ID]
    else:
        # print("\t \t NOT Already Logged in")
        return False, None
    # print("\t ======DONE======")
    # print("")


def verifyEmail(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False


def initializeLogin(state, LOGIN_JSON, sidebar):
    # print("\t Login...")
    elements = []
    with st.sidebar.beta_expander("Login", expanded=False) if (sidebar) else st.beta_expander("Login", expanded=False):
        email = st.text_input('Enter your E-mail', value="name@example.com")
        email = email.lower()

        if email == "name@example.com" or email.replace(' ', '') == "":
            # print("\t \t Email not set (empty)")
            # print("\t \t ======Failed======")
            pass
        elif not verifyEmail(email):
            # print("\t \t Invalid Email Address")
            st.error(f'"**{email}**" is **not** a valid email address')
            return False, email, elements

        elif email not in LOGIN_JSON:
            # print(f"\t \t {email} is not in our data base")
            # element = stEmpty()
            # element.error('''**'''+ email + """**
            #            is not registered as a **[patreon](https://www.patreon.com/quantml)**
            #            This app is under development, it's not finalized yet.
            #            To get **early access** to this app, **Join us at [patreon](https://www.patreon.com/quantml)**
            #        """)
            msg = f"""
                       **{email}** is not registered as a **[patreon](https://www.patreon.com/quantml) !**    
                       This app is under development, once it's concluded it will br available to everyone.       
                       To get **early access** to this app, **Join us at [patreon](https://www.patreon.com/quantml)**
                    """
            st.warning(msg)
            # print("\t \t ======Failed======")
        elif email in LOGIN_JSON:
            # print(f"\t \t {email} is a verified email address")
            if LOGIN_JSON[email]['pass'] == "None":
                st.header("Create Password")
                resetPassword(state, email, LOGIN_JSON, sidebar)
            else:
                password = st.text_input("Password", type="password")
                # print(password)
                if password == '':
                    # print("\t \t \t password field is (empty)")
                    # print("\t \t \t ======Failed======")
                    pass
                elif hashPasswd(password) == LOGIN_JSON[email]['pass']:
                    # print("\t \t \t password Matched")
                    # print("\t \t \t ======DONE======")
                    # print("")
                    return True, email, elements
                else:
                    # print("\t \t \t password didn't Match")
                    incorrectPassword_warn = st.empty()
                    incorrectPassword_warn.warning("Incorrect Password")
                    status = st.checkbox("Reset Password")
                    if status:
                        # print("\t \t \t \t Reseting password...")
                        incorrectPassword_warn.empty()
                        if resetPassword(state, email, LOGIN_JSON, sidebar):
                            return True, email, elements
        # print("")
    return False, email, elements


def onLoginUpdateJSON(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    # print("\t Updating Database")
    ID = state.ID

    prev_ID = LOGIN_JSON[email]["ID"]
    if (prev_ID in CURRENTLY_LOGIN_JSON):
        del CURRENTLY_LOGIN_JSON[prev_ID]
    CURRENTLY_LOGIN_JSON[ID] = email

    LOGIN_JSON[email]["login"] = "true"
    LOGIN_JSON[email]["ID"] = ID
    # print("\t ======DONE======")
    # print("")


def login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, sidebar):
    access_granted, email, elements = initializeLogin(state, LOGIN_JSON, sidebar)
    if (access_granted):
        onLoginUpdateJSON(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        write_JSON(CURRENTLY_LOGIN_JSON, CURRENTLY_LOGIN_JSON_PATH)
    return access_granted, email, elements


def logout(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    # print(f"\t logout {email}")
    LOGIN_JSON[email]["login"] = "false"
    LOGIN_JSON[email]["ID"] = "None"
    del CURRENTLY_LOGIN_JSON[state.ID]
    # print("\t ======DONE======")
    # print("")


def logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    status = st.sidebar.button("Logout")
    if (status):
        logout(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        write_JSON(CURRENTLY_LOGIN_JSON, CURRENTLY_LOGIN_JSON_PATH)
        state.experimental_rerun = True
