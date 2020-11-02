import numpy as np
from scipy.stats import bernoulli, geom, binom, poisson
from scipy.stats import beta, expon, uniform, cauchy, norm, chi2
from logic.lln.simulation import get_pdf, simulation

# Continuous Distribution
def gauss_dist(var, n_population, n_samples):
    print("\t \t lln.run.gauss_dist ")
    mu, sigma = var["mu"], var["sigma"]
    dist = norm(loc=mu, scale=sigma)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = dist.pdf(iid_rvs)
    name = f'N(μ={mu}, σ={sigma})'
    return get_pdf(iid_rvs, pdf_rvs, name), simulation(iid_rvs, mu, sigma, n_samples, name)

## Continuous Distribution
def unif_dist(var, n_population, n_samples):
    print("\t \t lln.run.unif_dist ")
    a, b = var["a"], var["b"]
    mu, sigma = (a+b)/2, ((b-a)**2)/12
    dist = uniform(a, b-a)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = dist.pdf(iid_rvs)
    name = f'Unif([a={a}, b={b}])'
    return get_pdf(iid_rvs, pdf_rvs, name), simulation(iid_rvs, mu, sigma, n_samples, name)

## Discreat Distribution
def bernoulli_dist(var, n_population, n_samples):
    print("\t \t lln.run.bernoulli_dist ")
    p= var["p"]
    mu, sigma = p, p*(1-p)
    dist = bernoulli(p)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = np.empty(n_samples)
    pdf_rvs[iid_rvs == 1] = p
    pdf_rvs[iid_rvs == 0] = 1-p
    name = f'Ber(p={p})'
    return get_pdf(iid_rvs, pdf_rvs, name, iscontinuous=False), simulation(iid_rvs, mu, sigma, n_samples, name)

## Discreat Distribution
def geom_dist(var, n_population, n_samples):
    print("\t \t lln.run.geom_dist")
    p = var["p"]
    mu, sigma = 1/p, (1-p)/p**2
    dist = geom(p)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = ((1-p)**iid_rvs)*p
    name = f'Geo(p={p})'
    return get_pdf(iid_rvs, pdf_rvs, name, iscontinuous=False), simulation(iid_rvs, mu, sigma, n_samples, name)

## Discreat Distribution
def binom_dist(var, n_population, n_samples):
    print("\t \t lln.run.binom_dist")
    n, p = var["n"], var["p"]
    from scipy.special import comb
    mu, sigma = n*p, n*p*(1-p)
    dist = binom(n, p)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = np.array([comb(n,min(k, n-k))*(p**k)*((1-p)**(n-k)) for k in iid_rvs])
    name = f'Bin(n={n}, p={p})'
    return get_pdf(iid_rvs, pdf_rvs, name, iscontinuous=False), simulation(iid_rvs, mu, sigma, n_samples, name)

## Discreat Distribution
def poisson_dist(var, n_population, n_samples):
    print("\t \t lln.run.poisson_dist")
    _lambda = var["lambda"]
    from math import factorial
    dist = poisson(_lambda)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = (_lambda**iid_rvs)*(np.e**(-_lambda))/np.array([factorial(k) for k in iid_rvs])
    name = f'Poisson(λ={_lambda})'
    return get_pdf(iid_rvs, pdf_rvs, name, iscontinuous=False), simulation(iid_rvs, _lambda, _lambda, n_samples, name)

## Continuous Distribution
def beta_dist(var, n_population, n_samples):
    print("\t \t lln.run.beta_dist")
    a, b = var["a"], var["b"]
    mu, sigma = a/(a+b), a*b/(  (a + b)**2 * (a + b + 1)  )
    dist = beta(a, b)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = dist.pdf(iid_rvs)
    name = f'Beta(α={a}, β={b})'
    return get_pdf(iid_rvs, pdf_rvs, name), simulation(iid_rvs, mu, sigma, n_samples, name)
    
"""
def exp_dist(var, n_population, n_samples):
    _lambda = var["lambda"]
    mu, sigma = 1/_lambda, 1/_lambda**2
    dist = np.random.exponential(scale=1/_lambda)
    iid_rvs = dist.rvs(size=n_population)[:n_samples]
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs, name), simulation(iid_rvs, mu, sigma, n_samples, f'Exp({_lambda})')
"""

def run_dist(dist, var, n_population, n_samples):
    print("\t ######## lln.run ########")
    if(dist == "gauss"):
        return gauss_dist(var, n_population, n_samples)
    elif(dist == "unif"):
        return unif_dist(var, n_population, n_samples)
    elif(dist == "ber"):
        return bernoulli_dist(var, n_population, n_samples)
    elif(dist == "geo"):
        return geom_dist(var, n_population, n_samples)
    elif(dist == "bin"):
        return binom_dist(var, n_population, n_samples)
    elif(dist == "poiss"):
        return poisson_dist(var, n_population, n_samples)
    elif(dist == "beta"):
        return beta_dist(var, n_population, n_samples)
    """
    elif(dist == "exp"):
        exp_dist(var, n_population, n_samples)
    """
