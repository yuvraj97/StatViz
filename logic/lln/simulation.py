import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import Figure

def simulation_mpl(distribution, n_samples, name=""):
    fig = plt.figure()
    ax = fig.gca()

    mean, std = distribution.mean(), distribution.std()

    ns = np.linspace(1, n_samples, n_samples, dtype=int)

    # Generate n i.i.d. random variables from the distribution
    iid_rvs = distribution.rvs(n_samples)

    # sample mean for each n
    sample_mean = []
    for n in range(n_samples):
        sample_mean.append(np.mean(iid_rvs[:n + 1]))

    ax.plot(ns, iid_rvs, 'o', color='grey', alpha=0.5)
    label = '$\\bar X_n$ for $X_i \\sim$' + name
    ax.plot(ns, sample_mean, 'g-', lw=3, alpha=0.6, label=label)
    ax.plot(ns, [mean] * n_samples, 'k--', lw=1.5, label='$\\mu$')
    ax.vlines(ns, mean, iid_rvs, lw=0.2)

    bbox = (0.0, 1.0, 1.0, 0.1)
    legend_args = {'ncol': 2,
                   'bbox_to_anchor': bbox,
                   'mode': 'expand'}

    ax.legend(**legend_args, fontsize=12)
    return fig

def continuous_chart(fig: Figure, iid_rvs:  np.ndarray, pdf_rvs: np.ndarray) -> None:
    std = np.std(iid_rvs)
    pdf_lower, pdf_upper = pdf_rvs - std / 2, pdf_rvs + std / 2
    fig.add_trace(go.Scatter(x=iid_rvs, y=pdf_rvs,
                             mode='lines',
                             hovertemplate='Random Variable(x): %{x}<br>PDF(x)=%{y}',
                             name="pdf",
                             line=dict(color='royalblue', width=4), ))
    fig.add_trace(go.Scatter(
        x=np.concatenate([iid_rvs, np.flip(iid_rvs)]),  # x, then x reversed
        y=np.concatenate([pdf_lower, np.flip(pdf_upper)]),  # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=False
    ))
    fig.update_yaxes(range=[pdf_lower.min() - 0.4, pdf_upper.max() + 0.4])
    fig.update_layout(xaxis_title='<b>iid</b> Random Variables(x)',
                      yaxis_title='Simulated PDF(x)')

def discrete_chart(fig: Figure, iid_rvs:  np.ndarray, pdf_rvs: np.ndarray) -> None:
    n_samples = len(iid_rvs)
    x = [0] * (3 * n_samples - 1)
    y = [0] * (3 * n_samples - 1)
    n, counter = 0, 0
    while n < 3 * n_samples - 1:
        if (n + 1) % 3 == 0:
            x[n], y[n] = None, None
        else:
            x[n], y[n] = iid_rvs[counter], pdf_rvs[counter]
            x[n + 1], y[n + 1] = iid_rvs[counter], 0
            counter += 1
            n += 1
        n += 1

    fig.add_trace(go.Scatter(x=x, y=y,
                             mode='lines',
                             showlegend=False,
                             line=dict(color='rgb(189,189,189)', width=1), ))
    fig.add_trace(go.Scatter(x=iid_rvs, y=pdf_rvs,
                             mode='markers',
                             name='PMF(x)',
                             hovertemplate='Random Variable(x): %{x}<br>PMF(x)=%{y}',
                             line=dict(color='purple')))
    fig.update_layout(xaxis_title='<b>iid</b> Random Variables(x)',
                      yaxis_title='Simulated PMF(x)')

def get_pdf(iid_rvs:  np.ndarray, pdf_rvs: np.ndarray, name: str, iscontinuous: bool = True) -> Figure:
    idx = np.argsort(iid_rvs)
    fig = go.Figure()

    iid_rvs, pdf_rvs = iid_rvs[idx], pdf_rvs[idx]

    # Add traces
    if iscontinuous:
        continuous_chart(fig, iid_rvs, pdf_rvs)
    else:
        discrete_chart(fig, iid_rvs, pdf_rvs)

    # Edit the layout
    fig.update_layout(title=name)

    return fig

def plot_data(data: np.ndarray, title: str, width: int) -> Figure:
    margin = 10000
    data = np.array(data * margin, dtype=int)
    _min, _max = int(np.min(data)), int(np.max(data))
    width = int(width*(_max-_min+2)//len(data))
    counts, bins = np.histogram(data, bins=range(_min-1, _max+width, width))
    bins = 0.5 * (bins[:-1] + bins[1:]) / margin
    fig = px.bar(x=bins, y=counts, labels={'x': 'Height', 'y': '# occurrence'})
    fig.update_layout(title=title,
                      xaxis_title='Random Variable',
                      yaxis_title='# occurrence of certain random variable')
    return fig

def simulation(iid_rvs: np.ndarray, mean: float, n_samples: int, name: str, state) -> Figure:
    ns = np.linspace(1, n_samples, n_samples, dtype=int)

    # sample mean for each n
    average = [0] * n_samples
    x = [0] * (3 * n_samples - 1)
    y = [0] * (3 * n_samples - 1)
    n, counter, _sum = 0, 0, 0
    while n < 3 * n_samples - 1:
        if (n + 1) % 3 == 0:
            x[n], y[n] = None, None
        else:
            _sum += iid_rvs[counter]
            # noinspection PyTypeChecker
            average[counter] = _sum / (counter + 1)
            x[n], y[n] = ns[counter], iid_rvs[counter]
            x[n + 1], y[n + 1] = ns[counter], mean
            counter += 1
            n += 1
        n += 1

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y,
                             mode='lines',
                             showlegend=False,
                             line=dict(color='rgb(189,189,189)', width=1), ))

    fig.add_trace(go.Scatter(x=ns, y=average,
                             mode='lines',
                             name='Sample Average',
                             hovertemplate='In this Simulation<br>For <b style="color:pink">Sample Size</b>=%{x}<br>Sample Average=%{y}',
                             line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=ns, y=iid_rvs,
                             mode='markers',
                             name='Random variable(x)',
                             hovertemplate='Random Draw(x): %{y}',
                             line=dict(color='purple')))
    fig.add_trace(go.Scatter(x=ns, y=[mean] * n_samples,
                             mode='lines',
                             name='mean',
                             hovertemplate='True mean: %{y}',
                             line=dict(
                                 color="green",
                                 width=4,
                                 dash="dot")
                             )
                  )

    # Edit the layout
    fig.update_layout(title=name,
                      xaxis_title='Sample Size',
                      yaxis_title='<b>iid</b> Random Variable')
    fig.update_layout(showlegend=False if state.isMobile else True)
    return fig
