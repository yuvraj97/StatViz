from typing import Union

import streamlit as st
import numpy as np
import pandas as pd
from Chapters.utilities.lite_utils import stPandas
from Chapters.utilities.plots import animate_dot_2D, plot_histogram3D, surface_plot3D
from scipy.stats import multivariate_normal


def get_st_probability(max_bounces, max_sim):
    p_up: float = 0.25
    p_right: float = 0.25
    p_left: float = 0.25
    p_down: float = 0.25

    seed: Union[int, None] = st.sidebar.number_input(
        "Enter Seed (-1 mean seed is disabled)",
        min_value=-1,
        max_value=10000,
        value=0,
        step=1
    )
    if seed == -1: seed = None

    with st.sidebar.container():
        add_bias: bool = st.checkbox("Add bias")
        if add_bias:
            st_u, st_r, st_l = st.columns([1, 1, 1])
            p_up_max = 1.0
            if p_up_max <= 0: return None
            p_up: float = st_u.slider(
                "P(moving up)",
                min_value=0.0,
                max_value=1.0,
                value=0.25,
                step=0.1
            )
            p_right_max = p_up_max - p_up
            if p_right_max <= 0: return None
            p_right: float = st_r.slider(
                "P(moving right)",
                min_value=0.0,
                max_value=p_right_max,
                value=0.25 if 0.25 < p_right_max else p_right_max / 2,
                step=0.1
            )
            p_left_max = p_up_max - p_up - p_right
            if p_left_max <= 0: return None
            p_left: float = st_l.slider(
                "P(moving left)",
                min_value=0.0,
                max_value=p_left_max,
                value=0.25 if 0.25 < 1.0 - p_up - p_right else (1.0 - p_up - p_right) / 2,
                step=0.1
            )
            p_down: float = 1 - p_up - p_right - p_left
            if p_down <= 0: return None

        st_bounces, st_sim = st.columns([1, 1])
        n_bounces: int = st_bounces.slider(
            "Number of bounces (N)",
            min_value=1,
            max_value=max_bounces,
            value=50,
            step=1
        )

        n_sim: int = st_sim.slider(
            "Number of simulations",
            min_value=10,
            max_value=max_sim,
            value=200,
            step=10)

    return (p_up, p_down, p_right, p_left), (n_bounces, n_sim), seed


