import streamlit as st

import gui.lln.display as stDisplay
import logic.lln.lln as lln
from distribution import distributions_properties, which_distribution, stDistribution
from logic.lln.utils import urlIndex
from utils import set_get_URL


def main(state):
    # print("    ======== lln.py ========")
    # print("    ARGUMENTS: state")
    option = st.sidebar.selectbox("Select Distribution", list(which_distribution.keys()), index=urlIndex(state.url))
    dist = which_distribution[option]
    # print("          * option: ",option)
    # print("          * dist: ",dist)

    set_get_URL(dist=distributions_properties[dist]["name"])

    # print("          * state.URL: ",state.url)

    var, n = stDistribution(dist)
    # print("          * var: ", var)
    # print("          * n: ", n)

    if state.stSettings["seed-checkbox"].checkbox("Enable Seed", True):
        state.stSettings["seed"] = state.stSettings["seed-number"].number_input("Enter Seed", 0, 10000, 0, 1)

    mean, population, sample, pdf, simulation = lln.run(dist, var, n, state)

    # print("      Loading...")
    # st.plotly_chart(simulation, use_container_width=True)#, filename='latex', include_mathjax='cdn')
    stDisplay.run(dist, population, sample, var, n, mean, pdf, simulation, state)
