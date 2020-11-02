import streamlit as st
from logic.lln.run import run_dist
from gui.lln.utils import distributions_properties, which_distribution, stDistribution, getDistByIndex

def main(state, GlobalElements):
    print("########## lln.main() ##########")
    if(state.lln_init == None):
        print("\t  lln.main state initializing ...")
        state.lln_init = True
        state.lln = distributions_properties
        state.lln_index = 0
        print("\t  lln.main state initialized !  ")
        
    option = st.sidebar.selectbox("Select Distribution", which_distribution, index = state.lln_index)
    print("Option:", option)

    plot_TF = False
    idx = which_distribution.index(option)
    dist = getDistByIndex(idx)
    var = stDistribution(dist, state, True)
    if(state.lln_index == idx and state.lln[dist] == var):
        print("\t plotit :)")
        plot_TF = True
        pdf, simulation = run_dist(dist, var, state.lln["n_population"], state.lln["n_samples"])
    else:
        print("\t wait to plot !")
        state.lln[dist] = var
    state.lln_index = idx
    
    if(plot_TF):
        success = st.empty()
        success.success("Loading...")
        print("\t Loading...")
        
        plot = st.empty()
        plot.plotly_chart(pdf)#, filename='latex', include_mathjax='cdn')
        plot = st.empty()
        plot.plotly_chart(simulation)#, filename='latex', include_mathjax='cdn')
        
        success.empty()