import streamlit as st
import numpy as np
import pandas as pd
from gui.utils import stPandas


def run(state):
    st.markdown("""
        Now let's see how Random walk in $2$ Dimension results in a
        <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Multivariate_normal_distribution">Multivariate Gaussian distribution</a>.<br>
        """, unsafe_allow_html=True)

    max_bounces, max_sim = 100, 500
    prev_p_x = None if "p_x" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_x"]
    prev_p_y = None if "p_y" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_y"]
    p_x: float = 0.5
    p_y: float = 0.5
    with st.sidebar.beta_container():
        st.markdown("", unsafe_allow_html=True)
        add_bias: bool = st.checkbox("Add bias")
        if add_bias:
            p_x: float = st.number_input("Probability of particle moving right (in +x direction)",
                                         min_value=0.0,
                                         max_value=1.0,
                                         value=0.5,
                                         step=0.1)
            p_y: float = st.number_input("Probability of particle moving up (in +y direction)",
                                         min_value=0.0,
                                         max_value=1.0,
                                         value=0.5,
                                         step=0.1)

        state.gauss["Random walk 1D"]["p_x"] = p_x
        state.gauss["Random walk 1D"]["p_y"] = p_y

        n_bounces: int = st.slider("Number of bounces (N)",
                                   min_value=1,
                                   max_value=max_bounces,
                                   value=50,
                                   step=1)

        n_sim: int = st.number_input("Number of simulations",
                                     min_value=10,
                                     max_value=max_sim,
                                     value=200,
                                     step=10)

    if state.stSettings["seed"] is not None: np.random.seed(state.stSettings["seed"])
    else: np.random.seed()

    state.gauss["Random walk 1D"]["random_walks_x"] = state.gauss["Random walk 1D"]["random_walks_x"] if \
        "random_walks_x" in state.gauss["Random walk 1D"] and \
        prev_p_x == p_x and \
        state.stSettings["seed"] is not None and \
        state.seed_changed is False else \
        np.array([np.cumsum(np.random.choice([+1, -1], max_bounces, p=[p_x, 1 - p_x])) for _ in range(max_sim)])

    state.gauss["Random walk 1D"]["random_walks_y"] = state.gauss["Random walk 1D"]["random_walks_y"] if \
        "random_walks_y" in state.gauss["Random walk 1D"] and \
        prev_p_y == p_y and \
        state.stSettings["seed"] is not None and \
        state.seed_changed is False else \
        np.array([np.cumsum(np.random.choice([+1, -1], max_bounces, p=[p_y, 1 - p_y])) for _ in range(max_sim)])

    with st.beta_expander("Scenario", expanded=True):
        st.markdown(f"""
        Let's assume that there is a crazy particle wandering on a $2$-Dimensional surface.    
        Say that initial location of particle is origin $(x=0, y=0)$    
        (Say that it's current location is $(x,y)$)This particle bounces,
        
        - Right (at $x+1$) with probability ${'{:.2f}'.format(p_x)}$
        - Left (at $x-1$) with probability ${'{:.2f}'.format(1-p_x)}$
        - Up (at $y+1$) with probability ${'{:.2f}'.format(p_y)}$
        - Down (at $y-1$) with probability ${'{:.2f}'.format(1-p_y)}$

        Now we want to study this particle's location after $N({n_bounces})$ number of bounces.    
        Now let's see a random walk of a single particle. Here column indicates number of bounces
        and value(of that column) indicates x-axis and y-axis position respectively after certain number of bounces.
        """)
        npArray = np.array([state.gauss["Random walk 1D"]["random_walks_x"][0],state.gauss["Random walk 1D"]["random_walks_y"][0]])
        npArray = pd.DataFrame(data=npArray, index=["Position (x-axis)", "Position (y-axis)"])
        npArray.columns += 1
        st.write(npArray)
