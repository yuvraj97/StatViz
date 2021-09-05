import os
from typing import Union

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from plotly.graph_objs import Figure

from Chapters.utils.plots import plot_binary_data
from Chapters.Introduction.utils import run
from utils import set_get_URL
from Chapters.utils.utils import stPandas


def stDisplay(n_population: int, n_sample: int, true_p: float, n_simulations: int, seed: Union[int, None]):
    with st.beta_expander("Scenario", expanded=True):
        st.markdown("""
        Say we have a <b>room</b> full of <span class="l1">Red balls</span> and <span class="l2">Blue balls</span>. <br>
        We want to determine the proportions of
        <span class="l1">Red balls</span> and <span class="l2">Blue balls</span>.<br>
        But we can't count all the balls in the room as there are too many of them. <br>
        So instead what we can do is, we can take a <b>small sample</b> of <b>balls</b> from that <b>room</b>,
        then find the proportion of <span class="l1">Red balls</span> and <span class="l2">Blue balls</span>
        in that <b>sample</b> and hope that proportion we just estimated is somewhat near the
        <b>True proportion</b>(for the whole room). <br>
        """, unsafe_allow_html=True)

    st.markdown("""
    [Remember the Central Dogma of Probability and Statistics](https://read.quantml.org/statistics/introduction/#dogma)
    """)

    image_path: str = os.path.join(os.getcwd(), "img", "dogma.png")
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    with st.beta_expander("Truth", expanded=True):
        st.markdown("""
        First of all we need a room full of balls, 
        (here those balls will be generated by a computer) to fill the room with balls
        we need some underlying **Truth** that we describes in our left sidebar. <br>
        Here the **truth** is that, currently the <b>room</b> is holding
        <span class="l1">$40\\%$</span> of <span class="l1">Red balls</span> and
        <span class="l2">$60\\%$</span> of <span class="l2">Blue balls</span>. <br>
        <blockquote class="warning">
            Note that we do <b>not</b> know this proportion and our intent is to find this proportion.
        </blockquote>
        """, unsafe_allow_html=True)

    population_plot: Figure = plot_binary_data({
        "title": "Population",
        "legend-1": "Red Balls",
        "legend-2": "Blue Balls",
        "count-1": int(n_population * true_p),
        "count-2": n_population - int(n_population * true_p),
        "description-1": "Red Ball",
        "description-2": "Blue Ball"
    }, seed)

    with st.beta_expander("Probability", expanded=True):
        st.markdown(f"""
        Now let's create a <b>Population</b>(<i>"All the balls in the room"</i>), 
        here we use probability to generate our data using the <b>Truth</b> we defined above. <br>
        **Probability** tells us what our data looks like, as we know that $p = {true_p}$
        so using this probability we generate(synthetic) data.
        """, unsafe_allow_html=True)

        population_sample: np.ndarray
        samples: list
        fig: Figure
        estimate: float
        estimators: np.ndarray
        population_sample, samples, fig, estimate, estimators = run(n_population,
                                                                    n_sample,
                                                                    true_p,
                                                                    n_simulations,
                                                                    "Simulated Distribution",
                                                                    seed)

        population_sample: pd.DataFrame = stPandas(population_sample, "Population")

        st.plotly_chart(population_plot)

        st.markdown("""
        Now let's denote
        <span class="l1">Red balls</span> by <span class="l1">"$1$"</span>  and
        <span class="l2">Blue balls</span> by <span class="l2">"$0$"</span>.
        """, unsafe_allow_html=True)
        st.write(population_sample)

    sample_plot = plot_binary_data({
        "title": "Sample",
        "legend-1": "Red Balls",
        "legend-2": "Blue Balls",
        "count-1": int(n_population * true_p),
        "count-2": n_population - int(n_population * true_p),
        "description-1": "Red Ball",
        "description-2": "Blue Ball"
    }, seed)

    with st.beta_expander("Observation", expanded=True):
        st.markdown(f"""
        As we can see the room is full of ${n_population}$ balls, and we can't count all of them 
        to find out the proportion of <span class="l1">Red balls</span> and <span class="l2">Blue balls</span>. <br>
        So we took a sample of ${n_sample}$ balls out of those ${n_population}$ balls to find the proportion of
        <span class="l1">Red balls</span> and <span class="l2">Blue balls</span> in that room. <br>
        """, unsafe_allow_html=True)

        st.plotly_chart(sample_plot)
        st.write(stPandas(samples[0], "Sample"))

    redBalls: list = [sample.sum() for sample in samples]

    with st.beta_expander("Statistics", expanded=True):
        st.markdown(f"""
        So now we have our sample of ${n_sample}$ balls, let's start finding an estimate for
        <span class="l1">Red balls</span> proportion and
        <span class="l2">Blue balls</span> proportion. <br>
        To find the proportion of <span class="l1">Red balls</span>,
        we count number of <span class="l1">Red balls</span>
        then we divide it by total number of balls (i.e. ${n_sample}$). <br>
        <span class="l1">$\\hat{{p}}$</span>:
        our estimate for proportion of <span class="l1">Red balls</span> denoted by $1$. <br>
        <span class="l2">$\\hat{{q}}$</span>:
        our estimate for proportion of <span class="l2">Blue balls</span> denoted by $0$. <br>
        """, unsafe_allow_html=True)

        st.latex(f"\\hat{{p}} = \\frac{1}{{{n_sample}}}\\sum_{{i=0}}^{{{n_sample}}}X_i ")
        st.latex(" \\hat{q} = 1-\\hat{p} ")

        st.markdown(f"""In our sample we have ${redBalls[0]}$ <span class="l1">red balls</span> and 
        ${n_sample - redBalls[0]}$ <span class="l2">blue balls</span>, so for this sample
        our estimate for the proportion of <span class="l1">red balls</span> is
        $\\hat{{p}} = {redBalls[0]}/{n_sample}={redBalls[0] / n_sample}$
        """, unsafe_allow_html=True)

    tex: list = []
    for i in range(5):
        t = f"$\\widehat{{p}} = {int(estimators[i] * n_sample)}/{n_sample} = {'{:.4f}'.format(estimators[i])}$"
        tex.append(t)

    st.markdown(f"""
    This estimate is a result of a single simulation, if we perform this simulation multiple times, i.e. collecting 
    samples from same population multiple times, we can get a better picture of our estimator. <br>
    By collecting multiple sample we can see how our estimator is distributed. <br>
    Let's collect samples, <br>
    We have {n_simulations} samples, let's see first $3$ samples, <br>
    #### Experiment 1: 
    *   In first experiment out of ${n_sample}$,  ${int(estimators[0] * n_sample)}$ balls are 
        <span class="l1">red balls</span>.    
        So estimate for first experiment is {tex[0]}    
    #### Experiment 2: 
    *   In second experiment out of ${n_sample}$,  ${int(estimators[1] * n_sample)}$ balls are
        <span class="l1">red balls</span>.    
        So estimate for first experiment is {tex[1]}    
    #### Experiment 3: 
    *   In third experiment out of ${n_sample}$,  ${int(estimators[2] * n_sample)}$ balls are
        <span class="l1">red balls</span>.        
        So estimate for first experiment is {tex[2]}
        
    Now if we plot a histogram of our estimators we can see how our estimator $(\\hat{{p}})$ is distributed.    
    """, unsafe_allow_html=True)
    st.plotly_chart(fig)

    st.markdown("""
    <blockquote class="success">
        If you spot any error then please tell me in our discussion form.<br>
        Also please share your experience, I'm eager to know if this help you understand,
        <b>what is Statistics?</b>
    </blockquote>""", unsafe_allow_html=True)


def main(state):
    set_get_URL(parameters={
        "dist": "remove",
        "topic": "remove"
    })

    seed: Union[int, None] = st.sidebar.number_input(
        "Enter Seed (-1 mean seed is disabled)",
        min_value=-1,
        max_value=10000,
        value=0,
        step=1
    )

    if seed == -1: seed = None

    n_population: int = st.sidebar.number_input("Enter population size",
                                                min_value=100,
                                                max_value=400,
                                                value=200)
    n_sample: int = st.sidebar.number_input("Enter sample size",
                                            min_value=10,
                                            max_value=50,
                                            value=30)
    true_p: float = st.sidebar.slider("Proportion of Red balls (p)",
                                      min_value=0.0,
                                      max_value=1.0,
                                      value=0.5,
                                      step=0.05)
    n_simulations: int = st.sidebar.number_input("Enter number of simulation",
                                                 min_value=10,
                                                 max_value=50,
                                                 value=50)

    stDisplay(n_population, n_sample, true_p, n_simulations, seed)
