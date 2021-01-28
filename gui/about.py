import os
import streamlit as st
from PIL import Image

def main(state):
    with st.beta_expander("About", True):
        st.markdown("""
        Hello my name is <b>Yuvraj Garg</b><br>
        I am an independent creator of
        <a rel='noreferrer' target='_blank' href="https://www.quantml.org/">QuantML.org</a><br>
        I am passionate for Mathematics and Machine Learning.<br>
        Here at <a rel='noreferrer' target='_blank' href="https://app.quantml.org/statistics/">https://app.quantml.org/statistics/</a>,
        you will learn <b>statistical</b> concepts by interacting with them.<br>
        Here I try my best to visualize statistical concepts and
        make those statistical concepts interactive so you can better understand those statistical concepts.<br>
        You should expect new concept <b>visualization</b> (and chapter for our
        <a rel='noreferrer' target='_blank' href="https://read.quantml.org/statistics/">Statistics Guide</a>
        ) <b>every week</b>.
        
        """, unsafe_allow_html=True)

    with st.beta_expander("Connect", True):
        st.markdown("""
        Join us on <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">patreon</a><br>
        Join our &nbsp;&nbsp;&nbsp; <a rel='noreferrer' target='_blank' href="https://discord.gg/8wpzGhfXJR">Discussion form</a><br>
        Linkedin:&nbsp;&nbsp;
        <a rel='noreferrer' target='_blank' href="https://www.linkedin.com/in/yuvraj97/">yuvraj97</a><br> 
        Email: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="mailto:yuvraj97.ml@gmail.com">yuvraj97.ml@gmail.com</a>
        """, unsafe_allow_html=True)

    with st.beta_expander("🐞 Bugs", True):
        # image_path = os.path.join(os.getcwd(), "img-dark" if state.theme == "dark" else "img", "bad-msg-format.png")
        # image = Image.open(image_path)
        st.markdown("""
        These bugs will be fixed in near future.
        - In Settings, (currently) you may need to click twice on "Apply Dark Theme" to change theme.
        - Sometime a reloading ("F5" / "Ctrl + R") is require to initialize the app.
        - When you login you see a flash of an error.  
        """)
        # if st.checkbox("Show error Image"):
        #     st.image(image, use_column_width=True)
