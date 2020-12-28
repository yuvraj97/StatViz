import streamlit as st

def main(state):
    app_under_dev = """
    <blockquote class="warning">
        This app is under development so currently <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">patreons</a>
        that opt for Statistics App, are able to access all upcoming visualizations.<br>
        Once this Statistics App is concluded plan is to make all visualizations of this Statistics App to be available
        to everyone.<br>
        If you wish to support my work <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">Join us on patreon</a>,
        also opt for Statistics App to get access to all of the upcoming visualizations.<br>
    </blockquote>
    """
    st.markdown(f"""
    <blockquote class="info">
        Expected date of release: <b>DD/MM/YYYY</b><br>
    </blockquote>
    {app_under_dev if not state.isLoggedIn else ""}
    Hope you enjoyed the app so far, now our next step is to eliminate <b>most</b> of our doubts regarding the 
    beauty of <b>Gaussian Distribution</b>.<br>

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
