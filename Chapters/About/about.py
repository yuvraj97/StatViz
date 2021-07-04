import streamlit as st
from utils import set_get_URL

def main(state):
    set_get_URL(parameters={
        "dist": "remove",
        "topic": "remove"
    })
    st.write("# About")
    st.markdown("""
    Hello my name is **Yuvraj Garg**.   
    I am an independent creator of
    [QuantML.org](https://www.quantml.org/)   
    I am passionate for Mathematics and Machine Learning.  
    Here in our [Statistics App](https://app.quantml.org/statistics/)
    you will learn **statistical** concepts by interacting with them.   
    Here I will try my best to visualize statistical concepts and
    make those statistical concepts interactive so you can better understand those statistical concepts
    """)

    st.write("# Connect")
    st.markdown("""
    Join us on [Patreon](https://www.patreon.com/quantml)    
    Join our &nbsp;&nbsp;&nbsp; [Community](https://discord.quantml.org)    
    Linkedin:&nbsp;&nbsp; [yuvraj97](https://www.linkedin.com/in/yuvraj97/)    
    Email: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [support@quantml.org](mailto:support@quantml.org)
    """)
