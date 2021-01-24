import streamlit as st

def run():
    st.markdown("""
    We can found Random walk everywhere like in 
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Brownian_motion">Brownian motion</a>, 
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Diffusion_process">Modeling Diffusion Process</a>,
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/PageRank#Distributed_algorithm_for_PageRank_computation">PageRank Algorithm</a>,
    etc.<br>
    Here we will see how random walk results in a
    <a rel='noreferrer' target='_blank' href="https://read.quantml.org/statistics/gaussian-distribution/">Gaussian distribution</a>.<br>
    """, unsafe_allow_html=True)

    p: float = 0.5
    with st.sidebar.beta_container():
        st.markdown("", unsafe_allow_html=True)
        add_bias: bool = st.checkbox("Add bias")
        if add_bias:
            p: float = st.number_input("Probability of particle moving to the right (p)",
                                       min_value=0.0,
                                       max_value=1.0,
                                       value=0.5,
                                       step=0.1)
        n_bounces: bool = st.number_input("Number of bounces (N)",
                                          min_value=1,
                                          max_value=100,
                                          value=10)

    with st.beta_expander("Scenario", expanded=True):
        st.markdown(f"""
        Say you have a very thin pipe and you place a crazy particle inside that pipe.    
        This particle bounces left(with probability ${'{:.2f}'.format(p)}$) and right(with probability ${'{:.2f}'.format(1 - p)}$).    
        Now we want to study this particle's location after $N(={n_bounces})$ number of bounces.
        """)
