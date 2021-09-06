from typing import Dict, List, Union, Tuple, Type
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
                "min": -10.0, "max": 10.0, "value": 0.0, "increment": 0.5, "type": float
            },
            "Standard deviation(σ)": {
                "min": 0.1, "max": 10.0, "value": 1.0, "increment": 0.5, "type": float
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
                "min": -10.0, "max": 10.0, "value": 0.0, "increment": 0.5, "type": float
            },
            "Scale(Δ)": {
                "min": 0.0, "max": 20.0, "value": 10.0, "increment": 0.5, "type": float
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
                "min": 0.0, "max": 1.0, "value": 0.5, "increment": 0.05, "type": float
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
                "min": 0.1, "max": 1.0, "value": 0.5, "increment": 0.05, "type": float
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
                "min": 1, "max": 100, "value": 50, "increment": 1, "type": int
            },
            "probability(p)": {
                "min": 0.0, "max": 1.0, "value": 0.5, "increment": 0.05, "type": float
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
                "min": 0.0, "max": 30.0, "value": 1.0, "increment": 0.5, "type": float
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
                "min": 1.0, "max": 10.0, "value": 5.0, "increment": 0.5, "type": float
            },
            "Shape Parameter(β)": {
                "min": 1.0, "max": 10.0, "value": 5.0, "increment": 0.5, "type": float
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
                "min": 0.5, "max": 30.0, "value": 1.0, "increment": 0.5, "type": float
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

    def check_param_limit(_param, _value, _min, _max):
        if _value < _min or _value > _max:
            st.error(f'{_param} should be in between ${_min}$ and ${_max}$')
            raise ValueError

    dist_parameters: Dict[str, Dict[str, Union[float, Type[float]]]] = distributions_properties[dist]["stSlider"]
    dist_parameters_list = list(dist_parameters.keys())
    var: Dict[str, Union[int, float]] = {}
    for param1, param2 in zip(*[iter(dist_parameters_list)] * 2):
        st_param1, st_param2 = st.sidebar.columns([1, 1])
        _type1, _type2 = dist_parameters[param1]["type"], dist_parameters[param2]["type"]
        var[param1] = _type1(st_param1.text_input(param1, dist_parameters[param1]["value"]))
        var[param2] = _type2(st_param2.text_input(param2, dist_parameters[param2]["value"]))
        check_param_limit(param1, var[param1], dist_parameters[param1]["min"], dist_parameters[param1]["max"])
        check_param_limit(param2, var[param2], dist_parameters[param2]["min"], dist_parameters[param2]["max"])
    if len(dist_parameters_list) % 2 != 0:
        param1 = dist_parameters_list[-1]
        _type1 = dist_parameters[param1]["type"]
        var[param1] = _type1(st.sidebar.text_input(param1, dist_parameters[param1]["value"]))
        check_param_limit(param1, var[param1], dist_parameters[param1]["min"], dist_parameters[param1]["max"])

    return var


def stDistribution(idx=0,
                   dist: Union[str, None] = None,
                   default_values: Dict[str, Dict[str, int]] = None,
                   n_simulations: bool = False,
                   seed: Union[int, None] = None
                   ) -> Tuple[Dict[str, Union[str, int, None, Dict[str, int]]], Dict[str, Union[int, float]]]:

    if dist is None:
        dist_repr = st.sidebar.selectbox(
            "Select Distribution",
            [distributions_properties[dist]["repr"] for dist in distributions_properties],
            index=idx
        )
        dist: str = repr2dist(dist_repr)

    st_seed, st_population, st_samples = st.sidebar.columns([0.8, 1, 1])

    if seed is None:
        seed: Union[int, None] = int(st_seed.text_input("Enter Seed (-1: disable)", "0"))
        if seed == -1: seed = None

    _n: Dict[str, int] = {
        "population": int(st_population.text_input("Enter Population size", "200")),
        "samples": int(st_samples.text_input("Sample Size", "50"))
    }
    if n_simulations:
        _n["simulations"] = int(st.sidebar.text_input("Number of simulations(k)", "50"))
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
