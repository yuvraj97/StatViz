# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 04:32:01 2020

@author: OS
"""

import os
import streamlit as st
import pandas as pd
from PIL import Image
from distribution import distributions_properties

def stDisplay(dist, parameters, population, sample, n, mean, pdf, simulation, state):
    #print("            - definitions(state, distribution=" + str(distribution) + ", parameters="+ str(parameters) + ", population=" + str(population) + ", sample=" + str(sample) + ")")

    total_population = str(n["population"])
    sample_size = str(n["samples"])
    mean = "{:.4f}".format(mean)
    sample_mean = "{:.4f}".format(sample.iloc[0].mean())
    
    image_path = os.path.join(os.getcwd(), "img" if state.theme != "dark" else "img-dark","dogma.png")
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    st.markdown('[Remember the Central Dogma of Probability and Statistics](https://read.quantml.org/stats/#dogma)')
    truth = """- Data is drawn from a **"""+distributions_properties[dist]["name"]+"**, "+distributions_properties[dist]["latex"]+"""    
""" + parameters
    with st.beta_expander("Truth", expanded=True):
        st.markdown("""Let's, first define the **Truth**, in this case the truth is,""")
        st.markdown(truth)
        
    with st.beta_expander("Probability", expanded=True):
        st.markdown("""
        *Here we use probability to generate our data using the **Truth** we defined above.*   
        Using the knowledge of truth we generate a (synthetic) population of $"""+total_population+"""$ observations.   
        """)
        st.write(population)
        
        st.markdown("""
        These observations are *realization* of a **random process**,
        We call these observations as **Random variables**,
        in this case we have drawn these **random variables** from a """ +distributions_properties[dist]["name"]+ ", " +distributions_properties[dist]["latex"]+ """.    
        """)

    with st.beta_expander("Observation", expanded=True):
        st.markdown("""
        *Here we took a sample from our population.*   
        Now we have our $""" + total_population + """$ **observations**, we took a **sample** of $""" + sample_size + """$ observations.
        """)
        st.write(sample)
    
    with st.beta_expander("Statistics", expanded=True):
        st.plotly_chart(pdf, use_container_width=True)
        st.markdown("""
        So now we have $"""+sample_size+"""$ Random variables,
        $X_1, X_2, \\cdots, X_{""" +sample_size+"""}$.    
        According to **Law of Large Numbers**,    
        
        > Sample mean $(\\overline{X}_n)$ tends to the the **true mean** as
        **Our sample size $\\to \\infty$**""")
        
        st.latex("\\overline{X}_n:=\\frac{1}{n}\\sum _{i=1}^ n X_ i \\xrightarrow [n\\to \\infty ]{\\text{ a.s.}} \\mu")    

        st.markdown("""    
        ## Estimation
        We can estimate **True mean $(\\mu)$** by taking the sample mean, and our estimate get better as our sample size increases.
        """)

        st.latex("\\hat{\\mu} = \\frac{1}{"+ sample_size +"}\\sum _{i=1}^ {"+ sample_size +"} X_ i = "+ sample_mean  )
        st.info("Here our estimate is $\\hat\\mu="+ sample_mean +"$")
    
    st.markdown("""
    In the graph below you can see as we increases the Sample size, Sample mean goes toward true mean.    
    Here the **true mean** is $""" + mean + """$
    """)
    st.plotly_chart(simulation, use_container_width=True)

    st.markdown("""
    
    """)



def get_parameters(dist, vars):
    #print("            - parameters(dist="+ dist + ", vars="+ str(vars) +")")
    parameters = ""
    i = 0
    for parameter in distributions_properties[dist]["stSlider"]:
        parameters += """- """ + distributions_properties[dist]["parameters"][i] + """: $""" +str(vars[parameter]) +"""$
"""
        i += 1
    return parameters

def run(dist, population, sample, vars, n, mean, pdf, simulation, state):
    #print("          - definitions(dist=" + str(dist) + ", population="+ str(population) + ", sample=" + str(sample) + ")")
    population = population.reshape((1,len(population)))
    population = pd.DataFrame(data=population, index=['Random draws'])
    population.columns += 1
    sample = sample.reshape((1,len(sample)))
    sample = pd.DataFrame(data=sample, index=['Sample r.v.'])
    sample.columns += 1
    stDisplay(dist, get_parameters(dist, vars), population, sample, n, mean, pdf, simulation, state)