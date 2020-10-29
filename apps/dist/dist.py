import numpy as np
from scipy.stats import bernoulli, geom, binom, poisson
from scipy.stats import beta, expon, uniform, cauchy, norm, chi2
from apps.dist.run import get_pdf, simulation

def gauss_dist(mu, sigma, n_sim):
    dist = norm(loc=mu, scale=sigma)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, mu, sigma, n_sim, f'$Norm({mu}, {sigma})$')

def unif_dist(a, b, n_sim):
    mu, sigma = (a+b)/2, ((b-a)**2)/12
    dist = uniform.rvs(a, b-a)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, mu, sigma, n_sim, f'$Unif([{a}, {b}])$')


def bernoulli_dist(p, n_sim):
    mu, sigma = p, p*(1-p)
    dist = bernoulli.rvs(p)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, mu, sigma, n_sim, f'$Ber(p={p})$')
    
def geom_dist(p, n_sim):
    mu, sigma = 1/p, (1-p)/p**2
    dist = geom.rvs(p)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, mu, sigma, n_sim, f'$Geo(p={p})$')
    
def binom_dist(n, p, n_sim):
    mu, sigma = n*p, n*p*(1-p)
    dist = binom(n, p)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, mu, sigma, n_sim, f'$Geo(p={p})$')
    
def poisson_dist(_lambda, n_sim):
    dist = poisson(_lambda)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, _lambda, _lambda, n_sim, f'$Poisson({_lambda})$')
    
def beta_dist(a, b, n_sim):
    mu, sigma = a/(a+b), a*b/(  (a + b)**2 * (a + b + 1)  )
    dist = beta.rvs(a, b)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, mu, sigma, n_sim, f'$Beta(a={a}, b={b})$')
    
"""
def exp_dist(_lambda, n_sim):
    mu, sigma = 1/_lambda, 1/_lambda**2
    dist = np.random.exponential(scale=1/_lambda)
    iid_rvs = dist.rvs(size=n_sim)
    pdf_rvs = dist.pdf(iid_rvs)
    return get_pdf(iid_rvs, pdf_rvs), simulation(iid_rvs, mu, sigma, n_sim, f'$Exp({_lambda})$')
"""