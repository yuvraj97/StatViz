import os
from auth.resetPassword import resetPassword
from auth.utils import hashPasswd, write_JSON
from auth.stInputs import stLoginTitle, stLoginEmail, stLoginPasswordTitle, stLoginPassword, stLoginIncorrectPassword, stLoginResetPassword, stLoginIncorrectEmail, stLoginInvalidEmail, stLogoutButton

LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","login.json")
CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","currently-loggedin.json")

def alreadyLoggedIn(state, CURRENTLY_LOGIN_JSON):
    #print("\t Checking If already Logged in")
    ID = state.ID
    if ID in CURRENTLY_LOGIN_JSON:
        #print("\t \t Already Logged in")
        return True, CURRENTLY_LOGIN_JSON[ID]
    else:
        #print("\t \t NOT Already Logged in")
        return False, None
    #print("\t ======DONE======")
    #print("")

def verifyEmail(email):
    if('@' in email and '.' in email):
        return True
    else:
        return False

def initializeLogin(state, LOGIN_JSON, sidebar, GlobalElements):
    #print("\t Login...")
    elements = []
    element = stLoginTitle(sidebar)
    elements.append(element)
    GlobalElements.append(element)
    
    email_txt, email = stLoginEmail(sidebar)
    elements.append(email_txt)
    GlobalElements.append(email_txt)
    email = email.lower()
    
    if email == "name@example.com" or email.replace(' ','') == "":
        #print("\t \t Email not set (empty)")
        #print("\t \t ======Failed======")
        pass
    elif(not verifyEmail(email)):
        #print("\t \t Invalid Email Address")
        element = stLoginInvalidEmail(f'"**{email}**" is **not** a valid email address', sidebar)
        GlobalElements.append(element)
        return False, email, elements

    elif email  not in LOGIN_JSON:
        #print(f"\t \t {email} is not in our data base")
        #element = stEmpty()
        #element.error('''**'''+ email + """**
        #            is not registered as a **[patreon](https://www.patreon.com/quantml)**    
        #            This app is under development, it's not finalized yet.    
        #            To get **early access** to this app, **Join us at [patreon](https://www.patreon.com/quantml)**
        #        """)
        msg  =  f"""
                    **{email}** is not registered as a *developer*.    
                    This app is under development so only *developer* can access it.   
                    It will soon be publicly available.
                """
        element = stLoginIncorrectEmail(msg, sidebar)
        elements.append(element)
        GlobalElements.append(element)
        #print("\t \t ======Failed======")
    elif email in LOGIN_JSON:
        #print(f"\t \t {email} is a verified email address")
        if(LOGIN_JSON[email]['pass'] == "None"):
            element = stLoginPasswordTitle("Create Password", sidebar)
            elements.append(element)
            GlobalElements.append(element)
            resetPassword(state, email, LOGIN_JSON, sidebar, GlobalElements)
        else:
            #elements.append(stLoginPasswordTitle("Password", sidebar))
            passwd_txt, password = stLoginPassword(sidebar)
            GlobalElements.append(passwd_txt)
            #print(password)
            elements.append(passwd_txt)
            if(password == ''):
                #print("\t \t \t password field is (empty)")
                #print("\t \t \t ======Failed======")
                pass
            elif(hashPasswd(password) == LOGIN_JSON[email]['pass']):
                #print("\t \t \t password Matched")
                #print("\t \t \t ======DONE======")
                #print("")
                return True, email, elements
            else:
                #print("\t \t \t password didn't Match")
                incorrectPassword_warn = stLoginIncorrectPassword(sidebar)
                GlobalElements.append(incorrectPassword_warn)
                resetPassword_check, status = stLoginResetPassword(sidebar)
                GlobalElements.append(resetPassword_check)
                elements.append(resetPassword_check)
                if(status):
                    #print("\t \t \t \t Reseting password...")
                    incorrectPassword_warn.empty()
                    if(resetPassword(state, email, LOGIN_JSON, sidebar, GlobalElements)):
                        return True, email, elements
    #print("")
    return False, email, elements

def onLoginUpdateJSON(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    #print("\t Updating Database")
    ID = state.ID
    
    prev_ID = LOGIN_JSON[email]["ID"]
    if(prev_ID in CURRENTLY_LOGIN_JSON):
        del CURRENTLY_LOGIN_JSON[prev_ID]
    CURRENTLY_LOGIN_JSON[ID] = email
    
    LOGIN_JSON[email]["login"] = "true"
    LOGIN_JSON[email]["ID"]    =  ID
    #print("\t ======DONE======")
    #print("")  

def login(state, LOGIN_JSON, CURRENTLY_LOGIN_JSON, sidebar, GlobalElements):
    access_granted, email, elements = initializeLogin(state, LOGIN_JSON, sidebar, GlobalElements)
    if(access_granted):
        onLoginUpdateJSON(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        write_JSON(CURRENTLY_LOGIN_JSON, CURRENTLY_LOGIN_JSON_PATH)
    return access_granted, email, elements

def logout(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON):
    #print(f"\t logout {email}")
    LOGIN_JSON[email]["login"]  = "false"
    LOGIN_JSON[email]["ID"]   = "None"
    del CURRENTLY_LOGIN_JSON[state.ID]
    #print("\t ======DONE======")
    #print("")

def logout_button(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON, GlobalElements):
    element, status = stLogoutButton()
    GlobalElements.append(element)
    if(status):
        logout(state, email, LOGIN_JSON, CURRENTLY_LOGIN_JSON)
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        write_JSON(CURRENTLY_LOGIN_JSON, CURRENTLY_LOGIN_JSON_PATH)
        state.experimental_rerun = True