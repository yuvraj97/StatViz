import streamlit as st
import numpy as np
import pandas as pd
from pandas import DataFrame
from scipy.stats import norm

from gui.utils import stPandas
from logic.utils import plot_histogram, line_plot


def run(state):
    st.markdown("""
    We can find Random walk everywhere like in 
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Brownian_motion">Brownian motion</a>, 
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Diffusion_process">Modeling Diffusion Process</a>,
    <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/PageRank#Distributed_algorithm_for_PageRank_computation">PageRank Algorithm</a>,
    etc.<br>
    Here we will see how random walk in $1D$ results in a
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
    else: np.random.seed()
    # print('state.stSettings["seed"]', state.stSettings["seed"])

    print("random_walks" in state.gauss["Random walk 1D"], prev_p == p, state.seed_changed is False)
    state.gauss["Random walk 1D"]["random_walks"] = state.gauss["Random walk 1D"]["random_walks"] if \
        "random_walks" in state.gauss["Random walk 1D"] and \
        prev_p == p and \
        state.stSettings["seed"] is not None and \
        state.seed_changed is False else \
            np.array([np.cumsum(np.random.choice([+1, -1], 100, p=[p, 1 - p])) for _ in range(500)])

    with st.beta_expander("Scenario", expanded=True):
        st.markdown(f"""
        Say you have a very thin pipe and you place a crazy particle inside that pipe.    
        Say that initial location of particle is $x=0$    
        This particle bounces right at $x+1$(with probability ${'{:.2f}'.format(p)}$) and 
        left at $x-1$(with probability ${'{:.2f}'.format(1 - p)}$).    
        Now we want to study this particle's location after $N({n_bounces})$ number of bounces.    
        Now let's see a random walk of a single particle. Here column indicates number of bounces
        and value(of that column) indicates position after certain number of bounces.
        """)
        st.write(stPandas(state.gauss["Random walk 1D"]["random_walks"][0], label="Position"))

    with st.beta_expander("Getting Data", expanded=True):
        st.markdown(f"""
        Data we see above is just for a single observation, we need multiple observations of in order to
        study position after ${n_bounces}$ bounces.    
        So let's simulate data for ${n_sim}$ particles where each particle performs ${n_bounces}$
        number of bounces.    
        """)

        index = ["1st Random walk", "2nd Random walk", "3rd Random walk"]
        index.extend([f"{i+4}th Random walk" for i in range(n_sim - 3)])
        df = pd.DataFrame(data=state.gauss["Random walk 1D"]["random_walks"][:n_sim, :n_bounces], index=index)
        df.columns += 1
        st.write(df)

    with st.beta_expander(f"Getting particle's position after {n_bounces} bounces", expanded=True):
        st.markdown(f"""
        Now we want to study particle's position after ${n_bounces}$ bounces.    
        We have our data of ${n_sim}$ particles with ${n_bounces}$ bounces each.    
        Let's extract particle's position after ${n_bounces}$ bounces, i.e. the last column of our data.   
        """)

        position_data = state.gauss["Random walk 1D"]["random_walks"][:n_sim, n_bounces - 1]
        npArray: DataFrame = pd.DataFrame(data=position_data)
        index = ["1st Particle", "2nd Particle", "3rd Particle"]
        index.extend([f"{i + 4}th Particle" for i in range(n_sim - 3)])
        npArray.index = index
        npArray.columns = [f"Position after {n_bounces} bounces"]
        st.write(npArray)

    bins, counts = np.unique(state.gauss["Random walk 1D"]["random_walks"][:n_sim, n_bounces - 1], return_counts=True)
    fig, (counts, bins) = plot_histogram(
        position_data,
        description={
            "title": {
                "main": f"Particle's Position after {n_bounces} bounces",
                "x": f"Position(x) after {n_bounces} bounces",
                "y": f"PMF of Position(x) after {n_bounces} bounces",
                "force": True
            },
            "label": {
                "main": "Position's PMF",
                "x": "Position",
            }
        },
        convert_into_probability_plot=True,
        isMobile=state.isMobile,
        tilde_equals="=",
        bins=bins,
        counts=counts,
        centralize_bins=False,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

