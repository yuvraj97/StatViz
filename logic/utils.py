from typing import Dict, Union, Tuple, List
import numpy as np
import plotly.graph_objects as go
from plotly.graph_objs import Figure

def plot_histogram(data: np.ndarray,
                   description: Dict[str, Union[str, Dict[str, str]]],
                   num_bins: int = -1,
                   convert_into_probability_plot: bool = False,
                   fig: Figure = None,
                   isMobile: bool = False,
                   tilde_equals: str = '~',
                   bins: np.ndarray = None,
                   counts: np.ndarray = None,
                   centralize_bins: bool = True,
                   showlegend: bool = True) -> Tuple[Figure, Tuple[np.ndarray, np.ndarray]]:
    """
    description = {
        "title": {
            "main": "Title of plot",
            "x": "x-axis title",
            "y": "y-axis title"
        },
        "label": {
            "main": "Legend",
            "x": "x-axis label",
            "y": "y-axis label",
            "force": False
        }
    }
    """
    if num_bins == -1 and bins is None:
        num_bins = len(np.unique(data))//4
    # bins: np.ndarray
    if bins is None:
        # noinspection PyArgumentList
        bins = np.linspace(data.min(), data.max(), num_bins)
    if counts is None: counts, bins = np.histogram(data, bins=bins)
    if centralize_bins: bins = 0.5 * (bins[:-1] + bins[1:])
    if convert_into_probability_plot:
        counts  = counts/counts.sum()
        description["title"]["y"] = description['title']['y'] if "force" in description['title'] and description['title']['force'] else f"Probability of {description['title']['x']}<br>Falling into particular bin"
        hovertemplate = description["label"]["x"] + ' (x) ' + tilde_equals + ' %{x}<br>Probability(x ' + tilde_equals + ' %{x}): %{y}'
    else:
        hovertemplate = description["label"]["x"] + ' (x) ' + tilde_equals + ' %{x}<br>' + description["label"]["y"] + '(x ' + tilde_equals + ' %{x}): %{y}'
    if fig is None: fig: Figure = go.Figure()
    fig.add_trace(go.Bar(x=bins,
                         y=counts,
                         name=description["label"]["main"],
                         hovertemplate=hovertemplate,
                         showlegend=False if description["label"]["main"] is None else True
                         ))
    fig.update_layout(title=description["title"]["main"],
                      xaxis_title=description["title"]["x"],
                      yaxis_title=description["title"]["y"])
    fig.update_layout(showlegend=False if isMobile or not showlegend else True)
    return fig, (counts, bins)

def line_plot(x: np.ndarray,
              y: np.ndarray,
              description: dict,
              fig: Figure = None,
              mode="lines",
              isMobile: bool = False) -> Figure:
    """
    description={
        "title": {
            "main": "Title of plot",
            "x": "x-axis title",
            "y": "y-axis title"
        },
        "label": {
            "main": "Legend",
        },
        "hovertemplate": "x-label (x): %{x}<br>y-label(x=%{x}): %{y}",
        "color": "green"
    }
    """
    if fig is None:
        fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y,
                             mode=mode,
                             name=description["label"]["main"],
                             hovertemplate=description["hovertemplate"],
                             line=dict(color=description["color"])))
    if "title" in description:
        if "main" in description["title"]: fig.update_layout(title=description["title"]["main"])
        if "x" in description["title"]: fig.update_layout(xaxis_title=description["title"]["x"])
        if "y" in description["title"]: fig.update_layout(yaxis_title=description["title"]["y"])
    fig.update_layout(showlegend=False if isMobile else True)
    return fig

def animate_dot_2D(x, y, title, button_label="Start"):
    fig = go.Figure(
        data=[go.Scatter(x=[0], y=[0])],
        layout=go.Layout(
            xaxis=dict(range=[x.min() - 2, x.max() + 2], autorange=False),
            yaxis=dict(range=[y.min() - 2, y.max() + 2], autorange=False),
            title=title,
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label=button_label,
                              method="animate",
                              args=[None])])]
        ),
        frames=[go.Frame(data=[go.Scatter(x=[x[i]], y=[y[i]])]) for i in range(len(x))]
    )
    return fig
