from typing import Union

import streamlit as st
import numpy as np
import pandas as pd
from pandas import DataFrame
from scipy.stats import norm
from Chapters.utils.utils import stPandas
from Chapters.utils.plots import plot_histogram, line_plot


def run():

    st.markdown("""
    We can find Random walk everywhere like in
    [Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion),
    [Modeling Diffusion Process](https://en.wikipedia.org/wiki/Diffusion_process),
    [PageRank Algorithm](https://en.wikipedia.org/wiki/PageRank#Distributed_algorithm_for_PageRank_computation)  
    
    Here we will see how random walk in $1$ Dimension results in a
    [Gaussian distribution](https://read.quantml.org/statistics/gaussian-distribution)
    """)

    p: float = 0.5
    with st.sidebar.beta_container():
        add_bias: bool = st.checkbox("Add bias")
        st_seed_p = st.beta_columns([1, 1] if add_bias else [1])
        st_bounce_sim = st.beta_columns([1, 1])

        seed: Union[int, None] = st_seed_p[0].number_input(
            "Enter Seed (-1 mean seed is disabled)",
            min_value=-1,
            max_value=10000,
            value=0,
            step=1
        )
        if seed == -1: seed = None

        if add_bias:
            p: float = st_seed_p[1].slider(
                "Probability of particle moving to the right (p)",
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                step=0.1
            )

        n_bounces: int = st_bounce_sim[0].slider(
            "Number of bounces (N)",
            min_value=1,
            max_value=100,
            value=50,
            step=1
        )

        n_sim: int = st_bounce_sim[1].slider(
            "Number of simulations",
            min_value=10,
            max_value=500,
            value=200,
            step=10
        )

    if seed is not None: np.random.seed(seed)

    random_walks = np.array([np.cumsum(np.random.choice([+1, -1], 100, p=[p, 1 - p])) for _ in range(500)])

    with st.beta_expander("Scenario", expanded=True):
        st.markdown(f"""
        Say you have a very thin pipe and you place a crazy particle inside that pipe.    
        Say that initial location of particle is $x=0$    
        This particle bounces right at $x+1$(with probability ${'{:.2f}'.format(p)}$) and 
        left at $x-1$(with probability ${'{:.2f}'.format(1 - p)}$).    
        Now we want to study this particle's location after $N({n_bounces})$ number of bounces.    
        Now let's see a random walk of a single particle. Here column indicates number of bounces
        and value(of that column) indicates position after certain number of bounces.
        """)
        st.write(stPandas(random_walks[0], label="Position"))

    with st.beta_expander("Getting Data", expanded=True):
        st.markdown(f"""
        Data we see above is just for a single observation, we need multiple observations of in order to
        study position after ${n_bounces}$ bounces.    
        So let's simulate data for ${n_sim}$ particles where each particle performs ${n_bounces}$
        number of bounces.    
        """)

        index = ["1st Random walk", "2nd Random walk", "3rd Random walk"]
        index.extend([f"{i+4}th Random walk" for i in range(n_sim - 3)])
        df = pd.DataFrame(data=random_walks[:n_sim, :n_bounces], index=index)
        df.columns += 1
        st.write(df)

    with st.beta_expander(f"Getting particle's position after {n_bounces} bounces", expanded=True):
        st.markdown(f"""
        Now we want to study particle's position after ${n_bounces}$ bounces.    
        We have our data of ${n_sim}$ particles with ${n_bounces}$ bounces each.    
        Let's extract particle's position after ${n_bounces}$ bounces, i.e. the last column of our data.   
        """)

        position_data = random_walks[:n_sim, n_bounces - 1]
        npArray: DataFrame = pd.DataFrame(data=position_data)
        index = ["1st Particle", "2nd Particle", "3rd Particle"]
        index.extend([f"{i + 4}th Particle" for i in range(n_sim - 3)])
        npArray.index = index
        npArray.columns = [f"Position after {n_bounces} bounces"]
        st.write(npArray)

    bins, counts = np.unique(random_walks[:n_sim, n_bounces - 1], return_counts=True)
    fig, (counts, bins) = plot_histogram(
        position_data,
        description={
            "title": {
                "main": f"Particle's Position after {n_bounces} bounces",
                "x": f"Position(x) after {n_bounces} bounces",
                "y": f"PMF of Position(x) after {n_bounces} bounces",
                "force": True
            },
            "label": {
                "main": "Position's PMF",
                "x": "Position",
            }
        },
        convert_into_probability_plot=True,
        tilde_equals="=",
        bins=bins,
        counts=counts,
        centralize_bins=False,
        showlegend=False,
        isMobile=False  # NEED TO BE CHANGE
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    Doesn't this histogram of "Particle's PMF of Position after ${n_bounces}$ bounces" looks to be
    Normally distributed.    
    Let's visually inspect it, but how can we visually inspect that
    "Particle's PMF of Position after ${n_bounces}$ bounces" approximates a Normal Distribution or not.
    """)

    with st.beta_expander("Imposing PDF of a Normal Distribution", expanded=True):
        st.markdown(f""" 
        **Question:** Can we impose a PDF of a Normal Distribution over our histogram 
        and see if it fit's the histogram nicely?    
        **Answer:** No we can't, our histogram shows "Particle's PMF of Position after ${n_bounces}$ bounces" 
        and heights of PMF and PDF do not denotes same thing, height of PMF is a probability but 
        height of PDF is not probability.    
        Let's see ourselves, let's impose a Normal Distribution with empirical mean and empirical variance.
        """)

        mean = position_data.mean()
        std = position_data.std()
        iid_rvs = np.linspace(mean - 3 * std, mean + 3 * std, 100)
        line_plot(
            x=iid_rvs, y=norm.pdf(iid_rvs, mean, std),
            description={
              "title": {
                  "main": f"Particle's Position after {n_bounces} bounces/<br>"
                          f"Normal Distribution N(μ={'{:.4f}'.format(mean)}, σ={'{:.4f}'.format(std)})",
                  "x": f"Position(x) after {n_bounces} bounces/<br>"
                       f"Random draw from N(μ={'{:.4f}'.format(mean)}, σ={'{:.4f}'.format(std)})",
                  "y": f"PMF of Position(x) after {n_bounces} bounces/<br>PDF of Normal Distribution"
              },
              "label": {
                  "main": "Normal distribution"
              },
              "hovertemplate": "Random draw(x): %{x}<br>PDF(x=%{x}): %{y}",
              "color": "green"
            },
            fig=fig,
            mode="lines",
            isMobile=False  # NEED TO BE CHANGE
        )
        st.plotly_chart(fig, use_container_width=True)

    with st.beta_expander("Imposing CDF of a Normal Distribution", expanded=True):
        st.markdown(f"""
        **Question:** Can we impose a **CDF** of a Normal Distribution over our histogram
        and see if it fit's the histogram nicely?    
        **Answer:** Yes we can, CDF of our histogram and CDF of Normal Distribution denotes same thing.    
        Let's see ourselves, let's impose CDF of a Normal Distribution with empirical mean and empirical variance
        on CDF of Particle's PMF of Position after ${n_bounces}$ bounces.
        """)

        fig = line_plot(
            x=iid_rvs, y=norm.cdf(iid_rvs, mean, std),
            description={
                "label": {
                    "main": "Normal distribution CDF"
                },
                "hovertemplate": "Random draw(x): %{x}<br>CDF(x=%{x}): %{y}",
                "color": "green"
            },
            mode="lines",
            isMobile=False  # NEED TO BE CHANGE
        )

        fig = line_plot(
            x=bins, y=np.cumsum(counts) / np.sum(counts),
            description={
                "title": {
                    "main": f"CDF:<br>Particle's Position after {n_bounces} bounces/<br>"
                            f"Normal Distribution N(μ={'{:.4f}'.format(mean)}, σ={'{:.4f}'.format(std)})",
                    "x": f"Position(x) after {n_bounces} bounces/<br>"
                         f"Random draw from N(μ={'{:.4f}'.format(mean)}, σ={'{:.4f}'.format(std)})",
                    "y": f"<b>CDF</b> of Position(x) after {n_bounces} bounces/"
                         f"<br><b>CDF</b> of Normal Distribution"
                },
                "label": {
                    "main": "Position's CDF"
                },
                "hovertemplate": "Position(x) = %{x}<br>CDF(x = %{x}): %{y}",
                "color": "royalblue"
            },
            fig=fig,
            mode="markers",
            isMobile=False  # NEED TO BE CHANGE
        )

        st.plotly_chart(fig, use_container_width=True)

    with st.beta_expander("But why Normal Distribution?", expanded=True):
        st.markdown(f"""
        Ok we get it that Particle's PMF of Position after ${n_bounces}$ bounces approximates to a 
        Normal Distribution (as number of bounces increases), but why Normal Distribution?  
        Why it make sense for PMF of Position to be Normally distributed?   
        
        And the answer is
        [Central Limit Theorem](https://www.quantml.org/statistics/central-limit-theorem/).      
        To get the particle's position after ${n_bounces}$ bounces, we add ${n_bounces}$ steps taken by particle
        $(\\pm 1)$, and each step is completely random (also independent of any other step).   
        So here we are adding ${n_bounces}$ i.i.d. random variables, and
        [CLT](https://www.quantml.org/statistics/central-limit-theorem/)
        says that as number of bounces increases, PMF of that particle's position after certain number of bounces
        converges to a Normal Distribution.
        """)
