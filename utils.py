from typing import List
import streamlit as st
from distribution import distributions_properties, distribution2idx

chapters: List[str] = [
    "Introduction",
    "Law of Large Number",
    "Central Limit Theorem (patreon)",
]


def chapter2idx(chapter: str) -> int:
    # print("        - chapter2idx("+ chapter +")")
    return chapters.index(chapter)


chapters_acronyms: List[str] = [
    "Introduction",
    "LLN",
    "CLT",
]

chapters_acronyms_lowercase: List[str] = [e.lower() for e in chapters_acronyms]


def getChapterByURL(url: dict) -> str:
    # print("        - getChapterByURL("+ str(url) +")")
    if "ch" in url and url["ch"][0].lower() in chapters_acronyms_lowercase:
        chapter = url["ch"][0].lower()
    else:
        chapter = None
    # print("            * chapter: ", chapter)
    return chapter


def getChapterIndexByURL(url: dict) -> int:
    # print("        - getChapterIndexByURL("+ str(url) +")")
    chapter_acronym = getChapterByURL(url)
    idx = chapters_acronyms_lowercase.index(chapter_acronym) if chapter_acronym is not None else 0
    # print("            * chapter_acronym: ", chapter_acronym)
    # print("            * idx: ", idx)
    return idx


def set_get_URL(ch: str = None, dist: str = None, url: dict = None) -> dict:
    # print("        - set_get_URL(url="+ str(url) + ", ch=" + str(ch) + ", dist=" + str(dist) +")")
    url = st.experimental_get_query_params() if url is None else url
    _ch, _dist = "", ""
    add_dist = False
    if dist is not None or "dist" in url: add_dist = True
    if "ch" in url: _ch = url["ch"][0]
    if "dist" in url: _dist = url["dist"][0]
    if ch is not None: _ch = ch
    if dist is not None: _dist = dist
    if add_dist and dist != "remove":
        st.experimental_set_query_params(ch=_ch, dist=_dist)
    else:
        st.experimental_set_query_params(ch=_ch)
    url = st.experimental_get_query_params()
    # print("            * ch: ", ch)
    # print("            * dist: ", dist)
    # print("            * url: ", url)
    return url

def urlIndex(url: dict) -> int:
    if "dist" not in url:
        return 0
    dist_name = url["dist"][0]
    idx = 0
    for dist in distributions_properties.keys():
        if distributions_properties[dist]["name"] == dist_name:
            idx = distribution2idx[dist]
            break
    return idx
