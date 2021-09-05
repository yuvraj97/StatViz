import streamlit as st
from Chapters.utils.SessionState import set_title
from utils.utils import set_get_URL
from Chapters.Gaussian_Distribution import random_walk_1D, random_walk_2D


def main(state):
    topics, idx = ["Random walk 1D", "Random walk 2D"], 0
    if "topic" in state.url and state.url["topic"][0] in topics:
        idx = topics.index(state.url["topic"][0])

    option: str = st.sidebar.selectbox("Topic", topics, index=idx)

    set_get_URL(parameters={
        "dist": "remove",
        "topic": option
    })

    state.gauss = state.gauss if state.gauss is not None else {"Random walk 1D": {}, "Random walk 2D": {}}
    if option == topics[0]:
        set_title('Random walk 1D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_1D.run(state)
    if option == topics[1]:
        set_title('Random walk 2D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_2D.run(state)
