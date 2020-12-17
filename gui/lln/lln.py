import streamlit as st
import logic.lln.lln as lln
import logic.lln.display as stDisplay
from logic.lln.utils import urlIndex
from utils import set_get_URL
from distribution import distributions_properties, n, which_distribution, stDistribution, idx2distribution, distribution2idx, distribution2url

def main(state, GlobalElements):
    #print("    ======== lln.py ========")
    #print("    ARGUMENTS: state, GlobalElements")
    option = st.sidebar.selectbox("Select Distribution", list(which_distribution.keys()), index = urlIndex(state.url))
    dist = which_distribution[option]
    #print("          * option: ",option)
    #print("          * dist: ",dist)

    url = set_get_URL(dist = distributions_properties[dist]["name"])

    #print("          * state.URL: ",state.url)

    var, n = stDistribution(dist, state)
    #print("          * var: ", var)
    #print("          * n: ", n)
    
    mean, population, sample, pdf, simulation = lln.run(dist, var, n, state)
    
    #print("      Loading...")
    
    
    st.plotly_chart(simulation, use_container_width=True)#, filename='latex', include_mathjax='cdn')
    stDisplay.run(dist, population, sample, var, n, mean, pdf, simulation)