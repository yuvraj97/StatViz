import streamlit as st
import numpy as np

def run(state):
    st.markdown("""
        We can find Random walk everywhere like in 
        <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Brownian_motion">Brownian motion</a>, 
        <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Diffusion_process">Modeling Diffusion Process</a>,
        <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/PageRank#Distributed_algorithm_for_PageRank_computation">PageRank Algorithm</a>,
        etc.<br>
        Here we will see how random walk in $1$ Dimension results in a
        <a rel='noreferrer' target='_blank' href="https://read.quantml.org/statistics/gaussian-distribution/">Gaussian distribution</a>.<br>
        """, unsafe_allow_html=True)

    prev_p = None if "p" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p"]
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
        state.gauss["Random walk 1D"]["p"] = p

        n_bounces: int = st.slider("Number of bounces (N)",
                                   min_value=1,
                                   max_value=100,
                                   value=50,
                                   step=1)

        n_sim: int = st.number_input("Number of simulations",
                                     min_value=10,
                                     max_value=500,
                                     value=200,
                                     step=10)

    if state.stSettings["seed"] is not None:
        np.random.seed(state.stSettings["seed"])
    else:
        np.random.seed()
