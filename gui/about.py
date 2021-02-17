# import os
import streamlit as st
# from PIL import Image
from utils import set_get_URL

def main(state):
    set_get_URL(parameters={
        "dist" : "remove",
        "topic": "remove"
    })
    with st.beta_expander("About", True):
        st.markdown("""
        Hello my name is <b>Yuvraj Garg</b><br>
        I am an independent creator of
        <a rel='noreferrer' target='_blank' href="https://www.quantml.org/">QuantML.org</a><br>
        I am passionate for Mathematics and Machine Learning.<br>
        Here in our <a rel='noreferrer' target='_blank' href="https://app.quantml.org/statistics/">Statistics App</a>,
        you will learn <b>statistical</b> concepts by interacting with them.<br>
        Here I will try my best to visualize statistical concepts and
        make those statistical concepts interactive so you can better understand those statistical concepts.<br>
        You should expect new concept <b>visualization</b> (and chapter for our
        <a rel='noreferrer' target='_blank' href="https://read.quantml.org/statistics/">Statistics Guide</a>
        ) <b>every other week</b>.
        
        """, unsafe_allow_html=True)

    with st.beta_expander("Connect", True):
        st.markdown("""
        Join us on <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">Patreon</a><br>
        Join our &nbsp;&nbsp;&nbsp; <a rel='noreferrer' target='_blank' href="https://discord.quantml.org">Community</a><br>
        Linkedin:&nbsp;&nbsp;
        <a rel='noreferrer' target='_blank' href="https://www.linkedin.com/in/yuvraj97/">yuvraj97</a><br> 
        Email: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="mailto:support@quantml.org">support@quantml.org</a>
        """, unsafe_allow_html=True)

    with st.beta_expander("🐞 Bugs", True):
        # image_path = os.path.join(os.getcwd(), "img-dark" if state.theme == "dark" else "img", "bad-msg-format.png")
        # image = Image.open(image_path)
        st.markdown("""
        These bugs will be fixed in near future.
        - In Settings, (currently) you may need to click twice on "Apply Dark Theme" to change theme.
        - Sometime a reloading ("F5" / "Ctrl + R") is require to initialize the app.
        """)
        # if st.checkbox("Show error Image"):
        #     st.image(image, use_column_width=True)
