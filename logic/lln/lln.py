from typing import Dict, Union, Iterable, Tuple
import scipy.stats
from plotly.graph_objs import Figure

from logic.lln.simulation import get_pdf, simulation
from distribution import distributions_properties, get_distribution, graph_label
import numpy as np


def run(dist, var: Dict[str, Union[int, float]], n: Dict[str, int], state) -> Tuple[float, Union[np.ndarray, int, float, complex], np.ndarray, Figure, Figure]:
    # print("          - run(dist=" + dist + ", var=" + str(var) + ", n=" + str(n))
    iscontinuous:   bool = distributions_properties[dist]["iscontinuous"]
    n_population:   int  = n["population"]
    n_samples:      int  = n["samples"]
    var = [var[k] for k in var.keys()]
    distribution: Union[scipy.stats.rv_continuous, scipy.stats.rv_discrete] = get_distribution(dist, var)
    population: Union[np.ndarray, int, float, complex] = distribution.rvs(size=n_population)
    iid_rvs: np.ndarray = population[:n_samples]
    pdf_rvs: Union[np.ndarray, Iterable, int, float] = distribution.pdf(iid_rvs) if iscontinuous else distribution.pmf(iid_rvs)
    name: str = graph_label(dist, var)
    mean: float = distribution.mean()
    if state.stSettings["seed"] is not None: np.random.seed(state.stSettings["seed"])
    pdf_plot: Figure = get_pdf(iid_rvs, pdf_rvs, name, iscontinuous)
    if state.stSettings["seed"] is not None: np.random.seed(state.stSettings["seed"])
    simulation_plot: Figure = simulation(iid_rvs, mean, n_samples, name, state)
    return mean, population, iid_rvs, pdf_plot, simulation_plot
