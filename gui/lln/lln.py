from typing import Union, Dict
import numpy as np
from plotly.graph_objs import Figure

import logic.lln.lln as lln
from distribution import distributions_properties, which_distribution, stDistribution
from gui.lln.display import stDisplay
from utils import set_get_URL


def main(distribution: str, state):
    dist: str = which_distribution[distribution]

    set_get_URL(parameters={
        "dist" : distributions_properties[dist]["name"],
        "topic": "remove"
    })

    var: Dict[str, Union[int, float]]
    n: Dict[str, int]
    var, n = stDistribution(dist)

    if state.stSettings["seed-checkbox"].checkbox("Enable Seed", True):
        state.stSettings["seed"]: int = state.stSettings["seed-number"].number_input("Enter Seed",
                                                                                     min_value=0,
                                                                                     max_value=10000,
                                                                                     value=0,
                                                                                     step=1)

    mean: float
    population: np.ndarray
    sample: np.ndarray
    pdf: Figure
    simulation: Figure
    mean, population, sample, pdf, simulation = lln.run(dist, var, n, state)

    stDisplay(dist, population, sample, var, n, mean, (pdf, simulation), state)
