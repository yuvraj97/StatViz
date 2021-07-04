from typing import Union, Tuple
import numpy as np
import plotly.express as px
from plotly.graph_objs import Figure

def get_plot(data: np.ndarray, title: str) -> Figure:
    counts: np.ndarray
    bins: np.ndarray
    counts, bins = np.histogram(np.array(data * 100, dtype=int), bins=range(0, 101, 2))
    bins = 0.5 * (bins[:-1] + bins[1:]) / 100
    fig: Figure = px.bar(x=bins, y=counts, labels={'x': 'p', 'y': '# occurrence'})
    fig.update_layout(title=title,
                      xaxis_title='Proportion of red balls (p)',
                      yaxis_title='# occurrence of certain (p) in our simulation')
    return fig

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

    if seed is not None: np.random.seed(seed)
    population_sample: np.ndarray = get_sample_with_true_p(n_population, true_p)
    estimators: np.ndarray = np.empty(n_simulations)
    samples: list = []
    for i in range(0, n_simulations):
        # Here we randomly select "n_sample" couples out of "population_sample"
        sample = np.random.choice(population_sample, n_sample)
        estimators[i] = sample.sum() / n_sample
        samples.append(sample)
    return population_sample, samples, get_plot(estimators, title), estimators.sum() / n_simulations, estimators
