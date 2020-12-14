import os
from auth.otp import askForOTP, verifyOTP
from auth.utils import write_JSON, hashPasswd
from auth.stInputs import stNewPassword,  stConfirmPassword,  stIncorrectNewPassword,  stSuccess, stResetPasswordError

LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","login.json")
CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","currently-loggedin.json")

def updateNewPassword(state, email, LOGIN_JSON, password):
    #print("\t Updating Password")
    LOGIN_JSON[email]['pass'] = hashPasswd(password)
    write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
    state.experimental_rerun = True
    #print("\t ======DONE======")
    #print("")

def newPasswordOTPConfirmed(state, email, LOGIN_JSON, sidebar, GlobalElements):
    #print("\t New Password")
    #print("\t \t OTP is verified")
    newPassword_passwd, newpasswd = stNewPassword(sidebar)
    GlobalElements.append(newPassword_passwd)
    confirmPassword_passwd, confirmpasswd = stConfirmPassword(sidebar)
    GlobalElements.append(confirmPassword_passwd)
    if(newpasswd =="" or confirmpasswd==""):
        #print("\t \t \t Password not Entered (empty)")
        pass
    elif(newpasswd != confirmpasswd):
        element = stIncorrectNewPassword(sidebar)
        GlobalElements.append(element)
        #print("\t \t \t Incorrect Password")
    elif(newpasswd == confirmpasswd):
        newPassword_passwd.empty()
        confirmPassword_passwd.empty()
        updateNewPassword(state, email, LOGIN_JSON, newpasswd)
        element = stSuccess(sidebar)
        GlobalElements.append(element)
        #print("\t \t \t Successfully Updated the Password")
        #print("\t \t \t ======DONE======")
        #print("")
        return True
    #print("\t \t \t ======FAILED======")
    #print("")
    return False

def resetPassword(state, email, LOGIN_JSON, sidebar, GlobalElements):
    #print("\t Reset Password")
    #print("OTP_COUNT",LOGIN_JSON[email]["OTP_COUNT"])
    status, stlog = askForOTP(state, email, LOGIN_JSON)
    #print("OTP_COUNT",LOGIN_JSON[email]["OTP_COUNT"])
    if(status):
        if(LOGIN_JSON[email]["OTP_VERIFICATION_ID"] == state.ID or verifyOTP(state, email, LOGIN_JSON, sidebar, GlobalElements)):
            if(newPasswordOTPConfirmed(state, email, LOGIN_JSON, sidebar, GlobalElements)):
                return True
    else:
        element = stResetPasswordError(stlog, sidebar)
        GlobalElements.append(element)
    #print("")
    return False