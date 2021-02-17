from typing import Dict, Union
from gui.clt.display import stDisplay
from distribution import distributions_properties, which_distribution, stDistribution
from utils import set_get_URL

def main(distribution, state):
    dist: str = which_distribution[distribution]

    set_get_URL(parameters={
        "dist" : distributions_properties[dist]["name"],
        "topic": "remove"
    })

    var: Dict[str, Union[int, float]]
    n: Dict[str, int]
    var, n = stDistribution(dist, default_values={
        "sample": {
            "min_value" : 1,
            "max_value" : 40,
            "value"     : 30,
            "step"      : 1,
        }
    }, n_simulations=True)

    if state.stSettings["seed-checkbox"].checkbox("Enable Seed", True):
        state.stSettings["seed"] = state.stSettings["seed-number"].number_input("Enter Seed", 0, 10000, 0, 1)

    stDisplay(dist, var, n, state)
