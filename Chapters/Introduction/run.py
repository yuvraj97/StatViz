import os
from typing import Union, Dict

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from plotly.graph_objs import Figure

from Chapters.utilities.plots import plot_binary_data
from Chapters.Introduction.utils import run
from utilities.ui import footer
from utilities.utils import set_get_URL, check_input_limits
from Chapters.utilities.lite_utils import stPandas


def stDisplay(inputs: Dict[str, Union[int, None, float]]):

    n_population: int = inputs["n_population"]
    n_samples: int = inputs["n_samples"]
    true_p: float = inputs["p"]
    n_simulations: int = inputs["n_simulations"]
    seed: Union[int, None] = inputs["seed"]

    with st.expander("Scenario", expanded=True):
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

    with st.expander("Truth", expanded=True):
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

    with st.expander("Probability", expanded=True):
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
                                                                    n_samples,
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

    with st.expander("Observation", expanded=True):
        st.markdown(f"""
        As we can see the room is full of ${n_population}$ balls, and we can't count all of them 
        to find out the proportion of <span class="l1">Red balls</span> and <span class="l2">Blue balls</span>. <br>
        So we took a sample of ${n_samples}$ balls out of those ${n_population}$ balls to find the proportion of
        <span class="l1">Red balls</span> and <span class="l2">Blue balls</span> in that room. <br>
        """, unsafe_allow_html=True)

        st.plotly_chart(sample_plot)
        st.write(stPandas(samples[0], "Sample"))

    redBalls: list = [sample.sum() for sample in samples]

    with st.expander("Statistics", expanded=True):
        st.markdown(f"""
        So now we have our sample of ${n_samples}$ balls, let's start finding an estimate for
        <span class="l1">Red balls</span> proportion and
        <span class="l2">Blue balls</span> proportion. <br>
        To find the proportion of <span class="l1">Red balls</span>,
        we count number of <span class="l1">Red balls</span>
        then we divide it by total number of balls (i.e. ${n_samples}$). <br>
        <span class="l1">$\\hat{{p}}$</span>:
        our estimate for proportion of <span class="l1">Red balls</span> denoted by $1$. <br>
        <span class="l2">$\\hat{{q}}$</span>:
        our estimate for proportion of <span class="l2">Blue balls</span> denoted by $0$. <br>
        """, unsafe_allow_html=True)

        st.latex(f"\\hat{{p}} = \\frac{1}{{{n_samples}}}\\sum_{{i=0}}^{{{n_samples}}}X_i ")
        st.latex(" \\hat{q} = 1-\\hat{p} ")

        st.markdown(f"""In our sample we have ${redBalls[0]}$ <span class="l1">red balls</span> and 
        ${n_samples - redBalls[0]}$ <span class="l2">blue balls</span>, so for this sample
        our estimate for the proportion of <span class="l1">red balls</span> is
        $\\hat{{p}} = {redBalls[0]}/{n_samples}={redBalls[0] / n_samples}$
        """, unsafe_allow_html=True)

    tex: list = []
    for i in range(5):
        t = f"$\\widehat{{p}} = {int(estimators[i] * n_samples)}/{n_samples} = {'{:.4f}'.format(estimators[i])}$"
        tex.append(t)

    st.markdown(f"""
    This estimate is a result of a single simulation, if we perform this simulation multiple times, i.e. collecting 
    samples from same population multiple times, we can get a better picture of our estimator. <br>
    By collecting multiple sample we can see how our estimator is distributed. <br>
    Let's collect samples, <br>
    We have {n_simulations} samples, let's see first $3$ samples, <br>
    #### Experiment 1: 
    *   In first experiment out of ${n_samples}$,  ${int(estimators[0] * n_samples)}$ balls are 
        <span class="l1">red balls</span>.    
        So estimate for first experiment is {tex[0]}    
    #### Experiment 2: 
    *   In second experiment out of ${n_samples}$,  ${int(estimators[1] * n_samples)}$ balls are
        <span class="l1">red balls</span>.    
        So estimate for first experiment is {tex[1]}    
    #### Experiment 3: 
    *   In third experiment out of ${n_samples}$,  ${int(estimators[2] * n_samples)}$ balls are
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


def main():

    set_get_URL(parameters={
        "dist": "remove",
        "topic": "remove"
    })

    st_seed, st_n_population = st.sidebar.columns([1, 1])
    seed: Union[int, None] = int(st_seed.text_input("Enter Seed (-1 mean seed is disabled)", "0"))
    n_population: int = int(st_n_population.text_input("Enter population size", "200"))

    st_n_sample, st_n_simulation = st.sidebar.columns([1, 1])
    n_samples: int = int(st_n_sample.text_input("Enter sample size", "30"))
    n_simulations: int = int(st_n_simulation.text_input("Enter number of simulation", "50"))
    true_p: float = float(st.sidebar.text_input("Proportion of Red balls (p)", "0.5"))

    inputs: Dict[str, Union[int, None, float]] = {
        "seed": seed,
        "n_population": n_population,
        "n_samples": n_samples,
        "n_simulations": n_simulations,
        "p": true_p
    }

    if not check_input_limits(inputs):
        return

    stDisplay(inputs)

