from typing import Dict, Union
from distribution import distributions_properties
import numpy as np
import pandas as pd


def get_parameters(dist: str, _vars: Dict[str, Union[int, float]]) -> str:
    """

    :param dist: distribution
    :param _vars: distribution's parameter's values
    :return: markdown formatted string to display parameters
    """
    parameters: str = ""
    i = 0
    for parameter in distributions_properties[dist]["stSlider"]:
        parameters += f"""- {distributions_properties[dist]["parameters"][i]} : ${_vars[parameter]}$\n"""
        i += 1
    return parameters


def stPandas(npArray: np.ndarray, label: str = "Random Draws") -> pd.DataFrame:
    npArray = npArray.reshape((1, len(npArray)))
    npArray = pd.DataFrame(data=npArray, index=[label])
    npArray.columns += 1
    return npArray
