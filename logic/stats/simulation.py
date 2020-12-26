import numpy as np
import plotly.graph_objects as go

def plot_binary_data(info, seed):
    if seed is not None: np.random.seed(seed)
    count_1, count_2 = info["count-1"], info["count-2"]
    lim = max(count_1, count_2) * 2
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.random.randint(0, lim, count_1),
                             y=np.random.randint(0, lim, count_1),
                             mode='markers',
                             name=info["legend-1"],
                             hovertemplate=info["description-1"],
                             line=dict(color='red')))
    fig.add_trace(go.Scatter(x=np.random.randint(0, lim, count_2),
                             y=np.random.randint(0, lim, count_2),
                             mode='markers',
                             name=info["legend-2"],
                             hovertemplate=info["description-2"],
                             line=dict(color='blue')))
    fig.update_layout(
        title=info["title"],
        xaxis=dict(
            # autorange=True,
            showgrid=False,
            ticks='',
            showticklabels=False
        ),
        yaxis=dict(
            # autorange=True,
            showgrid=False,
            ticks='',
            showticklabels=False
        )
    )
    return fig
