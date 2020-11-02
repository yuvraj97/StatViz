# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 04:32:01 2020

@author: OS
"""

import streamlit as st
import pandas as pd

def dist_properties(dist, var):
    print("\t \t lln.utils.dist_prop")
    if(dist =="gauss"):
        distribution = {
                    "id": "gauss",
                    "name": "Normal distribution",
                    "latex": "$\\mathcal{N}(\\mu,\\sigma)$",
                    "latex-val": "$\\mathcal{N}(\\mu="+str(var["mu"])+",\\sigma="+str(var["sigma"])+")$",
                    "var": var
                   }
    elif(dist =="unif"):
        distribution = {
                    "id": "unif",
                    "name": "Uniform distribution",
                    "latex": "$\\mathcal{U}([a,b])$",
                    "latex-val": "$\\mathcal{U}(a="+str(var["a"])+",b="+str(var["b"])+")$",
                    "var": var
                   }
    elif(dist =="ber"):
        distribution = {
                    "id": "ber",
                    "name": "Bernoulli distribution",
                    "latex": "$\\text{Ber}(p)$",
                    "latex-val": "$\\text{Ber}(p="+str(var["p"])+")$",
                    "var": var
                   }
    elif(dist =="geo"):
        distribution = {
                    "id": "geo",
                    "name": "Geometric distribution",
                    "latex": "$\\text{Geo}(p)$",
                    "latex-val": "$\\text{Geo}(p="+str(var["p"])+")$",
                    "var": var
                   }
    elif(dist =="bin"):
        distribution = {
                    "id": "bin",
                    "name": "Binomial distribution",
                    "latex": "$\\text{Bin}(n, p)$",
                    "latex-val": "$\\text{Bin}(n="+str(var["n"])+",p="+str(var["p"])+")$",
                    "var": var
                   }
    elif(dist =="poiss"):
        distribution = {
                    "id": "poiss",
                    "name": "Poisson distribution",
                    "latex": "$\\text{Poisson}(\\lambda)$",
                    "latex-val": "$\\text{Poisson}(\\lambda="+str(var["lambda"])+")$",
                    "var": var
                   }
    elif(dist =="beta"):
        distribution = {
                    "id": "beta",
                    "name": "Beta distribution",
                    "latex": "$\\text{Beta}([\\alpha, \\beta])$",
                    "latex-val": "$\\text{Beta}(\\alpha="+str(var["a"])+",\\beta="+str(var["b"])+")$",
                    "var": var
                   }
    elif(dist =="exp"):
        distribution = {
                    "id": "exp",
                    "name": "Exponential distribution",
                    "latex": "$\\text{Exp}(\\lambda)$",
                    "latex-val": "$\\text{Exp}(\\lambda="+str(var["lambda"])+")$",
                    "var": var
                   }
    print("\t \t returning,",dist)
    return distribution

def definition(state, distribution, parameters, population, sample):
    total_population = str(state.lln["n_population"])
    sample_size = str(state.lln[distribution["id"]]["n_sample"])
    
    r = """
    # Truth
    Firstly, we define the **Truth**, in this case the truth is,     
    
    - Data is drawn from a **"""+distribution["name"]+"** "+distribution["latex"]+"""     
    """+parameters+ """
    
    # Probability
    *Here we use probability to generate our data using the **Truth** we defined above.*   
    Using the knowledge of truth we generate a (synthetic) population of $"""+total_population+"""$ observations.   
    """
    st.markdown(r)
    st.write(population)
    
    r = """
    These observations are *realization* of a **random process**,
    We call these observations as **Random variables**,
    in this case we have drawn these **random variables** from a """ +distribution["name"]+ " " +distribution["latex"]+ """.    
    
    # Observation
    *Here we took a sample from our population.*   
    Now we have our $""" + total_population + """$ **observations**, we took a **sample** of $""" + sample_size + """$ observations."""
    st.markdown(r)

    st.write(sample)
    
    
    r = """
    # Statistics
    
    So now we have $"""+sample_size+"""$ Random variables,
    $X_1, X_2, \cdots, X_{""" +sample_size+"""}$.    
    According to **Law of Large Numbers**,    
    
    > Sample Average $(\\overline{X}_n)$ tends to the the **true mean** as
      **Our sample size $\\to \\infty$**"""
    
    st.markdown(r)
    st.latex("\\overline{X}_n:=\\frac{1}{n}\\sum _{i=1}^ n X_ i \\xrightarrow [n\\to \\infty ]{\\text{ a.s.}} \\mu")    

    r = """    
    ## Estimation
    We can estimate **True mean $(\\mu)$** by taking the sample average, and our estimate get better as our sample size increases.
          
    """
    st.markdown(r)
    st.latex("\\hat{\\mu} = \\frac{1}{"+ sample_size +"}\\sum _{i=1}^ {"+ sample_size +"} X_ i = "+ "{:.4f}".format(sample.iloc[0].mean())  )


def parameters(distribution, state):
    print("\t ######## lln.run ########")
    if(dist == "gauss"):
        parameters = """- $\\text{mean}(\\mu): """ +str(state.lln[distribution["id"]]["mu"])+ """$    
    - $\\text{standard deviation}(\\sigma): """+str(state.lln[distribution["id"]]["sigma"])+"""$    
    """
    elif(dist == "unif"):
        parameters = """- $\\text{mean}(\\mu): """ +str(state.lln[distribution["id"]]["mu"])+ """$    
    - $\\text{standard deviation}(\\sigma): """+str(state.lln[distribution["id"]]["sigma"])+"""$    
    """
    elif(dist == "ber"):
        parameters = """- $\\text{mean}(\\mu): """ +str(state.lln[distribution["id"]]["mu"])+ """$    
    - $\\text{standard deviation}(\\sigma): """+str(state.lln[distribution["id"]]["sigma"])+"""$    
    """
    elif(dist == "geo"):
        parameters = """- $\\text{mean}(\\mu): """ +str(state.lln[distribution["id"]]["mu"])+ """$    
    - $\\text{standard deviation}(\\sigma): """+str(state.lln[distribution["id"]]["sigma"])+"""$    
    """
    elif(dist == "bin"):
        parameters = """- $\\text{mean}(\\mu): """ +str(state.lln[distribution["id"]]["mu"])+ """$    
    - $\\text{standard deviation}(\\sigma): """+str(state.lln[distribution["id"]]["sigma"])+"""$    
    """
    elif(dist == "poiss"):
        parameters = """- $\\text{mean}(\\mu): """ +str(state.lln[distribution["id"]]["mu"])+ """$    
    - $\\text{standard deviation}(\\sigma): """+str(state.lln[distribution["id"]]["sigma"])+"""$    
    """
    elif(dist == "beta"):
        parameters = """- $\\text{mean}(\\mu): """ +str(state.lln[distribution["id"]]["mu"])+ """$    
    - $\\text{standard deviation}(\\sigma): """+str(state.lln[distribution["id"]]["sigma"])+"""$    
    """
    return parameters

def run(state, distribution, population, sample):
    population = population.reshape((1,len(population)))
    population = pd.DataFrame(data=population, index=['Random draws'])
    population.columns += 1
    sample = sample.reshape((1,len(sample)))
    sample = pd.DataFrame(data=sample, index=['Sample r.v.'])
    sample.columns += 1
    #distribution = {
    #                "id": "gauss",
    #                "name": "Normal distribution",
    #                "latex": "$\\mathcal{N}(\\mu,\\sigma)$",
    #                "mean": 0
    #               }
    definition(state, distribution, parameters(distribution, state), population, sample)