def run():

    st.markdown("""
        Now let's see how Random walk in $2$ Dimension results in a
        [Multivariate Gaussian distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
        """)

    max_bounces, max_sim = 100, 200

    try:
        (p_up, p_down, p_right, p_left), (n_bounces, n_sim), seed = get_st_probability(max_bounces, max_sim)
    except Exception:
        st.sidebar.error("Probability selection is not valid!\nProbabilities should sum to $1$")
        return

    if seed is not None: np.random.seed(seed)

    x = np.zeros(shape=(max_sim, max_bounces), dtype=np.int8)

    y = np.zeros(shape=(max_sim, max_bounces), dtype=np.int8)

    directions = np.array([
        np.random.choice(["+y", "-y", "+x", "-x"], max_bounces, p=[p_up, p_down, p_right, p_left])
        for _ in range(max_sim)
    ])
    for sim in range(max_sim):
        if directions[sim][0] == "+y":
            x[sim][0], y[sim][0] = 0, 1
        elif directions[sim][0] == "-y":
            x[sim][0], y[sim][0] = 0, -1
        elif directions[sim][0] == "+x":
            x[sim][0], y[sim][0] = 1, 0
        else:
            x[sim][0], y[sim][0] = -1, 0
        for bounce in range(1, max_bounces):
            if directions[sim][bounce] == "+y":
                x[sim][bounce], y[sim][bounce] = x[sim][bounce - 1], y[sim][bounce - 1] + 1
            elif directions[sim][bounce] == "-y":
                x[sim][bounce], y[sim][bounce] = x[sim][bounce - 1], y[sim][bounce - 1] - 1
            elif directions[sim][bounce] == "+x":
                x[sim][bounce], y[sim][bounce] = x[sim][bounce - 1] + 1, y[sim][bounce - 1]
            else:
                x[sim][bounce], y[sim][bounce] = x[sim][bounce - 1] - 1, y[sim][bounce - 1]

    with st.expander("Scenario", expanded=True):
        st.markdown(f"""
        Let's assume that there is a crazy particle wandering on a $2$-Dimensional surface.    
        Say that initial location of particle is origin $(x=0, y=0)$    
        (Say that it's current location is $(x,y)$)This particle bounces,
        
        - Up (at $y+1$) with probability ${'{:.2f}'.format(p_up)}$
        - Right (at $x+1$) with probability ${'{:.2f}'.format(p_right)}$
        - Left (at $x-1$) with probability ${'{:.2f}'.format(p_left)}$
        - Down (at $y-1$) with probability ${'{:.2f}'.format(p_down)}$

        Now we want to study this particle's location after $N({n_bounces})$ number of bounces.    
        Now let's see a random walk of a single particle. Here column indicates number of bounces
        and value(of that column) indicates x-axis and y-axis position respectively after certain number of bounces.
        """)

        st.write(stPandas(np.array([
            f"({x[0][bounce]}, {y[0][bounce]})" for bounce in range(n_bounces)
        ]), "Position (x, y)"))

        if st.checkbox("See the particle in action", False):
            st.plotly_chart(animate_dot_2D(x=x[0][:n_bounces],
                                           y=y[0][:n_bounces],
                                           title="Single Particle Random walk",
                                           button_label="Start"))

    with st.expander("Getting Data", expanded=True):
        st.markdown(f"""
        Data we see above is a random walk of a single particle, it's just a single observation,
        we need multiple observations of in order to study position after ${n_bounces}$ bounces.    
        So let's simulate data for ${n_sim}$ particles where each particle performs ${n_bounces}$
        number of bounces.    
        """)

        st_table = np.array([[
            f"({x[sim][bounce]}, {y[sim][bounce]})" for bounce in range(n_bounces)
        ] for sim in range(n_sim)
        ])
        index = ["1st Particle", "2nd Particle", "3rd Particle"]
        index.extend([f"{i + 1}th Particle" for i in range(3, n_sim)])
        df = pd.DataFrame(data=st_table, index=index)
        df.columns += 1
        st.write(df)

    with st.expander(f"Getting particle's position after {n_bounces} bounces", expanded=True):
        st.markdown(f"""
        Now we want to study particle's position after ${n_bounces}$ bounces.    
        We have our data of ${n_sim}$ particles with ${n_bounces}$ bounces each.    
        Let's extract particle's position after ${n_bounces}$ bounces, i.e. the last column of our data.   
        """)

        df: pd.DataFrame = pd.DataFrame(data=st_table[:n_sim, n_bounces - 1])
        index = ["1st Particle", "2nd Particle", "3rd Particle"]
        index.extend([f"{i + 4}th Particle" for i in range(n_sim - 3)])
        df.index = index
        df.columns = [f"Position after {n_bounces} bounces"]
        st.write(df)

        X = x[:n_sim, n_bounces - 1],
        Y = y[:n_sim, n_bounces - 1],
        X, Y = X[0], Y[0]
        fig = plot_histogram3D(
            X,
            Y,
            description={
                "title": {
                    "main": f"Particle's Position after {n_bounces} bounces",
                    "x": f"Position(x) after {n_bounces} bounces",
                    "y": f"Position(y) after {n_bounces} bounces",
                    "z": f"PMF of Position(x, y) after {n_bounces} bounces",
                },
                "label": {
                    "main": "Position's PMF",
                    "x": "Position(x)",
                    "y": "Position(y)",
                    "z": "Position's PMF"
                }
            },
            bins=(25, 25),
            convert_into_probability_plot=True,
            fig=None,
            showlegend=False,
            tilda=" ~ ",
            isMobile=False  # NEED TO BE CHANGE
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    Isn't this shape looks to follow the bell curve.        
    Let's visually inspect it, but how can we visually inspect that
    "Particle's PMF of Position after ${n_bounces}$ bounces" approximates
    Multivariate Normal Distribution or not.
    """)

    with st.expander("Imposing PDF of a Normal Distribution", expanded=True):
        st.markdown(f""" 
        As we saw in 
        [Random walk 1D](https://app.quantml.org/statistics/?ch=Gaussian-Distribution&topic=Random+walk+2D")
        that imposing PDF of a Normal distribution over our histogram don't help us answering (visually) that
        do our "Particle's PMF of Position after ${n_bounces}$ bounces" approximates Multivariate Normal Distribution.  
        Let's see it ourselves, let's impose a Multivariate Normal Distribution with
        """, unsafe_allow_html=True)
        mean = [X.mean(), Y.mean()]
        st.latex("\\text{sample mean} = " + f"[\\mu_x = {mean[0]} , \\mu_y = {mean[1]}]")
        cov = np.cov(X, Y)
        st.latex(f"""
        \\text{{sample covariance matrix}} = \\begin{{bmatrix}} 
        {'{:.2f}'.format(cov[0, 0])} & {'{:.2f}'.format(cov[0, 1])} \\\\ 
        {'{:.2f}'.format(cov[1, 0])} & {'{:.2f}'.format(cov[1, 1])} \\\\ 
        \\end{{bmatrix}}""")

        count = 20
        _X = np.outer(np.linspace(-5 * X.std() * X.mean(), 5 * X.std() * X.mean(), count), np.ones(count))
        _Y = _X.copy().T
        _X_v, _Y_v = _X.reshape(1, count * count)[0], _Y.reshape(1, count * count)[0]
        pdf = multivariate_normal.pdf(
            np.vstack((_X_v, _Y_v)).T, mean=mean, cov=cov
        ).reshape(count, count)

        fig = surface_plot3D(
            x=_X, y=_Y, z=pdf,
            description={
                "title": {
                    "main": f"Particle's Position after {n_bounces} bounces/<br>Bivariate Normal Distribution",
                    "x": f"Position(x) after {n_bounces} bounces/<br>"
                         f"Random draw from Bivariate Normal Distribution",
                    "y": f"Position(y) after {n_bounces} bounces/<br>"
                         f"Random draw from Bivariate Normal Distribution",
                    "z": f"PMF of Position(x, y) after {n_bounces} bounces/<br>"
                         f"PDF of Bivariate Normal Distribution"
                },
                "label": {
                    "main": "Bivariate Normal distribution"
                },
                "hovertemplate": "Random draw(x, y): (%{x}, %{y})<br>PDF((x, y)=(%{x}, %{y})): %{z}",
            },
            fig=fig,
            isMobile=False  # NEED TO BE CHANGE
        )

        st.plotly_chart(fig, use_container_width=True)

    with st.expander("Imposing CDF of a Bivariate Normal Distribution", expanded=True):
        st.markdown(f"""
        As we saw in [Random walk 1D](https://app.quantml.org/statistics/?ch=Gaussian-Distribution&topic=Random+walk+2D)
        comparing CDFs is a good idea to see if one distribution coverges to another distribition.    
        So let's see it ourselves, let's impose CDF of a Bivariate Normal Distribution with sample mean and 
        sample covariance matrix, on CDF of Particle's PMF of Position after ${n_bounces}$ bounces.    
        Here,    
        <span class="l2">Blue curve is for CDF of Position after ${n_bounces}$ bounces</span>    
        <span class="l1">Red curve is for CDF of Bivariate distribution</span>    
        
        """, unsafe_allow_html=True)

        _X_h = np.outer(X, np.ones(len(X)))
        _Y_h = np.outer(Y, np.ones(len(Y))).T
        _Z_h = np.zeros(shape=_X_h.shape)
        for i in range(_Z_h.shape[0]):
            _Z_h[i] = [np.sum((X < _X_h[i][j]) & (Y < _Y_h[i][j])) for j in range(_Z_h.shape[1])]
        _Z_h = _Z_h / np.max(_Z_h)

        fig = surface_plot3D(
            x=_X_h, y=_Y_h, z=_Z_h,
            description={
                "title": {
                    "main": f"CDF:<br>Particle's Position after {n_bounces} bounces/<br>"""
                            f"Bivariate Normal Distribution",
                    "x": f"Position(x)",
                    "y": f"Position(y)",
                    "z": f"<b>CDF</b>"
                },
                "label": {
                    "main": "Position's CDF"
                },
                "hovertemplate": "Position(x, y) = (%{x}, %{y})<br>CDF((x, y)=(%{x}, %{y})): %{z}",
            },
            colorscale='Blues',
            opacity=0.01,
            isMobile=False  # NEED TO BE CHANGE
        )

        fig = surface_plot3D(
            x=_X, y=_Y,
            z=multivariate_normal.cdf(np.vstack((_X_v, _Y_v)).T, mean=mean, cov=cov).reshape(count, count),
            description={
                "label": {
                    "main": "Bivariate distribution CDF"
                },
                "hovertemplate": "Random draw(x, y): (%{x}, %{y})<br>CDF((x, y)=(%{x}, %{y})): %{z}",
            },
            fig=fig,
            colorscale='Burg',
            opacity=1.0,
            isMobile=False  # NEED TO BE CHANGE
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    Now we can say that Particle's Position after {n_bounces} bounces do follows a Bivariate Normal Distribution
    with sample mean and sample covariance matrix.""")
