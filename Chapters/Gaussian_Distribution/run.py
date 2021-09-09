import streamlit as st
from utilities.ui import intialize, footer
from utilities.utils import set_get_URL
from Chapters.Gaussian_Distribution import random_walk_1D
from Chapters.Gaussian_Distribution import random_walk_2D


def main():

    intialize("Gaussian Distribution")

    topics, idx = ["Random walk 1D", "Random walk 2D"], 0
    url = st.experimental_get_query_params()
    if "topic" in url and url["topic"][0] in topics:
        idx = topics.index(url["topic"][0])

    option: str = st.sidebar.selectbox("Topic", topics, index=idx)

    set_get_URL(parameters={
        "dist": "remove",
        "topic": option
    })

    state = st.session_state
    state["gauss"] = state["gauss"] if "gauss" in state else {"Random walk 1D": {}, "Random walk 2D": {}}
    if option == topics[0]:
        # set_title('Random walk 1D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_1D.run()
    if option == topics[1]:
        # set_title('Random walk 2D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_2D.run()

    footer()
