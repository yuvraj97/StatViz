from gui.stats import stats
from gui.lln import lln
from gui.clt import clt
from utils import chapters, chapters_acronyms, chapter2idx, getChapterIndexByURL, set_get_URL
import streamlit as st
from SessionState import set_title


def clear(elements):
    # print("      clear(elements)")
    for element in elements:
        element.empty()


def main(elements, email, state, GlobalElements):
    # print("    ======== success.py [START] ========")
    # print("    ARGUMENTS: elemants, email=" + email + ", state, GlobalElements")
    clear(elements)
    # stwrite(":floppy_disk:")
    idx = getChapterIndexByURL(state.url)  # if state.TOTAL_RELOADS==1 else state.url)
    option = st.selectbox("", chapters, index=idx)
    url = set_get_URL(ch=chapters_acronyms[chapter2idx(option)])

    # print("          * idx: ",idx)
    # print("          * option: ",option)
    # print("          * url: ",url)

    # if(option==chapters[0]):
    #    stats.main(state, GlobalElements)
    #    set_get_URL(dist = "remove")
    if (option == chapters[0]):
        set_title('Weak Law of Large Numbers | Visualization | Statistics - QuantML')
        lln.main(state, GlobalElements)
    elif (option == chapters[1]):
        set_title('Central Limit Theorem | Visualization | Statistics - QuantML')
        clt.main()

        # print("    ======== success.py  [END]  ========")
