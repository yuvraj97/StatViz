import os
import streamlit as st
from datetime import datetime
from auth.utils import write_JSON, sendOTP

LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "..", "app-data", "app-login.json")
CURRENTLY_LOGIN_JSON_PATH: str = os.path.join(os.getcwd(), "..", "app-data", "app-currently-loggedin.json")

def askForOTP(state, email, LOGIN_JSON):
    if LOGIN_JSON[email]["OTP_COUNT"] <= 3:
        return True, None
    if LOGIN_JSON[email]["OTP_COUNT"] == 4:
        LOGIN_JSON[email]["OTP_COUNT"] += 1
        time = datetime.now().replace(microsecond=0)
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["year"] = time.year
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["month"] = time.month
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["day"] = time.day
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["hour"] = time.hour
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["minute"] = time.minute
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["second"] = time.second
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        stlog = """
                    You have exceeded the limit.<br>
                    Now you need to wait for <b>30 minutes</b> to request for another OTP.<br>    
                    <i>(Rerun to update the time)</i>
                 """
        return False, stlog
    if LOGIN_JSON[email]["OTP_COUNT"] == 5:
        otp_exceed_time = datetime(
            LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["year"],
            LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["month"],
            LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["day"],
            LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["hour"],
            LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["minute"],
            LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["second"]
        )
        now = datetime.now().replace(microsecond=0)
        diff = now - otp_exceed_time
        if diff.seconds <= 1800:
            stlog = f"""
                        You have exceeded the limit.<br>    
                        You can request for another OTP after <b>{"{:.2f}".format((1800 - diff.seconds) / 60)} minutes</b>.<br>
                        <i>(Rerun to update the time)</i>
                    """
            return False, stlog
        else:
            LOGIN_JSON[email]["OTP_COUNT"] = 0
            write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
            state.FIRSTOTPSENT = None
            state.FIRST_INCORRECT_OTP = None
            # PASS, Now user can get OTP
            return True, None

def verifyOTP(state, email, LOGIN_JSON):
    otpHeader_info = st.empty()
    otpHeader_info.info(f"""An OTP ({LOGIN_JSON[email]["OTP_COUNT"]}/3) is sent over *{email}* also check the **Spam folder**""")
    stEnterOTP = st.empty()
    enteredOTP = stEnterOTP.text_input("Enter OTP")

    # 2nd condition is used to stop sending 2 OTP
    if enteredOTP == "" or enteredOTP == state.INCORRECT_OTP:
        if state.FIRSTOTPSENT is None:
            msg = f"""An OTP ({LOGIN_JSON[email]["OTP_COUNT"] + 1}/3) is sent over *{email}* also check the **Spam folder**"""
            otpHeader_info.info(msg)
            state.FIRSTOTPSENT = True
            state.OTP = str(sendOTP(state, email))
            LOGIN_JSON[email]["OTP_COUNT"] += 1
            write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        if state.FIRST_INCORRECT_OTP:
            otpHeader_info.empty()
            incorrectOTPText = f"""
                        OTP is incorrect!<br>
                        Another OTP ({LOGIN_JSON[email]["OTP_COUNT"]}/3) is sent over <i>{email}</i> also check the <b>Spam folder</b>.
                    """
            st.markdown(f'<blockquote class="error">{incorrectOTPText}</blockquote>', unsafe_allow_html=True)
    elif state.OTP != enteredOTP:
        state.INCORRECT_OTP = enteredOTP
        if state.FIRST_INCORRECT_OTP is None:
            state.FIRST_INCORRECT_OTP = True
        otpHeader_info.empty()
        incorrectOTPText = f"""
                        OTP is incorrect!<br>
                        Another OTP ({LOGIN_JSON[email]["OTP_COUNT"] + 1}/3) is sent over <i>{email}</i> also check the <b>Spam folder</b>.
                    """
        st.markdown(f'<blockquote class="error">{incorrectOTPText}</blockquote>', unsafe_allow_html=True)
        state.OTP = str(sendOTP(state, email))
        LOGIN_JSON[email]["OTP_COUNT"] += 1
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
    elif state.OTP == enteredOTP:
        stEnterOTP.empty()
        otpHeader_info.empty()
        LOGIN_JSON[email]["OTP_COUNT"] = 0
        state.OTP_VERIFIED = True
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        state.FIRSTOTPSENT = None
        state.FIRST_INCORRECT_OTP = None
        return True
    else:
        st.markdown(f'<blockquote class="error">Unknown Error Occurred!</blockquote>', unsafe_allow_html=True)
    return False
