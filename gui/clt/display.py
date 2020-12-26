import os
from PIL import Image
from typing import Dict, Union
import streamlit as st
import scipy.stats
from scipy.stats import norm
import numpy as np
import pandas as pd
from gui.utils import get_parameters
from distribution import distributions_properties, get_distribution  # graph_label
from logic.utils import plot_histogram, line_plot

def stDisplay(dist: str, _vars: Dict[str, Union[int, float]], n: Dict[str, int], state):

    n_population = n["population"]
    n_sample = n["samples"]
    n_simulations = n["simulations"]

    with st.beta_expander("Scenario", expanded=True):
        st.markdown(f"""
        Assume that there are ${n_population}$ students in your school and you want to know,
        what is the average height of ${n_sample}$ randomly selected students?
        and how is that average height is distributed (or say the distribution of that average height)?<br>
        """, unsafe_allow_html=True)
        # distributions_properties[dist]["name"]

    with st.beta_expander("How CLT can help us", expanded=True):
        st.markdown("Central Limit Theorem says that,")
        st.info(f"""
        As $n\\to \\infty$ then **CDF** ([cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function))
        of the Sampling distribution (say $Z_n$) converges to the **CDF** of Standard Normal distribution (say $Z$).
        """)
        st.markdown(f"""
        But we wont need $\\infty$ sample size $(n)$, $n\\geq 30$ will suffice.<br>
        So no matter what the distribution is, as long as it had a finite mean and a finite variance
        (unlike <a href="https://en.wikipedia.org/wiki/Cauchy_distribution">cauchy distribution</a>),
        distribution of sample mean will converge to the <b>Normal Distribution</b>.
        """, unsafe_allow_html=True)
    st.markdown("[Remember the Central Dogma of Probability and Statistics](https://read.quantml.org/stats/#dogma)")

    image_path = os.path.join(os.getcwd(), "img-dark" if state.theme == "dark" else "img", "dogma.png")
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    parameters: str = get_parameters(dist, _vars)

    with st.beta_expander("Truth", expanded=True):
        st.markdown("""Let's, first define the **Truth**, in this case the truth is,""")
        st.markdown(f"""
        - Data is drawn from a **{distributions_properties[dist]["name"]}**,
        {distributions_properties[dist]["latex"]}     
{parameters}
        """)

    with st.beta_expander("Probability", expanded=True):
        st.markdown(f"""
        Now we have defined that students height is distributed according to {distributions_properties[dist]["name"]}.   
        So let's create a population of ${n_population}$ students.
        """)
        _vars = [_vars[k] for k in _vars.keys()]
        distribution: Union[scipy.stats.rv_continuous, scipy.stats.rv_discrete] = get_distribution(dist, _vars)
        if state.stSettings["seed"] is not None: np.random.seed(state.stSettings["seed"])
        population: Union[np.ndarray, int, float, complex] = distribution.rvs(size=n_population)
        fig, (counts, bins) = plot_histogram(population,
            description={
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
            num_bins=len(np.unique(population)) // 4)
        st.plotly_chart(fig, use_container_width=True)

        population_pd: pd.DataFrame = pd.DataFrame(data=population.reshape((1, len(population))), index=['Random draws'])
        population_pd.columns += 1
        st.write(population_pd)

        del population_pd

        st.markdown(f"""
        These observations are *realization* of a **random process**,
        We call these observations as **Random variables**,
        in this case we have drawn these **random variables** from a
        **{distributions_properties[dist]["name"]}**, {distributions_properties[dist]["latex"]}.    
        """)

    sample_means = np.zeros(n_simulations)
    samples = []
    for k in range(n_simulations):
        sample = np.random.choice(population, n_sample)
        samples.append(sample)
        sample_means[k]=np.mean(sample)

    with st.beta_expander("Observation", expanded=True):
        st.markdown(f"""
        Now lets take ${n_simulations}$ samples from our population of ${n_population}$ students, and each sample
        consists of ${n_sample}$ observations of random student's height.    
        Let's see first $3$ samples.
        """)

        for i in range(3):
            population_pd: pd.DataFrame = pd.DataFrame(data=samples[i].reshape((1, n_sample)),
                                                       index=[f"Sample {i+1}"])
            population_pd.columns += 1
            st.write(population_pd)

            del population_pd
        if st.checkbox("Show all samples", False):
            for i in range(3,n_simulations):
                population_pd: pd.DataFrame = pd.DataFrame(data=samples[i].reshape((1, n_sample)),
                                                           index=[f"Sample {i + 1}"])
                population_pd.columns += 1
                st.write(population_pd)

                del population_pd
        del samples

    with st.beta_expander("Statistics", expanded=True):
        st.markdown(f"""
        Now we have {n_simulations} samples.   
        According to **CLT** distribution of sample mean $\\overline X_n$ converges to Normal distribution for larger
        sample size $(n)$, here we set $n={n_sample}$, let's see the shape of our Sampling distribution.
        """)

        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        true_estimated = st.radio("For Normal distribution", ("Use Estimated mean & variance", "Use True mean & variance"))
        use_estimated = True if true_estimated == "Use Estimated mean & variance" else False

        col = st.beta_columns([1, 30])
        with col[0]:
            use_centered_dist = st.checkbox(" ", False)
        with col[1]:
            st.markdown(
                "Use Sampling distribution of $\\sqrt{n}(\\overline{X}_n - \\mu)$ instead of $\\overline{X}_n$")


        fig, (counts, bins) = plot_histogram(
            sample_means if not use_centered_dist else np.sqrt(n_sample) * (sample_means - distribution.mean()),
            description={
                "title": {
                    "main": "Sampling Distribution",
                    "x": "Sample mean",
                    "y": "# occurrence of sample mean"
                },
                "label": {
                    "main": "Sampling Distribution",
                    "x": "Sample mean",
                    "y": "# occurrence of sample mean<br>falling into particular bin"
                }
            },
            num_bins=len(np.unique(sample_means)) // 2,
            convert_into_probability_plot=True,
            isMobile=state.isMobile)

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        Our Sampling distribution seems to have a bell curve, Now let's overlay a Normal distribution with same mean
        and variance as of our Sampling distribution.""")

        if use_centered_dist:
            # st.info(f"True std: {distribution.std()}, **Estimated std**: {np.sqrt(n_sample) * np.std(sample_means)}")
            mean = 0 if not use_estimated else np.mean(np.sqrt(n_sample) * (sample_means - distribution.mean()))
            std = distribution.std() if not use_estimated else np.sqrt(n_sample) * np.std(sample_means)
        else:
            mean = distribution.mean() if not use_estimated else np.mean(sample_means)
            std  = distribution.std()/np.sqrt(n_sample) if not use_estimated else np.std(sample_means)
        iid_rvs = np.linspace(mean - 3 * std, mean + 3 * std, 100)
        line_plot(x=iid_rvs,
                  y=norm.pdf(iid_rvs, mean, std),
                  description={
                      "title": {
                          "main": f"Sampling Distribution/<br>Normal Distribution N(μ={'{:.4f}'.format(mean)}, σ={'{:.4f}'.format(std)})",
                          "x": f"Sample mean/<br>Random draw from N(μ={'{:.4f}'.format(mean)}, σ={'{:.4f}'.format(std)})",
                          "y": "Probability of Sample mean/<br>PDF of Normal Distribution"
                      },
                      "label": {
                          "main": "Normal distribution"
                      },
                      "hovertemplate": "Random draw(x): %{x}<br>PDF(x=%{x}): %{y}",
                      "color": "green"
                  },
                  fig=fig)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    [As we discussed](https://read.quantml.org/stats/clt/#its-about-CDF)""")
    st.info("""**Central Limit Theorem** is **not** a statement about the convergence of PDF or PMF.
    It's a statement about the convergence of **CDF**.""")
    st.markdown("Now let's see that do the **CDF** of our Sampling distribution approaches to the CDF of a Normal Distribution")

    fig = line_plot(x=iid_rvs,
                    y=norm.cdf(iid_rvs, mean, std),
                    description={
                          "label": {
                              "main": "Normal distribution CDF"
                          },
                          "hovertemplate": "Random draw(x): %{x}<br>CDF(x=%{x}): %{y}",
                          "color": "green"
                    },
                    mode="lines")
    fig = line_plot(x=bins,
                    y=np.cumsum(counts)/np.sum(counts),
                    description={
                        "label": {
                            "main": "Sampling Distribution CDF"
                        },
                        "hovertemplate": "Sample Average(x) ~ %{x}<br>CDF(x ~ %{x}): %{y}",
                        "color": "royalblue"
                    },
                    mode="markers",
                    fig=fig)

    st.plotly_chart(fig, use_container_width=True)