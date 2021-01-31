import streamlit as st
import numpy as np
import pandas as pd
from gui.utils import stPandas
from logic.utils import animate_dot_2D, plot_histogram3D, surface_plot3D
from scipy.stats import multivariate_normal

def get_st_probability(max_bounces, max_sim):
    p_up: float = 0.25
    p_right: float = 0.25
    p_left: float = 0.25
    p_down: float = 0.25
    with st.sidebar.beta_container():
        st.markdown("", unsafe_allow_html=True)
        add_bias: bool = st.checkbox("Add bias")
        if add_bias:
            p_up_max = 1.0
            if p_up_max <= 0: return None
            p_up: float = st.slider("Probability of particle moving up (in +y direction)",
                                    min_value=0.0,
                                    max_value=1.0,
                                    value=0.25,
                                    step=0.1)
            p_right_max = p_up_max - p_up
            if p_right_max <= 0: return None
            p_right: float = st.slider("Probability of particle moving right (in +x direction)",
                                       min_value=0.0,
                                       max_value=p_right_max,
                                       value=0.25 if 0.25 < p_right_max else p_right_max/2,
                                       step=0.1)
            p_left_max = p_up_max - p_up - p_right
            if p_left_max <= 0: return None
            p_left: float = st.slider("Probability of particle moving left (in -x direction)",
                                      min_value=0.0,
                                      max_value=p_left_max,
                                      value=0.25 if 0.25 < 1.0 - p_up - p_right else (1.0 - p_up - p_right)/2,
                                      step=0.1)
            p_down: float = 1 - p_up - p_right - p_left
            if p_down <= 0: return None

            # st.markdown(f"Probability of particle moving down (in -y direction): {p_down}")
        n_bounces: int = st.sidebar.slider("Number of bounces (N)",
                                           min_value=1,
                                           max_value=max_bounces,
                                           value=50,
                                           step=1)

        n_sim: int = st.sidebar.number_input("Number of simulations",
                                             min_value=10,
                                             max_value=max_sim,
                                             value=200,
                                             step=10, )

    return (p_up, p_down, p_right, p_left), (n_bounces, n_sim)

