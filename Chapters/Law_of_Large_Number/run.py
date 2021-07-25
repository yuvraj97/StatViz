import os
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from plotly.graph_objs import Figure
from typing import Union, Dict

import Chapters.Law_of_Large_Number.utils as lln
from Chapters.utils.utils import get_parameters
from Chapters.utils.plots import plot_histogram
from distribution import distributions_properties, stDistribution
from utils import set_get_URL, urlIndex


def stDisplay(
        dist_vars: Dict[str, Union[str, int, None, Dict[str, int]]],
        dist_params: Dict[str, Union[int, float]],
        var: Dict[str, Union[float, np.ndarray, Figure]],
        state) -> None:

    parameters: str = get_parameters(dist_vars["dist"], dist_params)
    pdf: Figure
    simulation: Figure
    pdf, simulation = var["pdf_plot"], var["simulation_plot"]

    image_path = os.path.join(os.getcwd(), "img" if state.theme != "dark" else "img-dark", "dogma.png")
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    st.markdown("""
    [Remember the Central Dogma of Probability and Statistics](https://read.quantml.org/statistics/introduction/#dogma)
    """)
    truth = f"""- Data is drawn from a **{distributions_properties[dist_vars["dist"]]["name"]}**,
        {distributions_properties[dist_vars["dist"]]["latex"]}   
        
{parameters}
        """
    with st.beta_expander("Truth", expanded=True):
        st.markdown("""Let's, first define the **Truth**, in this case the truth is,""")
        st.markdown(truth)

    with st.beta_expander("Probability", expanded=True):
        st.markdown(f"""
        *Here we use probability to generate our data using the **Truth** we defined above.*   
        Using the knowledge of truth we generate a (synthetic) population of
        ${dist_vars["n"]["population"]}$ observations.  
        """)

        population: np.ndarray = var["population"]
        fig, _ = plot_histogram(
            population,
            {
                "title": {
                    "main": "Population",
                    "x": "Random Variable",
                    "y": "# occurrence of certain random variable"
                },
                "label": {
                    "main": None,
                    "x": "Height",
                    "y": "# occurrence"
                }
            },
            len(np.unique(population)) // 4
        )
        st.plotly_chart(fig, use_container_width=True)

        population = population.reshape((1, len(population)))
        population_df = pd.DataFrame(data=population, index=['Random draws'])
        population_df.columns += 1
        st.write(population_df)

        st.markdown(f"""
        These observations are *realization* of a **random process**,
        We call these observations as **Random variables**,
        in this case we have drawn these **random variables** from a 
        **{distributions_properties[dist_vars["dist"]]["name"]}**,
        {distributions_properties[dist_vars["dist"]]["latex"]}""")

    with st.beta_expander("Observation", expanded=True):
        st.markdown(f"""
        *Here we took a sample from our population.*   
        Now we have our ${dist_vars["n"]["population"]}$ **observations**,
        we took a **sample** of ${dist_vars["n"]["samples"]}$ observations.
        """)

        sample = var["iid_rvs"]
        # noinspection PyUnusedLocal
        fig, _ = plot_histogram(
            sample,
            {
                "title": {
                    "main": "Sample",
                    "x": "Random Variable",
                    "y": "# occurrence of certain random variable"
                },
                "label": {
                    "main": None,
                    "x": "Height",
                    "y": "# occurrence"
                }
            },
            len(np.unique(sample)) // 2
        )
        st.plotly_chart(fig, use_container_width=True)

        sample = sample.reshape((1, len(sample)))
        sample = pd.DataFrame(data=sample, index=['Sample r.v.'])
        sample.columns += 1
        st.write(sample)

    with st.beta_expander("Statistics", expanded=True):
        st.plotly_chart(pdf, use_container_width=True)
        st.markdown(f"""
        So now we have ${dist_vars["n"]["samples"]}$ Random variables,
        $X_1, X_2, \\cdots, X_{{{dist_vars["n"]["samples"]}}}$.    
        According to **Law of Large Numbers**,    
        """)

        st.info("""
        Sample mean $(\\overline{X}_n)$ tends to the the **true mean** as
        Our sample size $\\to \\infty$
        """)

        st.latex("\\overline{X}_n:=\\frac{1}{n}\\sum _{i=1}^ n X_ i \\xrightarrow [n\\to \\infty ]{\\text{ a.s.}} \\mu")

        st.markdown("""    
        ## Estimation
        We can estimate **True mean $(\\mu)$** by taking the sample mean,
        and our estimate get better as our sample size increases.
        """)

        sample_mean = "{:.4f}".format(sample.iloc[0].mean())
        st.latex(
            f"\\hat{{\\mu}} = \\frac{{1}}{{{dist_vars['n']['samples']}}}"
            f"\\sum _{{i=1}}^ {{{dist_vars['n']['samples']}}} X_ i =  {sample_mean}"
        )
        st.info("Here our estimate is $\\hat\\mu=" + sample_mean + "$")

    st.markdown(f"""
    In the graph below you can see as we increases the Sample size, Sample mean goes toward true mean.    
    Here the **true mean** is ${"{:.4f}".format(var["mean"])}$
    """)
    st.plotly_chart(simulation, use_container_width=True)

    st.markdown("""
    If you spot any error then please tell me in our discussion form.  
    Also please share your experience, I'm eager to know if it really help you to understand/visualize
    **Weak Law of large Numbers**.
    """)


def main(state):
    dist_vars: Dict[str, Union[str, int, None, Dict[str, int]]]
    dist_params: Dict[str, Union[int, float]]
    dist_vars, dist_params = stDistribution(urlIndex(state.url))

    set_get_URL(parameters={
        "dist": distributions_properties[dist_vars["dist"]]["name"],
        "topic": "remove"
    })

    var: Dict[str, Union[float, np.ndarray, Figure]] = lln.run(
        dist_vars["dist"], dist_params, dist_vars["n"], state, dist_vars["seed"]
    )

    stDisplay(dist_vars, dist_params, var, state)
