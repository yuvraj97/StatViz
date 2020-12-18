import json
import numpy as np
from hashlib import sha256
import auth.forgotPasswd
from auth.forgotPasswd import send


def hashPasswd(passwd):
    h = sha256()
    h.update(passwd.encode())
    H = h.hexdigest()
    return H


def read_JSON(path):
    with open(path) as f:
        data = f.read()
    f.close()
    return json.loads(data)


def write_JSON(json_file, path):
    with open(path, 'w+') as f:
        json.dump(json_file, indent=4, sort_keys=False, fp=f)
    f.close()


def sendOTP(state, email):
    state.experimental_rerun = True
    np.random.seed()
    OTP = np.random.randint(100001, 999999)
    send(email, OTP)
    return OTP
