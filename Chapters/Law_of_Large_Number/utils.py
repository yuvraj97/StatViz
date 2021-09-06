from typing import Dict, Union
import scipy.stats
import numpy as np
import plotly.graph_objects as go
from plotly.graph_objs import Figure

from Chapters.utils.plots import get_pdf
from utils.distribution import distributions_properties, graph_label
from Chapters.utils.utils import get_distribution


def simulation(iid_rvs: np.ndarray, mean: float, n_samples: int, name: str) -> Figure:
    ns = np.linspace(1, n_samples, n_samples, dtype=int)

    # sample mean for each n
    average = [0] * n_samples
    x = [0] * (3 * n_samples - 1)
    y = [0] * (3 * n_samples - 1)
    n, counter, _sum = 0, 0, 0
    while n < 3 * n_samples - 1:
        if (n + 1) % 3 == 0:
            x[n], y[n] = None, None
        else:
            _sum += iid_rvs[counter]
            # noinspection PyTypeChecker
            average[counter] = _sum / (counter + 1)
            x[n], y[n] = ns[counter], iid_rvs[counter]
            x[n + 1], y[n + 1] = ns[counter], mean
            counter += 1
            n += 1
        n += 1

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y,
                             mode='lines',
                             showlegend=False,
                             line=dict(color='rgb(189,189,189)', width=1), ))

    fig.add_trace(go.Scatter(x=ns, y=average,
                             mode='lines',
                             name='Sample Average',
                             hovertemplate='In this Simulation<br>'
                                           'For <b style="color:pink">Sample Size</b>=%{x}<br>Sample Average=%{y}',
                             line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=ns, y=iid_rvs,
                             mode='markers',
                             name='Random variable(x)',
                             hovertemplate='Random Draw(x): %{y}',
                             line=dict(color='purple')))
    fig.add_trace(go.Scatter(x=ns, y=[mean] * n_samples,
                             mode='lines',
                             name='mean',
                             hovertemplate='True mean: %{y}',
                             line=dict(
                                 color="green",
                                 width=4,
                                 dash="dot")
                             )
                  )

    # Edit the layout
    fig.update_layout(title=name,
                      xaxis_title='Sample Size',
                      yaxis_title='<b>iid</b> Random Variable')
    # fig.update_layout(showlegend=False if state.isMobile else True)
    # NEED TO BE CHANGE
    fig.update_layout(showlegend=True)
    return fig


def run(dist: str,
        var: Dict[str, Union[int, float]],
        n: Dict[str, int],
        state, seed=None) -> Dict[str, Union[float, np.ndarray, Figure]]:
    iscontinuous: bool = distributions_properties[dist]["iscontinuous"]
    n_population: int = n["population"]
    n_samples: int = n["samples"]
    var = [var[k] for k in var.keys()]
    distribution: Union[scipy.stats.rv_continuous, scipy.stats.rv_discrete] = get_distribution(dist, var)
    population: np.ndarray = distribution.rvs(size=n_population)
    iid_rvs: np.ndarray = population[:n_samples]
    pdf_rvs: np.ndarray = distribution.pdf(iid_rvs) if iscontinuous else distribution.pmf(iid_rvs)
    name: str = graph_label(dist, var)
    mean: float = distribution.mean()
    if seed is not None: np.random.seed(seed)
    pdf_plot: Figure = get_pdf(iid_rvs, pdf_rvs, name, iscontinuous)
    if seed is not None: np.random.seed(seed)
    simulation_plot: Figure = simulation(iid_rvs, mean, n_samples, name)
    return {
        "mean": mean,
        "population": population,
        "iid_rvs": iid_rvs,
        "pdf_plot": pdf_plot,
        "simulation_plot": simulation_plot
    }
