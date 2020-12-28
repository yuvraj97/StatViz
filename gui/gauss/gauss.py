import streamlit as st

def main(state):

    st.markdown("""
    <blockquote class="info">
        Expected date of release: <b>DD/MM/YYYY</b><br>
    </blockquote>
    When it came to Gaussian Distribution, what is the first thing came into mind
    <a rel='noreferrer' target='_blank' href="https://read.quantml.org/stats/clt/.">Central Limit Theorem</a>
    right.<br>
    In this section we will see some simulations and see how they results in a
    <a rel='noreferrer' target='_blank' href="https://read.quantml.org/gaussian-distribution/.">
    Gaussian Distribution</a>.<br>
    """, unsafe_allow_html=True)
    st.markdown("""
    Here we will simulate,    
    - Random walk $1\\text{D}$
    - Random walk $2\\text{D}$
    - Multiple Die Rolls
    """)