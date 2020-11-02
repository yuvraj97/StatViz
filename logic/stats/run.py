import numpy as np
import matplotlib.pyplot as plt

def get_sample_with_true_p(population,p):
    a=[0]*population
    _1_s = int(population*p)
    for i in range(0,_1_s):
        a[i]=1
    np.random.shuffle(a)
    return a

def simulate(n_population, n_sample, true_p, n_populationulation):
    population_sample = get_sample_with_true_p(n_population, true_p)
    estimators = []
    for i in range(0,n_populationulation):
        # Here we randomly select 124 couples out of 5000
        sample = np.random.choice(population_sample,n_sample)
        estimators.append(sum(sample)/n_sample)
    fig = plt.figure()
    ax = fig.gca()
    ax.hist(estimators, histtype='bar', rwidth=0.95)
    #ax.set_xlim(0,1)
    ax.set_xlabel("Proportion of people turning their head to right (p)")
    ax.set_ylabel("# occurence of certain (p) in our simulation")
    return fig, sum(estimators)/ n_populationulation, estimators