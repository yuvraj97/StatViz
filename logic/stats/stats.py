import numpy as np
import plotly.express as px

def get_plot(data, title):
    counts, bins = np.histogram(np.array(data * 100, dtype=int), bins=range(0, 101, 2))
    bins = 0.5 * (bins[:-1] + bins[1:]) / 100
    fig = px.bar(x=bins, y=counts, labels={'x': 'p', 'y': '# occurrence'})
    fig.update_layout(title=title,
                      xaxis_title='Proportion of people turning their head to right (p)',
                      yaxis_title='# occurrence of certain (p) in our simulation')
    return fig

def get_sample_with_true_p(population, p):
    a = np.zeros(population, dtype=np.int8)
    _1_s = int(population * p)
    for i in range(0, _1_s):
        a[i] = 1
    np.random.shuffle(a)
    return a

def run(n_population, n_sample, true_p, n_simulations, title, seed):
    if seed is not None: np.random.seed(seed)
    population_sample = get_sample_with_true_p(n_population, true_p)
    estimators = np.empty(n_simulations)
    samples = []
    for i in range(0, n_simulations):
        # Here we randomly select "n_sample" couples out of "population_sample"
        sample = np.random.choice(population_sample, n_sample)
        estimators[i] = sample.sum() / n_sample
        samples.append(sample)
    return population_sample, samples, get_plot(estimators, title), sum(estimators) / n_simulations, estimators
