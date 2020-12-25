from typing import Dict, Union

import numpy as np
from plotly.graph_objs import Figure
import plotly.express as px

def plot_histogram(data: np.ndarray, description: Dict[str, Union[str, Dict[str, str]]], num_bins: int = -1) -> Figure:
    if num_bins == -1:
        num_bins = len(np.unique(data))//4
    bins = np.linspace(min(data), max(data), num_bins)
    counts, bins = np.histogram(data, bins=bins)
    bins = 0.5 * (bins[:-1] + bins[1:])
    fig = px.bar(x=bins, y=counts, labels={'x': description["label"]["x"], 'y': description["label"]["y"]})
    fig.update_layout(title=description["title"]["main"],
                      xaxis_title=description["title"]["x"],
                      yaxis_title=description["title"]["y"])
    return fig