def run(state):
    st.markdown("""
        Now let's see how Random walk in $2$ Dimension results in a
        <a rel='noreferrer' target='_blank' href="https://en.wikipedia.org/wiki/Multivariate_normal_distribution">Multivariate Gaussian distribution</a>.<br>
        """, unsafe_allow_html=True)

    max_bounces, max_sim = 100, 500
    prev_p_up = None if "p_up" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_up"]
    prev_p_right = None if "p_right" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_right"]
    prev_p_left = None if "p_left" not in state.gauss["Random walk 1D"] else state.gauss["Random walk 1D"]["p_left"]

    try:
        (p_up, p_down, p_right, p_left), (n_bounces, n_sim) = get_st_probability(max_bounces, max_sim)
    except:
        st.sidebar.markdown("""
        <blockquote class="error">
            Probability selection is not valid!
        </blockquote>
        """, unsafe_allow_html=True)
        return

    state.gauss["Random walk 1D"]["p_up"] = p_up
    state.gauss["Random walk 1D"]["p_right"] = p_right
    state.gauss["Random walk 1D"]["p_left"] = p_left

    if state.stSettings["seed"] is not None: np.random.seed(state.stSettings["seed"])
    else: np.random.seed()

    directions = state.gauss["Random walk 1D"]["random_walks_direction"] = state.gauss["Random walk 1D"]["random_walks_direction"] if \
        "random_walks_direction" in state.gauss["Random walk 1D"] and \
        prev_p_up == p_up and \
        prev_p_right == p_right and \
        prev_p_left == p_left and \
        state.stSettings["seed"] is not None and \
        state.seed_changed is False else \
        np.array([np.random.choice(["+y", "-y", "+x", "-x"], max_bounces, p=[p_up, p_down, p_right, p_left]) for _ in range(max_sim)])

    x: np.ndarray = np.zeros(shape=(max_sim, max_bounces), dtype=np.int8)
    y: np.ndarray = np.zeros(shape=(max_sim, max_bounces), dtype=np.int8)
    for sim in range(max_sim):
        if directions[sim][0] == "+y"  : x[sim][0], y[sim][0] = 0, 1
        elif directions[sim][0] == "-y": x[sim][0], y[sim][0] = 0, -1
        elif directions[sim][0] == "+x": x[sim][0], y[sim][0] = 1, 0
        else: x[sim][0], y[sim][0] = -1, 0
        for bounce in range(1, max_bounces):
            if directions[sim][bounce]   == "+y": x[sim][bounce], y[sim][bounce] = x[sim][bounce-1], y[sim][bounce-1] + 1
            elif directions[sim][bounce] == "-y": x[sim][bounce], y[sim][bounce] = x[sim][bounce-1], y[sim][bounce-1] - 1
            elif directions[sim][bounce] == "+x": x[sim][bounce], y[sim][bounce] = x[sim][bounce-1] + 1, y[sim][bounce-1]
            else: x[sim][bounce], y[sim][bounce] = x[sim][bounce-1] - 1, y[sim][bounce-1]

    with st.beta_expander("Scenario", expanded=True):
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

        # npArray.columns += 1
        st.write(stPandas(np.array([f"({x[0][bounce]}, {y[0][bounce]})" for bounce in range(n_bounces)]), "Position (x, y)"))
        st.plotly_chart(animate_dot_2D(x=x[0][:n_bounces],
                                       y=y[0][:n_bounces],
                                       title="Single Particle Random walk",
                                       button_label="Start"))

    with st.beta_expander("Getting Data", expanded=True):
        st.markdown(f"""
        Data we see above is a random walk of a single particle, it's just a single observation,
        we need multiple observations of in order to study position after ${n_bounces}$ bounces.    
        So let's simulate data for ${n_sim}$ particles where each particle performs ${n_bounces}$
        number of bounces.    
        """)

        st_table = np.array([[f"({x[sim][bounce]}, {y[sim][bounce]})" for bounce in range(n_bounces)] for sim in range(n_sim)])
        index = ["1st Particle", "2nd Particle", "3rd Particle"]
        index.extend([f"{i + 1}th Particle" for i in range(3, n_sim)])
        df = pd.DataFrame(data=st_table, index=index)
        df.columns += 1
        st.write(df)

    with st.beta_expander(f"Getting particle's position after {n_bounces} bounces", expanded=True):
        st.markdown(f"""
        Now we want to study particle's position after ${n_bounces}$ bounces.    
        We have our data of ${n_sim}$ particles with ${n_bounces}$ bounces each.    
        Let's extract particle's position after ${n_bounces}$ bounces, i.e. the last column of our data.   
        """)

        st_position_data = st_table[:n_sim, n_bounces - 1]
        df: pd.DataFrame = pd.DataFrame(data=st_position_data)
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
            isMobile=state.isMobile,
            showlegend=False,
            tilda=" ~ ")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    Isn't this shape looks to follow the bell curve.        
    Let's visually inspect it, but how can we visually inspect that
    "Particle's PMF of Position after ${n_bounces}$ bounces" approximates
    Multivariate Normal Distribution or not.
    """)

    with st.beta_expander("Imposing PDF of a Normal Distribution", expanded=True):
        st.markdown(f""" 
        As we saw in <a rel='noreferrer' target='_blank' href="https://app.quantml.org/statistics/?ch=Gaussian-Distribution&topic=Random+walk+2D">Random walk 1D</a>
        that imposing PDF of a Normal distribution over our histogram don't help us answering (visually) that
        do our "Particle's PMF of Position after ${n_bounces}$ bounces" approximates Multivariate Normal Distribution.<br>
        Let's see it ourselves, let's impose a Multivariate Normal Distribution with
        """, unsafe_allow_html=True)
        mean = [X.mean(), Y.mean()]
        st.latex("\\text{sample mean} = "+f"[\\mu_x = {mean[0]} , \\mu_y = {mean[1]}]")
        cov = np.cov(X, Y)
        st.latex("\\text{sample covariance matrix} = \\begin{bmatrix} "+f"{'{:.2f}'.format(cov[0,0])} & {'{:.2f}'.format(cov[0,1])} \\\\ {'{:.2f}'.format(cov[1,0])} & {'{:.2f}'.format(cov[1,1])} "+" \\\\ \end{bmatrix}")

        count = 20
        _X = np.outer(np.linspace(-5 * X.std() * X.mean(), 5 * X.std() * X.mean(), count), np.ones(count))
        _Y = _X.copy().T
        _X_v, _Y_v = _X.reshape(1, count * count)[0], _Y.reshape(1, count * count)[0]
        pdf = multivariate_normal.pdf(np.vstack((_X_v, _Y_v)).T, mean=mean, cov=cov).reshape(count,count)
        fig = surface_plot3D(x=_X, y=_Y, z=pdf,
                             description={
                                 "title": {
                                     "main": f"Particle's Position after {n_bounces} bounces/<br>Bivariate Normal Distribution",
                                     "x": f"Position(x) after {n_bounces} bounces/<br>Random draw from Bivariate Normal Distribution",
                                     "y": f"Position(y) after {n_bounces} bounces/<br>Random draw from Bivariate Normal Distribution",
                                     "z": f"PMF of Position(x, y) after {n_bounces} bounces/<br>PDF of Bivariate Normal Distribution"
                                 },
                                 "label": {
                                     "main": "Bivariate Normal distribution"
                                 },
                                 "hovertemplate": "Random draw(x, y): (%{x}, %{y})<br>PDF((x, y)=(%{x}, %{y})): %{z}",
                             },
                             fig=fig,
                             isMobile=state.isMobile)
        st.plotly_chart(fig, use_container_width=True)

    with st.beta_expander("Imposing CDF of a Bivariate Normal Distribution", expanded=True):
        st.markdown(f"""
        As we saw in <a rel='noreferrer' target='_blank' href="https://app.quantml.org/statistics/?ch=Gaussian-Distribution&topic=Random+walk+2D">Random walk 1D</a>
        comparing CDFs is a good idea to see if one distribution coverges to another distribition.    
        So let's see it ourselves, let's impose CDF of a Bivariate Normal Distribution with sample mean and sample covariance matrix,  
        on CDF of Particle's PMF of Position after ${n_bounces}$ bounces.    
        Here,    
        <span class="l2">Blue curve is for CDF of Position after ${n_bounces}$ bounces</span>    
        <span class="l1">Red curve is for CDF of Bivariate distribution</span>    
        
        """, unsafe_allow_html=True)

        _X_h = np.outer(X, np.ones(len(X)))
        _Y_h = np.outer(Y, np.ones(len(Y))).T
        _Z_h = np.zeros(shape=_X_h.shape)
        for i in range(_Z_h.shape[0]):
            _Z_h[i] = [((X < _X_h[i][j]) & (Y < _Y_h[i][j])).sum() for j in range(_Z_h.shape[1])]
        _Z_h = _Z_h/_Z_h.max()

        fig = surface_plot3D(x=_X_h, y=_Y_h,
                             z=_Z_h,
                             description={
                                 "title": {
                                     "main": f"CDF:<br>Particle's Position after {n_bounces} bounces/<br>Bivariate Normal Distribution",
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
                             isMobile=state.isMobile)

        fig = surface_plot3D(x=_X,
                             y=_Y,
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
                             isMobile=state.isMobile)

        st.plotly_chart(fig, use_container_width=True)
