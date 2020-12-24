from utils import chapters, chapters_acronyms, chapter2idx, getChapterIndexByURL, set_get_URL
import streamlit as st
from SessionState import set_title

def clear(elements):
    # print("      clear(elements)")
    for element in elements:
        element.empty()


def main(elements, state):
    # print("    ======== success.py [START] ========")
    # print("    ARGUMENTS: elements, email=" + email + ", state")
    clear(elements)
    # st.write(":floppy_disk:")
    idx: int = getChapterIndexByURL(state.url)  # if state.TOTAL_RELOADS==1 else state.url)
    option: str = st.selectbox("", chapters, index=idx)
    set_get_URL(ch=chapters_acronyms[chapter2idx(option)])

    # print("          * idx: ",idx)
    # print("          * option: ",option)
    # print("          * url: ",url)

    if(option==chapters[0]):
        from gui.stats import stats
        set_title('Introduction | Visualization | Fundamentals of Statistics - QuantML')
        stats.main(state)
    if option == chapters[1]:
        from gui.lln import lln
        set_title('Weak Law of Large Numbers | Visualization | Fundamentals of Statistics - QuantML')
        lln.main(state)
    elif option == chapters[2]:
        from gui.clt import clt
        set_title('Central Limit Theorem | Visualization | Fundamentals of Statistics - QuantML')
        clt.main(state)

        # print("    ======== success.py  [END]  ========")
