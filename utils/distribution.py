from typing import Dict, List, Union, Tuple
import streamlit as st


distributions_properties: Dict[str, Union[Dict[str, Union[str, int, bool, List[str], Dict[str, int], Dict[str, Dict[str, float]]]], Dict[str, Union[str, int, bool, List[str], Dict[str, int], Dict[str, Union[Dict[str, int], Dict[str, float]]]]]]] = {
    "norm": {
        "name": "Normal distribution",
        "repr": "Gaussian(μ, σ)",
        "idx": 0,
        "iscontinuous": True,
        "latex": "$\\mathcal{N}(\\mu,\\sigma)$",
        "parameters": ["$\\text{mean}(\\mu)$", "$\\text{Standard Deviation}(\\sigma)$"],
        "parameters-repr": ["μ", "σ"],
        "parameters-latex": ["$\\mu$", "$\\sigma$"],
        "stSlider2idx": {"Mean(μ)": 0, "Standard deviation(σ)": 1},
        "stSlider": {
            "Mean(μ)": {
                "min": -10.0, "max": 10.0, "value": 0.0, "increment": 0.5
            },
            "Standard deviation(σ)": {
                "min": 0.1, "max": 10.0, "value": 1.0, "increment": 0.5
            }
        }
    },
    "uniform": {
        "name": "Uniform distribution",
        "repr": "Uniform(a, b)",
        "idx": 1,
        "iscontinuous": True,
        "latex": "$\\mathcal{U}([a,a+\\Delta])$",
        "parameters": ["$\\text{Lower Bound}(a)$", "$\\text{Scale}(\\Delta)$"],
        "parameters-repr": ["a", "Δ"],
        "parameters-latex": ["$a$", "$\\Delta$"],
        "stSlider2idx": {"Lower Bound(a)": 0, "Scale(Δ)": 1},
        "stSlider": {
            "Lower Bound(a)": {
                "min": -10.0, "max": 10.0, "value": 0.0, "increment": 0.5
            },
            "Scale(Δ)": {
                "min": 0.0, "max": 20.0, "value": 10.0, "increment": 0.5
            }
        }
    },
    "bernoulli": {
        "name": "Bernoulli distribution",
        "repr": "Bernoulli(p)",
        "idx": 2,
        "iscontinuous": False,
        "latex": "$\\text{Ber}(p)$",
        "parameters": ["$\\text{Probability}(p)$"],
        "parameters-repr": ["p"],
        "parameters-latex": ["$p$"],
        "stSlider2idx": {"probability(p)": 0},
        "stSlider": {
            "probability(p)": {
                "min": 0.0, "max": 1.0, "value": 0.5, "increment": 0.05
            }
        }
    },
    "geom": {
        "name": "Geometric distribution",
        "repr": "Geometric(p)",
        "idx": 3,
        "iscontinuous": False,
        "latex": "$\\text{Geo}(p)$",
        "parameters": ["$\\text{Probability}(p)$"],
        "parameters-repr": ["p"],
        "parameters-latex": ["$p$"],
        "stSlider2idx": {"probability(p)": 0},
        "stSlider": {
            "probability(p)": {
                "min": 0.1, "max": 1.0, "value": 0.5, "increment": 0.05
            }
        }
    },
    "binom": {
        "name": "Binomial distribution",
        "repr": "Binomial(n, p)",
        "idx": 4,
        "iscontinuous": False,
        "latex": "$\\text{Bin}(n, p)$",
        "parameters": ["$\\text{Total Trials}(n)$", "$\\text{Probability}(p)$"],
        "parameters-repr": ["n", "p"],
        "parameters-latex": ["$n$", "$p$"],
        "stSlider2idx": {"Total trials(n)": 0, "probability(p)": 1},
        "stSlider": {
            "Total trials(n)": {
                "min": 1, "max": 100, "value": 50, "increment": 1
            },
            "probability(p)": {
                "min": 0.0, "max": 1.0, "value": 0.5, "increment": 0.05
            },
        }
    },
    "poisson": {
        "name": "Poisson distribution",
        "repr": "Poisson(λ)",
        "idx": 5,
        "iscontinuous": False,
        "latex": "$\\text{Poisson}(\\lambda)$",
        "parameters": ["$\\text{#Expected occurrence}(\\lambda)$"],
        "parameters-repr": ["λ"],
        "parameters-latex": ["$\\lambda$"],
        "stSlider2idx": {"#Expected occurrence(λ)": 0},
        "stSlider": {
            "#Expected occurrence(λ)": {
                "min": 0.0, "max": 30.0, "value": 1.0, "increment": 0.5
            }
        }
    },
    "beta": {
        "name": "Beta distribution",
        "repr": "Beta(α,β)",
        "idx": 6,
        "iscontinuous": True,
        "latex": "$\\text{Beta}([\\alpha, \\beta])$",
        "parameters": ["$\\text{Shape Parameter}(\\alpha)$", "$\\text{Shape Parameter}(\\beta)$"],
        "parameters-repr": ["α", "β"],
        "parameters-latex": ["$\\alpha$", "$\\beta$"],
        "stSlider2idx": {"Shape Parameter(α)": 0, "Shape Parameter(β)": 1},
        "stSlider": {
            "Shape Parameter(α)": {
                "min": 1.0, "max": 10.0, "value": 5.0, "increment": 0.5
            },
            "Shape Parameter(β)": {
                "min": 1.0, "max": 10.0, "value": 5.0, "increment": 0.5
            }
        }
    },
    "expon": {
        "name": "Exponential distribution",
        "repr": "Exp(λ)",
        "idx": 7,
        "iscontinuous": True,
        "latex": "$\\text{Exp}(\\lambda)$",
        "parameters": ["$\\text{Rate Parameter}(\\lambda)$"],
        "parameters-repr": ["λ"],
        "parameters-latex": ["$\\lambda$"],
        "stSlider2idx": {"#Expected occurrence(λ)": 0},
        "stSlider": {
            "Rate Parameter(λ)": {
                "min": 0.5, "max": 30.0, "value": 1.0, "increment": 0.5
            }
        }
    }
}


