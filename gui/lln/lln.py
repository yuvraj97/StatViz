from typing import Union, Dict
import streamlit as st
import numpy as np
from plotly.graph_objs import Figure

from gui.lln.display import stDisplay
import logic.lln.lln as lln
from distribution import distributions_properties, which_distribution, stDistribution
from utils import set_get_URL, urlIndex


def main(state):
    option: str = st.sidebar.selectbox("Select Distribution", list(which_distribution.keys()), index=urlIndex(state.url))
    dist: str = which_distribution[option]

    set_get_URL(dist=distributions_properties[dist]["name"])

    var: Dict[str, Union[int, float]]
    n: Dict[str, int]
    var, n = stDistribution(dist)

    if state.stSettings["seed-checkbox"].checkbox("Enable Seed", True):
        state.stSettings["seed"] = state.stSettings["seed-number"].number_input("Enter Seed", 0, 10000, 0, 1)

    mean: float
    population: np.ndarray
    sample: np.ndarray
    pdf: Figure
    simulation: Figure
    mean, population, sample, pdf, simulation = lln.run(dist, var, n, state)

    stDisplay(dist, population, sample, var, n, mean, (pdf, simulation), state)
