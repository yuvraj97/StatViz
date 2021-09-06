from typing import Union, Tuple
import numpy as np
from plotly.graph_objs import Figure
from Chapters.utilities.plots import plot_histogram


def get_sample_with_true_p(population: int, p: float) -> np.ndarray:
    a: np.ndarray = np.zeros(population, dtype=np.int8)
    _1_s: int = int(population * p)
    for i in range(0, _1_s):
        a[i] = 1
    np.random.shuffle(a)
    return a


def run(n_population: int,
        n_sample: int,
        true_p: float,
        n_simulations: int,
        title: str,
        seed: Union[int, None]) -> Tuple[np.ndarray, list, Figure, float, np.ndarray]:
    if seed == -1: seed = None
    if seed is not None: np.random.seed(seed)
    population_sample: np.ndarray = get_sample_with_true_p(n_population, true_p)
    estimators: np.ndarray = np.empty(n_simulations)
    samples: list = []
    for i in range(0, n_simulations):
        # Here we randomly select "n_sample" couples out of "population_sample"
        sample = np.random.choice(population_sample, n_sample)
        estimators[i] = sample.sum() / n_sample
        samples.append(sample)

    fig, (counts, bins) = plot_histogram(
        estimators,
        description={
            "title": {
                "main": title,
                "x": "1Proportion of red balls (p)",
                "y": "# occurrence of certain (p) in our simulation"
            },
            "label": {
                "main": None,
                "x": "p",
                "y": "# occurrence of p"
            }
        },
        num_bins=len(np.unique(estimators))
    )
    return population_sample, samples, fig, estimators.sum() / n_simulations, estimators