def repr2dist(repr_: str):
    dist = [dist for dist in distributions_properties if distributions_properties[dist]["repr"] == repr_]
    if len(dist) == 0:
        return
    else:
        return dist[0]


def stGetParameters(dist: str) -> Dict[str, Union[int, float]]:
    params: Dict[str, Dict[str, float]] = distributions_properties[dist]["stSlider"]
    var: Dict[str, Union[int, float]] = {}
    for k in params.keys():
        var[k] = st.sidebar.slider(
            k,
            params[k]["min"],
            params[k]["max"],
            params[k]["value"],
            params[k]["increment"]
        )
    return var


def stDistribution(idx=0,
                   dist: Union[str, None] = None,
                   default_values: Dict[str, Dict[str, int]] = None,
                   n_simulations: bool = False,
                   seed: Union[int, None] = None
                   ) -> Tuple[Dict[str, Union[str, int, None, Dict[str, int]]], Dict[str, Union[int, float]]]:
    if seed is None:
        seed: Union[int, None] = st.sidebar.number_input(
            "Enter Seed (-1 mean seed is disabled)",
            min_value=-1,
            max_value=10000,
            value=0,
            step=1
        )
        if seed == -1: seed = None

    if dist is None:
        dist_repr = st.sidebar.selectbox(
            "Select Distribution",
            [distributions_properties[dist]["repr"] for dist in distributions_properties],
            index=idx
        )
        dist: str = repr2dist(dist_repr)

    st_population, st_samples = st.sidebar.columns([1, 1])
    _n: Dict[str, int] = {
        "population": st_population.number_input(
            "Enter Population size",
            min_value=100,
            max_value=400,
            value=200,
            step=10
        ),
        "samples": st_samples.slider(
            "Sample Size",
            min_value=10 if default_values is None else default_values["sample"]["min_value"],
            max_value=100 if default_values is None else default_values["sample"]["max_value"],
            value=50 if default_values is None else default_values["sample"]["value"],
            step=5 if default_values is None else default_values["sample"]["step"]
        )
    }
    if n_simulations:
        _n["simulations"] = st.sidebar.slider("Number of simulations(k)", 10, 100, 50, 10)
    st.sidebar.markdown("## Parameters")
    return {"dist": dist, "seed": seed, "n": _n}, stGetParameters(dist)


def show_parameters(dist: str, _vars: Dict[str, Union[int, float]]) -> str:
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


def graph_label(dist: str, var: List[Union[int, float]]) -> str:
    if dist == "norm":
        return f'N(μ={var[0]}, σ={var[1]})'
    elif dist == "uniform":
        return f'Unif(a={var[0]}, b={var[0] + var[1]})'
    elif dist == "bernoulli":
        return f'Ber(p={var[0]})'
    elif dist == "geom":
        return f'Geo(p={var[0]})'
    elif dist == "binom":
        return f'Bin(n={var[0]}, p={var[1]})'
    elif dist == "poisson":
        return f'Poisson(p={var[0]})'
    elif dist == "beta":
        return f'Beta(α={var[0]}, β={var[1]})'
    elif dist == "expon":
        return f'Exp(λ={var[0]})'
