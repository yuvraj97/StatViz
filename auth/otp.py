import os
from datetime import datetime
from auth.utils import write_JSON, sendOTP
from auth.stInputs import stOTPHeaderInfo, stEnterOTP,  stIncorrectOTPError, stUnknownOTPError

LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","login.json")
CURRENTLY_LOGIN_JSON_PATH = os.path.join(os.getcwd(), "data","currently-loggedin.json")

def askForOTP(state, email, LOGIN_JSON):
    if(LOGIN_JSON[email]["OTP_COUNT"] <= 3):
        return True, None
    if(LOGIN_JSON[email]["OTP_COUNT"] == 4):
        print("\t \t OTP Limit Reached 3 !!!")
        LOGIN_JSON[email]["OTP_COUNT"] += 1
        time = datetime.now().replace(microsecond=0)
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"][ "year" ] = time.year
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"][ "month"] = time.month
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"][  "day" ] = time.day
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"][ "hour" ] = time.hour
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["minute"] = time.minute
        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["second"] = time.second
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        stlog = """
                    You have exceeded the limit.    
                    Now you need to wait for **30 minutes** to request for another OTP.    
                    *(Rerun to update the time)*
                 """
        print("\t \t ======FAILED======")
        return False, stlog
    if(LOGIN_JSON[email]["OTP_COUNT"] == 5):
        print("\t \t OTP Limit Reached 4 !!!")
        otp_exceed_time =  datetime(
                                        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["year"],
                                        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["month"],
                                        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["day"],
                                        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["hour"],
                                        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["minute"],
                                        LOGIN_JSON[email]["OTP_LIMIT_REACH_TIME"]["second"]
                                    )
        now = datetime.now().replace(microsecond=0)
        diff = now - otp_exceed_time
        if(diff.seconds <= 1800):
            print("\t \t \t OTP LIMIT TIMEOUT <=1800 !")
            stlog = f"""
                        You have exceeded the limit.    
                        You can request for another OTP after **{"{:.2f}".format((1800 - diff.seconds)/60)} minutes**.    
                        *(Rerun to update the time)*
                    """
            print("\t \t \t ======FAILED======")
            return False, stlog
        else:
            print("\t \t \t OTP LIMIT TIMEOUT >1800 !")
            LOGIN_JSON[email]["OTP_COUNT"] = 0
            write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
            state.FIRSTOTPSENT=None
            state.FIRST_INCORRECT_OTP=None
            # PASS, Now user can get OTP
            print("\t \t \t ======DONE======")
            return True, None

def verifyOTP(state, email, LOGIN_JSON, sidebar, GlobalElements):

    print("\t Verifing OTP...")
    
    otpHeader_info = stOTPHeaderInfo(f"""An OTP ({LOGIN_JSON[email]["OTP_COUNT"]}/3) is sent over *{email}* also check the **Spam folder**""", sidebar)
    GlobalElements.append(otpHeader_info)
    enter_OTP_txt, enteredOTP = stEnterOTP(sidebar)
    GlobalElements.append(enter_OTP_txt)

    # 2nd condition is used to stop sending 2 OTP
    if(enteredOTP == "" or enteredOTP == state.INCORRECT_OTP): 
        print("\t \t OTP field is (empty)")
        if(state.FIRSTOTPSENT==None):
            print("\t \t \t First OTP sent")
            msg = f"""An OTP ({LOGIN_JSON[email]["OTP_COUNT"] + 1}/3) is sent over *{email}* also check the **Spam folder**"""
            otpHeader_info.info(msg)
            state.FIRSTOTPSENT = True
            state.OTP = str(sendOTP(email))
            LOGIN_JSON[email]["OTP_COUNT"] += 1
            write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
            print("\t \t \t ======Process======")
        if(state.FIRST_INCORRECT_OTP==True):
            print("\t \t \t Incorrect OTP (empty)")
            otpHeader_info.empty()
            incorrectOTPText = f"""
                        OTP is incorrect!    
                        Another OTP ({LOGIN_JSON[email]["OTP_COUNT"]}/3) is sent over *{email}* also check the **Spam folder**.
                    """
            element = stIncorrectOTPError(incorrectOTPText, sidebar)
            GlobalElements.append(element)
            print("\t \t \t ======FAILED======")
    elif(state.OTP != enteredOTP):
        print("\t \t OTP is incorrect")
        state.INCORRECT_OTP = enteredOTP
        if state.FIRST_INCORRECT_OTP == None: 
            print("\t \t \t This is First Incorrect OTP")
            state.FIRST_INCORRECT_OTP = True
        otpHeader_info.empty()
        incorrectOTPText = f"""
                        OTP is incorrect!    
                        Another OTP ({LOGIN_JSON[email]["OTP_COUNT"] + 1}/3) is sent over *{email}* also check the **Spam folder**.
                    """
        stIncorrectOTPError(incorrectOTPText, sidebar)
        state.OTP = str(sendOTP(email))
        LOGIN_JSON[email]["OTP_COUNT"] += 1
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        print("\t \t ======FAILED======")
    elif(state.OTP == enteredOTP):
        print("\t \t OTP Verified Successfully")
        otpHeader_info.empty()
        enter_OTP_txt.empty()
        LOGIN_JSON[email]["OTP_COUNT"] = 0
        LOGIN_JSON[email]["OTP_VERIFICATION_ID"] = state.ID
        write_JSON(LOGIN_JSON, LOGIN_JSON_PATH)
        state.FIRSTOTPSENT=None
        state.FIRST_INCORRECT_OTP=None
        print("\t \t ======DONE======")
        return True
    else:
        element = stUnknownOTPError(sidebar)
        GlobalElements.append(element)
        print("\t \t ======FAILED======")
    print("")
    
    return False