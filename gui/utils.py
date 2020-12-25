from typing import Dict, Union
from distribution import distributions_properties

def get_parameters(dist: str, _vars: Dict[str, Union[int, float]]) -> str:
    """

    :param dist: distribution
    :param _vars: distribution's parameter's values
    :return: markdown formatted string to display parameters
    """
    parameters: str = ""
    i = 0
    for parameter in distributions_properties[dist]["stSlider"]:
        parameters += """- """ + distributions_properties[dist]["parameters"][i] + """: $""" + str(_vars[parameter]) + """$
"""
        i += 1
    return parameters
