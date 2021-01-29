import streamlit as st

from SessionState import set_title
from utils import set_get_URL
from gui.gauss import random_walk_1D, random_walk_2D, multiple_die_rolls

def main(state):
    topics = ["Random walk 1D", "Random walk 2D", "Multiple Die Rolls"]
    idx = 0
    if "topic" in state.url and state.url["topic"][0] in topics:
        idx = topics.index(state.url["topic"][0])
    option: str = st.sidebar.selectbox("Topic", topics, index=idx)
    set_get_URL(dist="remove", parameters={
        "topic": option
    })

    prev_seed = state.stSettings["seed"]
    if state.stSettings["seed-checkbox"].checkbox("Enable Seed", True):
        state.stSettings["seed"] = state.stSettings["seed-number"].number_input("Enter Seed", 0, 10000, 0, 1)
    else:
        state.stSettings["seed"] = None
    state.seed_changed = True if state.stSettings["seed"] != prev_seed else False

    state.gauss = state.gauss if state.gauss is not None else {"Random walk 1D": {}, "Random walk 2D": {}, "Multiple Die Rolls": {}}
    if option == topics[0]:
        set_title('Random walk 1D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_1D.run(state)
    if option == topics[1]:
        set_title('Random walk 2D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_2D.run(state)
    if option == topics[2]:
        set_title('Multiple Die Rolls | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        multiple_die_rolls.run(state)
