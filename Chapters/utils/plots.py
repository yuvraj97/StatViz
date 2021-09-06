from typing import Dict, Union, Tuple
import numpy as np
import plotly.graph_objects as go
from plotly.graph_objs import Figure
import matplotlib.pyplot as plt


def plot_binary_data(info: Dict[str, Union[str, int]], seed: Union[int, None]) -> Figure:
    if seed is not None: np.random.seed(seed)
    count_1: int
    count_2: int
    count_1, count_2 = info["count-1"], info["count-2"]
    lim: int = max(count_1, count_2) * 2
    fig: Figure = go.Figure()
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
        num_bins = len(np.unique(data)) // 4
    if bins is None:
        bins = np.linspace(np.min(data), np.max(data), num_bins)
    if counts is None: counts, bins = np.histogram(data, bins=bins)
    if centralize_bins: bins = 0.5 * (bins[:-1] + bins[1:])
    if convert_into_probability_plot:
        counts = counts / counts.sum()
        if "force" in description['title'] and description['title']['force']:
            description["title"]["y"] = f"Probability of {description['title']['x']}<br>Falling into particular bin"
        hovertemplate = f"{description['label']['x']} (x)  {tilde_equals}  %{{x}}<br>" \
                        f"Probability(x {tilde_equals}  %{{x}}): %{{y}}"
    else:
        hovertemplate = f"{description['label']['x']} (x)  {tilde_equals}  %{{x}}<br>" \
                        f"{description['label']['y']} (x {tilde_equals}  %{{x}}): %{{y}}"
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


