import streamlit as st
from scipy.stats import bernoulli, geom, binom, poisson
from scipy.stats import beta, expon, uniform, cauchy, norm, chi2

idx2distribution = {
    0: "gauss",
    1: "unif",
    2: "ber",
    3: "geo",
    4: "bin",
    5: "poiss",
    6: "beta",
    7: "exp"
}
distribution2idx = {
    "gauss": 0,
    "unif": 1,
    "ber": 2,
    "geo": 3,
    "bin": 4,
    "poiss": 5,
    "beta": 6,
    "exp": 7
}

n = {
    "population": 400,
    "samples": 50,
}

distributions_properties = {
    "gauss": {
        "name": "Normal distribution",
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
    "unif": {
        "name": "Uniform distribution",
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
    "ber": {
        "name": "Bernoulli distribution",
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
    "geo": {
        "name": "Geometric distribution",
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
    "bin": {
        "name": "Binomial distribution",
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
    "poiss": {
        "name": "Poisson distribution",
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
    "exp": {
        "name": "Exponential distribution",
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

which_distribution = {
    "Gaussian(μ, σ)": "gauss",
    "Uniform(a, b)": "unif",
    "Bernoulli(p)": "ber",
    "Geometric(p)": "geo",
    "Binomial(n, p)": "bin",
    "Poisson(λ)": "poiss",
    "Beta(α,β)": "beta",
    "Exp(λ)": "exp"
}

distribution2url = {
    "gauss": "Gaussian",
    "unif": "Uniform",
    "ber": "Bernoulli",
    "geo": "Geometric",
    "bin": "Binomial",
    "poiss": "Poisson",
    "beta": "Beta",
    "exp": "Exponential"
}


def clear(L):
    # print("        clear(L)")
    for e in L:
        e.empty()


# noinspection PyTypeChecker
def stGetParameters(dist):
    # print("          - stGetParameters(dist="+ dist +")")
    params = distributions_properties[dist]["stSlider"]
    # print("              * params: ", params)
    var = {}
    for k in params.keys(): var[k] = st.sidebar.slider(k, params[k]["min"], params[k]["max"], params[k]["value"],
                                                       params[k]["increment"])
    # print("              * var: ", var)
    return var


def stDistribution(dist, default_vals=None, n_simulations=False):
    # print("          - stDistribution(dist="+ dist + ", state)")
    _n = {
        "population": st.sidebar.number_input("Enter Population size", min_value=100, max_value=400, value=200, step=10),
        "samples": st.sidebar.slider("Sample Size",
                                     min_value=10 if default_vals is None else default_vals["sample"]["min_value"],
                                     max_value=100 if default_vals is None else default_vals["sample"]["max_value"],
                                     value=50 if default_vals is None else default_vals["sample"]["value"],
                                     step=5 if default_vals is None else default_vals["sample"]["step"]
                                     )
    }
    if(n_simulations):
        _n["simulations"] = st.sidebar.slider("Number of simulations(k)", 10, 100, 50, 10)
    st.sidebar.markdown("## Parameters")
    # print("              * n: ",n)
    return stGetParameters(dist), _n


def get_distribution(dist, var):
    # print("          - get_distribution(dist="+ dist + ", var= " + str(var) +")")
    if dist == "gauss":
        return norm(*var)
    elif dist == "unif":
        return uniform(*var)
    elif dist == "ber":
        return bernoulli(*var)
    elif dist == "geo":
        return geom(*var)
    elif dist == "bin":
        return binom(*var)
    elif dist == "poiss":
        return poisson(*var)
    elif dist == "beta":
        return beta(*var)
    elif dist == "exp":
        return expon(1 / var[0])


def graph_label(dist, var):
    # print("          - graph_label(dist="+ dist + ", var= " + str(var) +")")
    if dist == "gauss":
        return f'N(μ={var[0]}, σ={var[1]})'
    elif dist == "unif":
        return f'Unif(a={var[0]}, b={var[0] + var[1]})'
    elif dist == "ber":
        return f'Ber(p={var[0]})'
    elif dist == "geo":
        return f'Geo(p={var[0]})'
    elif dist == "bin":
        return f'Bin(n={var[0]}, p={var[1]})'
    elif dist == "poiss":
        return f'Poisson(p={var[0]})'
    elif dist == "beta":
        return f'Beta(α={var[0]}, β={var[1]})'
    elif dist == "exp":
        return f'Exp(λ={var[0]})'
