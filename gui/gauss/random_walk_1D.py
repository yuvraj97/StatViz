import streamlit as st
import numpy as np
from gui.utils import stPandas
from logic.utils import plot_histogram


def run(state):
    st.markdown("""
    We can found Random walk everywhere like in 
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Brownian_motion">Brownian motion</a>, 
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Diffusion_process">Modeling Diffusion Process</a>,
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/PageRank#Distributed_algorithm_for_PageRank_computation">PageRank Algorithm</a>,
    etc.<br>
    Here we will see how random walk results in a
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

    if state.stSettings["seed"] is not None: np.random.seed(state.stSettings["seed"])

    print("random_walks" in state.gauss["Random walk 1D"], prev_p == p, state.seed_changed is False)
    state.gauss["Random walk 1D"]["random_walks"] = state.gauss["Random walk 1D"]["random_walks"] if \
        "random_walks" in state.gauss["Random walk 1D"] and \
        prev_p == p and \
        state.seed_changed is False else \
            np.array([np.cumsum(np.random.choice([+1, -1], 100, p=[p, 1 - p])) for _ in range(500)])

    with st.beta_expander("Scenario", expanded=True):
        st.markdown(f"""
        Say you have a very thin pipe and you place a crazy particle inside that pipe.    
        Say that initial location of particle is $x=0$    
        This particle bounces right at $x+1$(with probability ${'{:.2f}'.format(p)}$) and 
        left at $x-1$(with probability ${'{:.2f}'.format(1 - p)}$).    
        Now we want to study this particle's location after $N(={n_bounces})$ number of bounces.    
        Now let's see a random walk, here first row indicate number of bounces and second row indicates
        position after certain number of bounces.
        """)
        st.write(stPandas(state.gauss["Random walk 1D"]["random_walks"][0], label="Position"))
    bins, counts = np.unique(state.gauss["Random walk 1D"]["random_walks"][:n_sim, n_bounces - 1], return_counts=True)
    fig, (counts, bins) = plot_histogram(
        state.gauss["Random walk 1D"]["random_walks"][:n_sim, n_bounces - 1],
        description={
            "title": {
                "main": "Random Walk 1D",
                "x": f"Position(x) after {n_bounces} bounces",
                "y": f"PMF of Position(x) after {n_bounces} bounces",
                "force": True
            },
            "label": {
                "main": None,
                "x": "Position",
            }
        },
        convert_into_probability_plot=True,
        isMobile=state.isMobile,
        tilde_equals="=",
        bins=bins,
        counts=counts,
        centralize_bins=False
    )

    st.plotly_chart(fig, use_container_width=True)
