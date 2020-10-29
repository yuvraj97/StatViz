import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def simulation_mpl(distribution, n_sim, name=""):
    
    fig = plt.figure()
    ax = fig.gca()
    
    mean, std = distribution.mean(), distribution.std()
    
    ns = np.linspace(1, n_sim, n_sim, dtype = int)
    
    # Generate n i.i.d. random variables from the distribution
    iid_rv = distribution.rvs(n_sim)
    
    # sample mean for each n
    sample_mean = []
    for n in range(n_sim):
        sample_mean.append(np.mean(iid_rv[:n+1]))
    
    ax.plot(ns, iid_rv, 'o', color='grey', alpha=0.5)
    label = '$\\bar X_n$ for $X_i \sim$' + name
    ax.plot(ns, sample_mean, 'g-', lw=3, alpha=0.6, label=label)
    ax.plot(ns, [mean] * n_sim, 'k--', lw=1.5, label='$\mu$')
    ax.vlines(ns, mean, iid_rv, lw=0.2)
    
    
    bbox = (0.0, 1.0 , 1.0, 0.1)
    legend_args = {'ncol': 2,
                   'bbox_to_anchor': bbox,
                   'mode': 'expand'}
    
    ax.legend(**legend_args, fontsize=12)
    return fig

def get_pdf(iid_rvs, pdf_rvs):
    idx = np.argsort(iid_rvs)
    fig = go.Figure()

    iid_rvs, pdf_rvs = iid_rvs[idx], pdf_rvs[idx]
    pdf_lower, pdf_upper = pdf_rvs - 0.4, pdf_rvs + 0.4
    # Add traces
    fig.add_trace(go.Scatter(x=iid_rvs, y=pdf_rvs,
                             mode='lines',
                             name="pdf",
                             line=dict(color='royalblue', width=4),))
    fig.add_trace(go.Scatter(
        x=np.concatenate([iid_rvs, np.flip(iid_rvs)]), # x, then x reversed
        y=np.concatenate([pdf_lower, pdf_upper]), # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=False
    ))
    # Edit the layout
    fig.update_layout(xaxis_title='<b>iid</b> Random Variables(x)',
                       yaxis_title='pdf(x)')
    fig.update_yaxes(range=[pdf_lower.min()-0.4, pdf_upper.max()+0.4])
    return fig
        

def simulation(iid_rv, mean, sigma, n_sim, name=""):
    ns = np.linspace(1, n_sim, n_sim, dtype = int)
    
    # sample mean for each n
    average = [0]*n_sim
    x = [0]*(3 * n_sim - 1)
    y = [0]*(3 * n_sim - 1)
    n, counter = 0, 0
    while(n < 3 * n_sim - 1):
        if ((n+1) % 3 == 0):
            x[n], y[n] = None, None
        else:
            average[counter] = np.mean(iid_rv[:counter+1])
            x[n],   y[n]   = ns[counter], iid_rv[counter]
            x[n+1], y[n+1] = ns[counter], mean
            counter += 1
            n += 1
        n += 1
    
    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y,
                             mode='lines',
                             showlegend=False,
                             line=dict(color='rgb(189,189,189)', width=1),))
    
    fig.add_trace(go.Scatter(x=ns, y=average,
                        mode='lines',
                        name='Sample Average',
                        line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=ns, y=iid_rv,
                        mode='markers',
                        name='Random variable(x)',
                        line=dict(color='purple')))
    fig.add_trace(go.Scatter(x = ns, y = [mean] * n_sim,
                             mode='lines',
                             name='mean',
                             line=dict(
                                         color="green",
                                         width=4,
                                         dash="dot")
                                      )
                            )
    
    # Edit the layout
    fig.update_layout(xaxis_title='Number of simulations',
                       yaxis_title='<b>iid</b> Random Variable')
    return fig