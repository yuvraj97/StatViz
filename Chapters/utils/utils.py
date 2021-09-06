import scipy
import numpy as np
import pandas as pd
from typing import List, Union
from scipy.stats import bernoulli, geom, binom, poisson
from scipy.stats import beta, expon, uniform, cauchy, norm, chi2


def stPandas(npArray: np.ndarray, label: str = "Random Draws") -> pd.DataFrame:
    npArray = npArray.reshape((1, len(npArray)))
    npArray = pd.DataFrame(data=npArray, index=[label])
    npArray.columns += 1
    return npArray


def get_distribution(
        dist: str,
        var: List[Union[int, float]]
) -> Union[scipy.stats.rv_continuous, scipy.stats.rv_discrete]:
    if dist == "norm":
        return norm(*var)
    elif dist == "uniform":
        return uniform(*var)
    elif dist == "bernoulli":
        return bernoulli(*var)
    elif dist == "geom":
        return geom(*var)
    elif dist == "binom":
        return binom(*var)
    elif dist == "poisson":
        return poisson(*var)
    elif dist == "beta":
        return beta(*var)
    elif dist == "expon":
        return expon(1 / var[0])
