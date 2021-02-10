from typing import Dict
# import streamlit as st
from uuid import uuid4
from SessionState import get_cookie
import streamlit.components.v1 as components


def set_cookie(name: str, value: str) -> None:
    # print("set_cookie:: ", name, " : ", value)
    components.html(f"""
    <script>
        parent.document.cookie = "{name}={value};expires=Fri, 31 Dec 9999 23:59:59 GMT;path=/;SameSite=Lax"
    </script>
    """, height=0, width=0)


def get_ID(CURRENTLY_LOGIN_JSON: Dict[str, str]) -> str:
    quantml_id = get_cookie("quantml-app-ID")
    if quantml_id is not None: return quantml_id
    quantml_id = str(uuid4())
    while quantml_id in CURRENTLY_LOGIN_JSON:
        quantml_id = uuid4()
    set_cookie("quantml-app-ID", quantml_id)
    return quantml_id
