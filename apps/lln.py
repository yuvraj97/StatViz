import streamlit as st
import numpy as np
from apps.dist.dist import *
import matplotlib.pyplot as plt
from auth.stInputs import stWrite, stSelectbox, stSlider, stNumberInput, stEmpty


def main(state, GlobalElements):
    
    if(state.lln_init == None):
        state.lln_init = True
        state.lln = {
                    "gauss" : {"mu" : None, "sigma" : None, "n_sim": None},
                    "unif"  : {"a"  : None,   "b"   : None, "n_sim": None},
                    "ber"   : {"p"  : None,                 "n_sim": None},
                    "geo"   : {"p"  : None,                 "n_sim": None},
                    "bin"   : {"n"  : None,   "p"   : None, "n_sim": None},
                    "poiss" : {"lambda" : None,             "n_sim": None},
                    "beta"  : {"a"  : None,   "b"   : None, "n_sim": None},
                    "exp"   : {"lambda" : None,             "n_sim": None}
                    }
        state.index = 0
        
    element, option =   stSelectbox("Select Distribution", 
                                        (
                                          "Gaussian(μ, σ)",
                                          "Uniform(a, b)",
                                          "Bernoulli(p)", 
                                          "Geometric(p)", 
                                          "Binomial(n, p)",
                                          "Poisson(λ)",
                                          "Beta(α,β)",
                                          "Exp(λ)",
                                        ),
                                     index = state.index,
                                     sidebar = True
                                     )
    
    plot_TF = False
    if(option == "Gaussian(μ, σ)"):
        state.index = 0
        new_mu = st.sidebar.slider(f"Mean(μ)", min_value = -30.0, max_value = 30.0, value = state.lln["gauss"]["mu"] if state.lln["gauss"]["mu"] else 0.0, step = 0.5)
        new_sigma = st.sidebar.slider("Standard deviation(σ)", min_value = 0.0, max_value = 100.0, value = state.lln["gauss"]["sigma"] if state.lln["gauss"]["sigma"] else 1.0, step = 0.5)
        new_n_sim = st.sidebar.slider("Max. number of simulations", min_value = 10, max_value = 100, value = state.lln_n_sim if state.lln_n_sim else 50, step = 1)
        fig = gauss_dist(new_mu, new_sigma, new_n_sim)
        if(new_mu == state.lln["gauss"]["mu"] and new_sigma == state.lln["gauss"]["sigma"] and new_n_sim == state.lln["gauss"]["n_sim"]):
            plot_TF = True
            pdf, simulation = gauss_dist(new_mu, new_sigma, new_n_sim)
        else:
            state.lln["gauss"]["mu"], state.lln["gauss"]["sigma"], state.lln["gauss"]["n_sim"] = new_mu, new_sigma, new_n_sim
    elif(option == "Uniform(a, b)"):
        state.index = 1
        fig = unif_dist(a, b, nlim)
    elif(option == "Bernoulli(p)"):
        state.index = 2
        new_p = st.sidebar.slider("p", min_value = 0.0, max_value = 1.0, value = state.lln_p if state.lln_p else 0.1, step = 0.05)
        new_n_sim = st.sidebar.slider("Max. number of simulations", min_value = 10, max_value = 100, value = state.lln_n_sim if state.lln_n_sim else 50, step = 1)
        if(new_p == state.lln_p and new_n_sim == state.lln_n_sim ):
            plot_TF = True
            fig = bernoulli_dist(new_p, new_n_sim)
        else:
            state.lln_p, state.lln_n_sim = new_p, new_n_sim
    elif(option == "Geometric(p)"):
        state.index = 3
        new_p = st.sidebar.slider("p", min_value = 0.0, max_value = 1.0, value = state.lln_p if state.lln_p else 0.1, step = 0.05)
        if(new_p == state.lln_p):
            plot_TF = True
            pdf, simulation = bernoulli_dist(new_p, new_n_sim)
        else:
            state.lln_p, state.lln_n_sim = new_p, new_n_sim
    elif(option == "Binomial(n, p)"):
        state.index = 4
        fig = binom_dist(n, p, nlim)
    elif(option == "Poisson(λ)"):
        state.index = 5
        fig = poisson_dist(_lambda, nlim)
    elif(option == "Beta(α,β)"):
        state.index = 6
        fig = beta_dist(alpha, beta, nlim)
    elif(option == "Exp(λ)"):
        state.index = 7
        fig = exp_dist(_lambda, nlim)
    
    if(plot_TF):
        success = stEmpty()
        success.success("Loading...")
        plot = stEmpty()
        plot.plotly_chart(pdf, filename='latex', include_mathjax='cdn')
        plot = stEmpty()
        plot.plotly_chart(simulation, filename='latex', include_mathjax='cdn')
        
        success.empty()
                                          
                                          
    
if __name__ == '__main__':
    main()