def plot_histogram3D(x: np.ndarray,
                     y: np.ndarray,
                     description: Dict[str, Union[str, Dict[str, str]]],
                     bins: Tuple[int, int] = (25, 25),
                     convert_into_probability_plot: bool = False,
                     fig: Figure = None,
                     isMobile: bool = False,
                     showlegend: bool = True,
                     bargap: float = 0.02,
                     width: int = 585,
                     height: int = 630,
                     tilda="~"):
    def bar_data(position3d, size=(1, 1, 1)):
        # position3d - 3-list or array of shape (3,) that represents the point of coords (x, y, 0),
        # where a bar is placed
        # size = a 3-tuple whose elements are used to scale a unit cube to get a paralelipipedic bar
        # returns - an array of shape(8,3) representing the 8 vertices of  a bar at position3d

        bar = np.array([[0, 0, 0],
                        [1, 0, 0],
                        [1, 1, 0],
                        [0, 1, 0],
                        [0, 0, 1],
                        [1, 0, 1],
                        [1, 1, 1],
                        [0, 1, 1]], dtype=float)  # the vertices of the unit cube

        bar *= np.asarray(size)  # scale the cube to get the vertices of a parallelipipedic bar
        bar += np.asarray(position3d)  # translate each  bar on the directio OP, with P=position3d
        return bar

    def triangulate_bar_faces(positions, sizes=None):
        # positions - array of shape (N, 3) that contains all positions in the plane z=0,
        # where a histogram bar is placed
        # sizes -  array of shape (N,3); each row represents the sizes to scale a unit cube to get a bar
        # returns the array of unique vertices, and the lists i, j, k to be used in instantiating the go.Mesh3d class

        if sizes is None:
            sizes = [(1, 1, 1)] * len(positions)
        else:
            if isinstance(sizes, (list, np.ndarray)) and len(sizes) != len(positions):
                raise ValueError('Your positions and sizes lists/arrays do not have the same length')

        all_bars = [bar_data(pos, size) for pos, size in zip(positions, sizes) if size[2] != 0]
        p, q, r = np.array(all_bars).shape

        # extract unique vertices from the list of all bar vertices
        vertices, ixr = np.unique(np.array(all_bars).reshape(p * q, r), return_inverse=True, axis=0)

        # for each bar, derive the sublists of indices i, j, k assocated to its chosen  triangulation
        I, J, K = [], [], []

        for k in range(len(all_bars)):
            I.extend(np.take(ixr,
                             [8 * k, 8 * k + 2, 8 * k, 8 * k + 5, 8 * k, 8 * k + 7, 8 * k + 5, 8 * k + 2, 8 * k + 3,
                              8 * k + 6, 8 * k + 7, 8 * k + 5]))
            J.extend(np.take(ixr,
                             [8 * k + 1, 8 * k + 3, 8 * k + 4, 8 * k + 1, 8 * k + 3, 8 * k + 4, 8 * k + 1, 8 * k + 6,
                              8 * k + 7, 8 * k + 2, 8 * k + 4, 8 * k + 6]))
            K.extend(np.take(ixr,
                             [8 * k + 2, 8 * k, 8 * k + 5, 8 * k, 8 * k + 7, 8 * k, 8 * k + 2, 8 * k + 5, 8 * k + 6,
                              8 * k + 3, 8 * k + 5, 8 * k + 7]))

        return vertices, I, J, K  # triangulation vertices and I, J, K for mesh3d

    def get_plotly_mesh3d(range_extent=0.2):
        # x, y- array-like of shape (n,), defining the x, and y-coordinates of data set for which we plot a 3d hist
        hist, xedges, yedges = np.histogram2d(x, y,
                                              bins=bins,
                                              range=[[np.min(x) - range_extent, np.max(x) + range_extent],
                                                     [np.min(y) - range_extent, np.max(y) + range_extent]])
        xsize = xedges[1] - xedges[0] - bargap
        ysize = yedges[1] - yedges[0] - bargap
        xe, ye = np.meshgrid(xedges[:-1], yedges[:-1])
        ze = np.zeros(xe.shape)

        positions = np.dstack((xe, ye, ze))
        m, n, p = positions.shape
        positions = positions.reshape(m * n, p)
        sizes = np.array([(xsize, ysize, h) for h in hist.flatten()])
        vertices, I, J, K = triangulate_bar_faces(positions, sizes=sizes)
        X, Y, Z = vertices.T
        return X, Y, Z, I, J, K

    X, Y, Z, I, J, K = get_plotly_mesh3d()

    if convert_into_probability_plot:
        Z = Z / Z.sum()
        hovertemplate = f"{description['label']['x']} {tilda} %{{x}}<br>{description['label']['y']} {tilda} %{{y}}<br>" \
                        f"Probability(x {tilda} %{{x}} and y {tilda} %{{y}}): %{{z}}"
    else:
        hovertemplate = f"{description['label']['x']} {tilda} %{{x}}<br>{description['label']['y']} {tilda} %{{y}}<br>" \
                        f"{description['label']['x']}(x {tilda} %{{x}} and y {tilda} %{{y}}): %{{z}}"

    if fig is None: fig: Figure = go.Figure()

    fig.add_trace(go.Mesh3d(x=X, y=Y, z=Z,
                            i=I, j=J, k=K,
                            name=description["label"]["main"],
                            hovertemplate=hovertemplate,
                            showlegend=False if description["label"]["main"] is None else True))
    fig.update_layout(width=width,
                      height=height,
                      title=description["title"]["main"],
                      xaxis_title=description["title"]["x"],
                      yaxis_title=description["title"]["y"],
                      # zaxis_title=description["title"]["z"],
                      scene=dict(
                          camera_eye_x=-1.25,
                          camera_eye_y=1.25,
                          camera_eye_z=1.25),
                      showlegend=False if isMobile or not showlegend else True)
    return fig


def surface_plot3D(x, y, z,
                   description: dict,
                   fig: Figure = None,
                   colorscale='Viridis',
                   opacity=0.5,
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
    fig.add_trace(go.Surface(x=x, y=y, z=z,
                             name=description["label"]["main"],
                             hovertemplate=description["hovertemplate"],
                             colorscale=colorscale,
                             opacity=opacity))
    if "title" in description:
        fig.update_layout(scene=dict(xaxis_title=description["title"]["x"],
                                     yaxis_title=description["title"]["y"],
                                     zaxis_title=description["title"]["z"]),
                          title=description["title"]["main"])
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


def continuous_chart(fig: Figure, iid_rvs: np.ndarray, pdf_rvs: np.ndarray) -> None:
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


def discrete_chart(fig: Figure, iid_rvs: np.ndarray, pdf_rvs: np.ndarray) -> None:
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


def get_pdf(iid_rvs: np.ndarray, pdf_rvs: np.ndarray, name: str, iscontinuous: bool = True) -> Figure:
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
