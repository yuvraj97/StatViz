import os
from typing import Dict, Union, Tuple
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from plotly.graph_objs import Figure

from distribution import distributions_properties
from gui.utils import get_parameters
from logic.utils import plot_histogram


def stDisplay(dist: str,
              population: np.ndarray,
              sample: np.ndarray,
              _vars: Dict[str, Union[int, float]],
              n: Dict[str, int],
              mean: float,
              plots: Tuple[Figure, Figure],
              state) -> None:
    parameters: str = get_parameters(dist, _vars)
    pdf: Figure
    simulation: Figure
    pdf, simulation = plots

    total_population = str(n["population"])
    sample_size = str(n["samples"])

    image_path = os.path.join(os.getcwd(), "img" if state.theme != "dark" else "img-dark", "dogma.png")
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    st.markdown('[Remember the Central Dogma of Probability and Statistics](https://read.quantml.org/stats/#dogma)')
    truth = """- Data is drawn from a **""" + distributions_properties[dist]["name"] + "**, " + \
            distributions_properties[dist]["latex"] + """    
""" + parameters
    with st.beta_expander("Truth", expanded=True):
        st.markdown("""Let's, first define the **Truth**, in this case the truth is,""")
        st.markdown(truth)

    with st.beta_expander("Probability", expanded=True):
        st.markdown("""
        *Here we use probability to generate our data using the **Truth** we defined above.*   
        Using the knowledge of truth we generate a (synthetic) population of $""" + total_population + """$ observations.   
        """)

        # noinspection PyUnusedLocal
        fig, (counts, bins) = plot_histogram(population, {
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
        }, len(np.unique(population))//4)
        st.plotly_chart(fig, use_container_width=True)

        population = population.reshape((1, len(population)))
        population = pd.DataFrame(data=population, index=['Random draws'])
        population.columns += 1
        st.write(population)

        st.markdown("""
        These observations are *realization* of a **random process**,
        We call these observations as **Random variables**,
        in this case we have drawn these **random variables** from a """ + distributions_properties[dist][
            "name"] + ", " + distributions_properties[dist]["latex"] + """.    
        """)

    with st.beta_expander("Observation", expanded=True):
        st.markdown("""
        *Here we took a sample from our population.*   
        Now we have our $""" + total_population + """$ **observations**, we took a **sample** of $""" + sample_size + """$ observations.
        """)

        # noinspection PyUnusedLocal
        fig, (counts, bins) = plot_histogram(sample, {
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
        }, len(np.unique(sample))//2)
        st.plotly_chart(fig, use_container_width=True)

        sample = sample.reshape((1, len(sample)))
        sample = pd.DataFrame(data=sample, index=['Sample r.v.'])
        sample.columns += 1
        st.write(sample)

    with st.beta_expander("Statistics", expanded=True):
        st.plotly_chart(pdf, use_container_width=True)
        st.markdown("""
        So now we have $""" + sample_size + """$ Random variables,
        $X_1, X_2, \\cdots, X_{""" + sample_size + """}$.    
        According to **Law of Large Numbers**,    
        """)

        st.info("""
        Sample mean $(\\overline{X}_n)$ tends to the the **true mean** as
        Our sample size $\\to \\infty$
        """)

        st.latex("\\overline{X}_n:=\\frac{1}{n}\\sum _{i=1}^ n X_ i \\xrightarrow [n\\to \\infty ]{\\text{ a.s.}} \\mu")

        st.markdown("""    
        ## Estimation
        We can estimate **True mean $(\\mu)$** by taking the sample mean, and our estimate get better as our sample size increases.
        """)

        sample_mean = "{:.4f}".format(sample.iloc[0].mean())
        st.latex(
            "\\hat{\\mu} = \\frac{1}{" + sample_size + "}\\sum _{i=1}^ {" + sample_size + "} X_ i = " + sample_mean)
        st.info("Here our estimate is $\\hat\\mu=" + sample_mean + "$")

    st.markdown("""
    In the graph below you can see as we increases the Sample size, Sample mean goes toward true mean.    
    Here the **true mean** is $""" + "{:.4f}".format(mean) + """$
    """)
    st.plotly_chart(simulation, use_container_width=True)

    st.markdown("""
    
    """)

    st.markdown("""
    <blockquote class="success">
        If you spot any error then please tell me in our discussion form.<br>
        Also please share your experience, I'm eager to know if it really help you to understand/visualize
        <b>Weak Law of large Numbers</b>.
    </blockquote>""", unsafe_allow_html=True)
