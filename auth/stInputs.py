import streamlit as st


def stEmpty(sidebar=False):
    if (sidebar):
        element = st.sidebar.empty()
    else:
        element = st.empty()
    return element


def stWrite(msg, sidebar=False):
    if (sidebar):
        element = st.sidebar.empty()
    else:
        element = st.empty()
    element.write(msg)
    return element


def stSelectbox(label, options, index, sidebar=False):
    if (sidebar):
        element = st.sidebar.empty()
    else:
        element = st.empty()
    option = element.selectbox(label, options, index)
    return element, option


def stNumberInput(msg, min_value, max_value, value, sidebar):
    if (sidebar):
        element = st.sidebar.empty()
    else:
        element = st.empty()
    value = element.number_input(msg, min_value, max_value, value)
    return element, value


def stSlider(msg, min_value, max_value, value, step, sidebar):
    if (sidebar):
        element = st.sidebar.empty()
    else:
        element = st.empty()
    element.slider(msg, min_value, max_value, value, step)
    return element, value


def stLogoutButton():
    element = st.sidebar.empty()
    status = element.button("Logout")
    return element, status


############################## resetPassword.py ##############################

def stNewPassword(sidebar):
    if (sidebar):
        newPassword_passwd = st.sidebar.empty()
    else:
        newPassword_passwd = st.empty()
    newpasswd = newPassword_passwd.text_input("New Password", type="password")
    return newPassword_passwd, newpasswd


def stConfirmPassword(sidebar):
    if (sidebar):
        confirmPassword_passwd = st.sidebar.empty()
    else:
        confirmPassword_passwd = st.empty()
    confirmpasswd = confirmPassword_passwd.text_input("Confirm Password", type="password")
    return confirmPassword_passwd, confirmpasswd


def stIncorrectNewPassword(sidebar):
    msg = """
             Password doesn't match please enter again.
          """
    if (sidebar):
        incorrectNewPassword_warn = st.sidebar.empty()
    else:
        incorrectNewPassword_warn = st.empty()
    incorrectNewPassword_warn.warning(msg)
    return incorrectNewPassword_warn


def stSuccess(sidebar):
    msg = "Successfully Updated Your Password"
    if (sidebar):
        success = st.sidebar.empty()
    else:
        success = st.empty()
    success.success(msg)
    return success


def stResetPasswordError(stlog, sidebar):
    if (sidebar):
        reset_password_error = st.sidebar.empty()
    else:
        reset_password_error = st.empty()
    reset_password_error.warning(stlog)
    return reset_password_error


############################## otp.py ##############################

def stOTPHeaderInfo(msg, sidebar):
    if (sidebar):
        otpHeader_info = st.sidebar.empty()
    else:
        otpHeader_info = st.empty()
    otpHeader_info.info(msg)
    return otpHeader_info


def stEnterOTP(sidebar):
    if (sidebar):
        enter_OTP_txt = st.sidebar.empty()
    else:
        enter_OTP_txt = st.empty()
    enteredOTP = enter_OTP_txt.text_input("Enter OTP")
    return enter_OTP_txt, enteredOTP


def stIncorrectOTPError(incorrectOTPText, sidebar):
    if (sidebar):
        incorrectOTP_err = st.sidebar.empty()
    else:
        incorrectOTP_err = st.empty()
    incorrectOTP_err.error(incorrectOTPText)
    return incorrectOTP_err


def stUnknownOTPError(sidebar):
    if (sidebar):
        error = st.sidebar.empty()
    else:
        error = st.empty()
    error.error("Unknown Error Occurred!")
    return error

##############################  ##############################
