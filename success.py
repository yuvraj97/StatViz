import streamlit as st
from SessionState import set_title
from distribution import which_distribution
from utils import chapters, chapters_acronyms, chapter2idx, getChapterIndexByURL, set_get_URL, urlIndex


def main(state):
    # st.write(":floppy_disk:")
    idx: int = getChapterIndexByURL(state.url)  # if state.TOTAL_RELOADS==1 else state.url)
    option: str = st.selectbox("", chapters, index=idx)
    set_get_URL(ch=chapters_acronyms[chapter2idx(option)])

    if option != chapters[0] and \
       option != chapters[3] and \
       option != chapters[-1]:
        distribution: str = st.sidebar.selectbox("Select Distribution", list(which_distribution.keys()), index=urlIndex(state.url))
    else:
        distribution = ""

    if option == chapters[0]:
        from gui.stats import stats
        set_title('Introduction | Visualization | Fundamentals of Statistics - QuantML')
        stats.main(state)
    if option == chapters[1]:
        from gui.lln import lln
        set_title('Weak Law of Large Numbers | Visualization | Fundamentals of Statistics - QuantML')
        lln.main(distribution, state)
    elif option == chapters[2]:
        from gui.clt import clt
        set_title('Central Limit Theorem | Visualization | Fundamentals of Statistics - QuantML')
        clt.main(distribution, state)
    elif option == chapters[3]:
        from gui.gauss import gauss
        set_title('Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        gauss.main(state)
    elif option == chapters[4]:
        from gui.coming_soon import coming_soon
        set_title('Coming Soon | Visualization | Fundamentals of Statistics - QuantML')
        coming_soon.main()
