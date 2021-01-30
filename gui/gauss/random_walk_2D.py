import streamlit as st
import numpy as np
import pandas as pd
from logic.utils import animate_dot_2D

def get_st_probability(max_bounces, max_sim):
    p_up: float = 0.25
    p_right: float = 0.25
    p_left: float = 0.25
    p_down: float = 0.25
    with st.sidebar.beta_container():
        st.markdown("", unsafe_allow_html=True)
        add_bias: bool = st.checkbox("Add bias")
        if add_bias:
            p_up_max = 1.0
            if p_up_max <= 0: return None
            p_up: float = st.slider("Probability of particle moving up (in +y direction)",
                                    min_value=0.0,
                                    max_value=1.0,
                                    value=0.25,
                                    step=0.1)
            p_right_max = p_up_max - p_up
            if p_right_max <= 0: return None
            p_right: float = st.slider("Probability of particle moving right (in +x direction)",
                                       min_value=0.0,
                                       max_value=p_right_max,
                                       value=0.25 if 0.25 < p_right_max else p_right_max/2,
                                       step=0.1)
            p_left_max = p_up_max - p_up - p_right
            if p_left_max <= 0: return None
            p_left: float = st.slider("Probability of particle moving left (in -x direction)",
                                      min_value=0.0,
                                      max_value=p_left_max,
                                      value=0.25 if 0.25 < 1.0 - p_up - p_right else (1.0 - p_up - p_right)/2,
                                      step=0.1)
            p_down: float = 1 - p_up - p_right - p_left
            if p_down <= 0: return None

            # st.markdown(f"Probability of particle moving down (in -y direction): {p_down}")
        n_bounces: int = st.sidebar.slider("Number of bounces (N)",
                                           min_value=1,
                                           max_value=max_bounces,
                                           value=50,
                                           step=1)

        n_sim: int = st.sidebar.number_input("Number of simulations",
                                             min_value=10,
                                             max_value=max_sim,
                                             value=200,
                                             step=10, )

    return (p_up, p_down, p_right, p_left), (n_bounces, n_sim)

def run(state):
    st.markdown("""
        Now let's see how Random walk in $2$ Dimension results in a
        <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Multivariate_normal_distribution">Multivariate Gaussian distribution</a>.<br>
        """, unsafe_allow_html=True)

    max_bounces, max_sim = 100, 500
    prev_p_up = None if "p_up" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_up"]
    prev_p_right = None if "p_right" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_right"]
    prev_p_left = None if "p_left" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_left"]

    try:
        (p_up, p_down, p_right, p_left), (n_bounces, n_sim) = get_st_probability(max_bounces, max_sim)
    except:
        st.sidebar.markdown("""
        <blockquote class="error">
            Probability selection is not valid!
        </blockquote>
        """, unsafe_allow_html=True)
        return

    state.gauss["Random walk 1D"]["p_up"] = p_up
    state.gauss["Random walk 1D"]["p_right"] = p_right
    state.gauss["Random walk 1D"]["p_left"] = p_left

    if state.stSettings["seed"] is not None: np.random.seed(state.stSettings["seed"])
    else: np.random.seed()

    directions = state.gauss["Random walk 1D"]["random_walks_direction"] = state.gauss["Random walk 1D"]["random_walks_direction"] if \
        "random_walks_direction" in state.gauss["Random walk 1D"] and \
        prev_p_up == p_up and \
        prev_p_right == p_right and \
        prev_p_left == p_left and \
        state.stSettings["seed"] is not None and \
        state.seed_changed is False else \
        np.array([np.random.choice(["+y", "-y", "+x", "-x"], max_bounces, p=[p_up, p_down, p_right, p_left]) for _ in range(max_sim)])

    x, y = np.zeros(shape=(max_sim, max_bounces), dtype=np.int8), np.zeros(shape=(max_sim, max_bounces), dtype=np.int8)
    for sim in range(max_sim):
        for bounce in range(1, max_bounces):
            if directions[sim][bounce]   == "+y": x[sim][bounce], y[sim][bounce] = x[sim][bounce-1], y[sim][bounce-1] + 1
            elif directions[sim][bounce] == "-y": x[sim][bounce], y[sim][bounce] = x[sim][bounce-1], y[sim][bounce-1] - 1
            elif directions[sim][bounce] == "+x": x[sim][bounce], y[sim][bounce] = x[sim][bounce-1] + 1, y[sim][bounce-1]
            else: x[sim][bounce], y[sim][bounce] = x[sim][bounce-1] - 1, y[sim][bounce-1]

    with st.beta_expander("Scenario", expanded=True):
        st.markdown(f"""
        Let's assume that there is a crazy particle wandering on a $2$-Dimensional surface.    
        Say that initial location of particle is origin $(x=0, y=0)$    
        (Say that it's current location is $(x,y)$)This particle bounces,
        
        - Up (at $y+1$) with probability ${'{:.2f}'.format(p_up)}$
        - Right (at $x+1$) with probability ${'{:.2f}'.format(p_right)}$
        - Left (at $x-1$) with probability ${'{:.2f}'.format(p_left)}$
        - Down (at $y-1$) with probability ${'{:.2f}'.format(p_down)}$

        Now we want to study this particle's location after $N({n_bounces})$ number of bounces.    
        Now let's see a random walk of a single particle. Here column indicates number of bounces
        and value(of that column) indicates x-axis and y-axis position respectively after certain number of bounces.
        """)

        # npArray.columns += 1
        st.write(pd.DataFrame(data=np.array([f"({x[0][bounce]}, {y[0][bounce]})" for bounce in range(n_bounces + 1)]).reshape((1, n_bounces + 1)), index=["Position (x, y)"]))
