from logic.lln.simulation import get_pdf, simulation
from distribution import distributions_properties, get_distribution, graph_label

def run(dist, var, n, state):
    #print("          - run(dist=" + dist + ", var=" + str(var) + ", n=" + str(n))
    iscontinuous = distributions_properties[dist]["iscontinuous"]
    n_population, n_samples = n["population"], n["samples"]
    var = [var[k] for k in var.keys()]
    distribution = get_distribution(dist, var)
    population = distribution.rvs(size=n_population)
    iid_rvs = population[:n_samples]
    pdf_rvs = distribution.pdf(iid_rvs) if iscontinuous else distribution.pmf(iid_rvs)
    name = graph_label(dist, var)
    mean = distribution.mean()
    return mean, population, iid_rvs, get_pdf(iid_rvs, pdf_rvs, name, iscontinuous), simulation(iid_rvs, mean, n_samples, name, state)