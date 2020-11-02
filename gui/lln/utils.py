import streamlit as st
d = {
    0: "gauss", 
    1: "unif",
    2: "ber",
    3: "geo",
    4: "bin",
    5: "poiss",
    6: "beta",
    7: "exp"
}
distributions_properties={
    "n_population": 400,
    "n_samples"   : 50,
    "gauss" : {"idx": 0, "mu" : 0.0, "sigma" : 0.3},
    "unif"  : {"idx": 1, "a"  : 0.0,   "b"   : 1.0},
    "ber"   : {"idx": 2, "p"  : 0.5},
    "geo"   : {"idx": 3, "p"  : 0.25},
    "bin"   : {"idx": 4, "n"  : 50 ,   "p"   : 0.5},
    "poiss" : {"idx": 5, "lambda" : 15.0},
    "beta"  : {"idx": 6, "a"  : 5.0,   "b"   : 5.0},
    "exp"   : {"idx": 7, "lambda" : 1.0}
     }
which_distribution = ( 
    "Gaussian(μ, σ)",
    "Uniform(a, b)",
    "Bernoulli(p)", 
    "Geometric(p)", 
    "Binomial(n, p)",
    "Poisson(λ)",
    "Beta(α,β)",
    "Exp(λ)"
)

def clear(L):
    for e in L:
        e.empty()

def stDistribution(dist, state, sidebar):
    print("\t \t lln.utils.stDistribution")
    if(sidebar):
        population, sample, writeParameter, mu, sigma, a, b, p, n, _lambda = [st.sidebar.empty() for i in range(10)]
    else:
        population, sample, writeParameter, mu, sigma, a, b, p, n, _lambda = [st.empty() for i in range(10)]
    #clear([distribution, population, sample, mu, sigma, a, b, p, n, _lambda])

    new_n_population = population.number_input("Enter Population size", min_value=100, max_value=800, value=400, step=10)
    new_n_sample = sample.slider("Sample Size", min_value = 10, max_value = 100, value = state.lln["n_samples"], step = 5)
    state.lln["n_population"], state.lln["n_samples"] = new_n_population, new_n_sample
    writeParameter.markdown("## Parameters")
    if(dist =="gauss"):
        new_mu = mu.slider(f"Mean(μ)", min_value = -10.0, max_value = 10.0, value = state.lln[dist]["mu"] , step = 0.5)
        new_sigma = sigma.slider("Standard deviation(σ)", min_value = 0.1, max_value = 3.0, value = state.lln[dist]["sigma"], step = 0.1)
        var = {"idx": state.lln[dist]["idx"], "mu" : new_mu, "sigma" : new_sigma}
    elif(dist =="unif" or dist == "beta"):
        new_a = a.slider("a", min_value = -10.0, max_value = 10.0, value = state.lln[dist]["a"], step = 0.5)
        new_b = b.slider("b", min_value = new_a + 1, max_value = new_a + 11, value = new_a + 6, step = 0.5)
        var = {"idx": state.lln[dist]["idx"], "a"  : new_a, "b"   : new_b}
    elif(dist =="ber" or dist == "geo"):
        new_p = p.slider("p", min_value = 0.0, max_value = 1.0, value = state.lln[dist]["p"], step = 0.05)
        var = {"idx": state.lln[dist]["idx"], "p"  : new_p}
    elif(dist =="bin"):
        new_p = p.slider("p", min_value = 0.0, max_value = 1.0, value = state.lln[dist]["p"], step = 0.05)
        new_n = n.slider("n", min_value = 1, max_value = 100, value = state.lln[dist]["n"], step = 1)
        var = {"idx": state.lln[dist]["idx"], "n"  : new_n,   "p"   : new_p}        
    elif(dist =="poiss" or dist == "exp"):
        new_lambda = _lambda.slider("λ", min_value = 0.0, max_value = 30.0, value = state.lln["poiss"]["lambda"], step = 0.5)
        var = {"idx": state.lln[dist]["idx"], "lambda" : new_lambda}
    print("\t \t returning,",dist)
    return var

def getDistByIndex(idx):
    print("lln.utils.getDistByIndex")
    return d[idx]