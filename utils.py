import streamlit as st

chapters = [
    "Introduction",
    "Law of Large Number",
    "Central Limit Theorem (patreon)",
]


def chapter2idx(chapter):
    # print("        - chapter2idx("+ chapter +")")
    return chapters.index(chapter)


chapters_acronyms = [
    "Introduction",
    "LLN",
    "CLT",
]

chapters_acronyms_lowercase = [e.lower() for e in chapters_acronyms]


def getChapterByURL(url):
    # print("        - getChapterByURL("+ str(url) +")")
    if "ch" in url and url["ch"][0].lower() in chapters_acronyms_lowercase:
        chapter = url["ch"][0].lower()
    else:
        chapter = None
    # print("            * chapter: ", chapter)
    return chapter


def getChapterIndexByURL(url):
    # print("        - getChapterIndexByURL("+ str(url) +")")
    chapter_acronym = getChapterByURL(url)
    idx = chapters_acronyms_lowercase.index(chapter_acronym) if chapter_acronym is not None else 0
    # print("            * chapter_acronym: ", chapter_acronym)
    # print("            * idx: ", idx)
    return idx


def set_get_URL(ch=None, dist=None, url=None):
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
