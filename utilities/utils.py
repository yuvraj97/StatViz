from typing import List
import streamlit as st
from utilities.distribution import distributions_properties

chapters: List[str] = [
    "Introduction",
    "Law of Large Number",
    "Central Limit Theorem",
    "Gaussian Distribution",
    "Coming Soon",
    "About"
]

chapters_acronyms: List[str] = [
    "Introduction",
    "Weak-Law-of-Large-Numbers",
    "Central-Limit-Theorem",
    "Gaussian-Distribution",
    "Coming-Soon",
    "About"
]

chapters_acronyms_lowercase: List[str] = [e.lower() for e in chapters_acronyms]


def getChapterIndexByURL(url: dict) -> int:
    if "ch" not in url or url["ch"][0].lower() not in chapters_acronyms_lowercase: return 0
    return chapters_acronyms_lowercase.index(url["ch"][0].lower())


def set_get_URL(ch: str = None,
                url: dict = None,
                parameters: dict = {}) -> dict:
    url = st.experimental_get_query_params() if url is None else url
    d: dict = {}
    if "ch" in url: d["ch"] = url["ch"][0]
    if ch is not None: d["ch"] = ch
    if "dist" in parameters and parameters["dist"] == "remove":
        del parameters["dist"]
    elif "dist" in url:
        d["dist"] = url["dist"][0]
    if "topic" in parameters and parameters["topic"] == "remove":
        del parameters["topic"]
    elif "topic" in url:
        d["topic"] = url["topic"][0]
    for k in parameters.keys():
        d[k] = parameters[k]
    st.experimental_set_query_params(**d)
    url = st.experimental_get_query_params()
    return url


def urlIndex(url: dict) -> int:
    if "dist" not in url:
        return 0
    dist_name = url["dist"][0]
    idx = 0
    for dist in distributions_properties:
        if distributions_properties[dist]["name"] == dist_name:
            idx = distributions_properties[dist]["idx"]
            break
    return idx


def setMetaTags(meta_data):
    import streamlit.components.v1 as components
    image_meta_data = ""
    if "image-url" in meta_data:
        image_meta_data = f"""
        var meta = parent.document.getElementById("og-image");
        meta.setAttribute("property", "og:image");
        meta.content = "{meta_data["image-url"]}";
        
        var meta = parent.document.getElementById("twitter-image");
        meta.setAttribute("property", "twitter:image");
        meta.content = "{meta_data["image-url"]}";
        """
    components.html(f"""
    <script>
        var meta = parent.document.getElementById("description");
        meta.name = "description";
        meta.content = "{meta_data["description"]}";
        
        var meta = parent.document.getElementById("og-type");
        meta.setAttribute("property", "og:type");
        meta.content = "website";
        
        var meta = parent.document.getElementById("og-url");
        meta.setAttribute("property", "og:url");
        meta.content = "{meta_data["url"]}";
        
        var meta = parent.document.getElementById("og-title");
        meta.setAttribute("property", "og:title");
        meta.content = "{meta_data["title"]}";
        
        var meta = parent.document.getElementById("og-description");
        meta.setAttribute("property", "og:description");
        meta.content = "{meta_data["description"]}";
        
        var meta = parent.document.getElementById("twitter-card");
        meta.setAttribute("property", "twitter:card");
        meta.content = "summary_large_image";
        
        var meta = parent.document.getElementById("twitter-url");
        meta.setAttribute("property", "twitter:url");
        meta.content = "{meta_data["url"]}";
        
        var meta = parent.document.getElementById("twitter-title");
        meta.setAttribute("property", "twitter:title");
        meta.content = "{meta_data["title"]}";
        
        var meta = parent.document.getElementById("twitter-description");
        meta.setAttribute("property", "twitter:description");
        meta.content = "{meta_data["description"]}";
        
        {image_meta_data}
        </script>
    """, height=0, width=0)


def rename_inputs(inputs: dict):
    if "n" in inputs:
        inputs = inputs.copy()
        if "population" in inputs["n"]:
            inputs["n_population"] = inputs["n"]["population"]
        if "samples" in inputs["n"]:
            inputs["n_sample"] = inputs["n"]["samples"]
        if "simulations" in inputs["n"]:
            inputs["n_simulation"] = inputs["n"]["simulations"]

    return inputs


def check_input_limits(inputs):

    inputs = rename_inputs(inputs)
    
    if "seed" in inputs and (inputs["seed"] is not None and inputs["seed"] < -1):
        st.error(f"Seed Can't be less then $-1$")
        return
    if "n_population" in inputs and (
            inputs["n_population"] < 100 or
            inputs["n_population"] > 400):
        st.error(f"Population size should be in between $100$ and $400$")
        return

    if "n_sample" in inputs and (
            inputs["n_sample"] < 10 or
            inputs["n_sample"] > 50):
        st.error(f"Sample size should be in between $10$ and $50$")
        return

    if "n_simulation" in inputs and (
            inputs["n_simulation"] < 10 or
            inputs["n_simulation"] > 50):
        st.error(f"Simulation size should be in between $10$ and $50$")
        return

    if "p" in inputs and (
            inputs["p"] <= 0.0 or
            inputs["p"] >= 1.0):
        st.error(f"Probability should be in between $0.0$ and $1.0$")
        return

    return True
