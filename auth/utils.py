import json
from typing import Dict, Union

import numpy as np
from hashlib import sha256
from auth.forgotPasswd import send

def hashPasswd(passwd: str) -> str:
    h = sha256()
    h.update(passwd.encode())
    H = h.hexdigest()
    return H

def read_JSON(path: str) -> Union[Dict[str, Dict[str, Union[str, int, Dict[str, int]]]], Dict[str, str]]:
    with open(path) as f:
        data = f.read()
    f.close()
    return json.loads(data)

def write_JSON(json_file: dict, path: str) -> None:
    with open(path, 'w+') as f:
        json.dump(json_file, indent=4, sort_keys=False, fp=f)
    f.close()

def sendOTP(state, email: str) -> int:
    state.experimental_rerun = True
    # noinspection PyArgumentList
    np.random.seed()
    OTP = np.random.randint(100001, 999999)
    send(email, OTP)
    return OTP
