from typing import Dict, Union
from utils.distribution import distributions_properties
import numpy as np
import pandas as pd


def stPandas(npArray: np.ndarray, label: str = "Random Draws") -> pd.DataFrame:
    npArray = npArray.reshape((1, len(npArray)))
    npArray = pd.DataFrame(data=npArray, index=[label])
    npArray.columns += 1
    return npArray
