import streamlit as st
from SessionState import set_title
from distribution import which_distribution
from utils import chapters, chapters_acronyms, chapter2idx, getChapterIndexByURL, set_get_URL, urlIndex, setMetaTags

def main(state, isAuthenticated):
    # st.write(":floppy_disk:")
    idx: int = getChapterIndexByURL(state.url)  # if state.TOTAL_RELOADS==1 else state.url)
    option: str = st.selectbox("", chapters, index=idx)
    set_get_URL(ch=chapters_acronyms[chapter2idx(option)])

    if option != chapters[0] and \
       option != chapters[3] and \
       option != chapters[-2] and \
       option != chapters[-1]:
        distribution: str = st.sidebar.selectbox("Select Distribution", list(which_distribution.keys()), index=urlIndex(state.url))
    else:
        distribution = ""

    if option == chapters[0]:
        from gui.stats import stats
        set_title('Introduction | Visualization | Fundamentals of Statistics - QuantML')
        setMetaTags({
            "title": "Introduction | Visualization | Fundamentals of Statistics - QuantML",
            "url": "https://app.quantml.org/?ch=Introduction",
            "description": "Let's visually see what is statistics with an example, then estimate parameter, tweak some variables and see how it affects our estimation."
        })
        stats.main(state)
    if option == chapters[1]:
        from gui.lln import lln
        set_title('Weak Law of Large Numbers | Visualization | Fundamentals of Statistics - QuantML')
        setMetaTags({
            "title": "Weak Law of Large Numbers | Visualization | Fundamentals of Statistics - QuantML",
            "url": "https://app.quantml.org/?ch=Weak-Law-of-Large-Numbers&dist=Normal+distribution",
            "description": "Visualize Weak Law of Large Numbers | Statistics. See how changing parameters, affects convergence of sample average. Here you can learn Weak Law of Large Numbers by interacting with it."
        })
        lln.main(distribution, state)
    elif option == chapters[2]:
        from gui.clt import clt
        set_title('Central Limit Theorem | Visualization | Fundamentals of Statistics - QuantML')
        setMetaTags({
            "title": "Central Limit Theorem | Visualization | Fundamentals of Statistics - QuantML",
            "url": "https://app.quantml.org/?ch=Central-Limit-Theorem&dist=Normal+distribution",
            "description": "Visualize Central Limit Theorem | Statistics. See how changing parameters, affects convergence of distribution of sample average. Here you can learn Central Limit Theorem by interacting with it."
        })
        clt.main(distribution, state)
    elif option == chapters[3]:
        # from gui.gauss import gauss
        set_title('Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        setMetaTags({
            "title": "Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML",
            "url": "https://app.quantml.org/?ch=Gaussian-Distribution",
            "description": "Visualize Gaussian Distribution | Statistics. Here we can see simulation of Random Walk 1D, Random Walk 2D and Multiple Die Rolls. And see how they results in Gaussian Distribution."
        })
        # gauss.main(state)
        concluded = True
        if concluded:
            if isAuthenticated:
                from gui.gauss import gauss
                gauss.main(state)  # RUN ...
            else:
                from gui.gauss import gauss_unauthorized
                gauss_unauthorized.main(state)  # Do not Run ___
        else:
            from gui.gauss import gauss_comming_soon
            gauss_comming_soon.main(isAuthenticated)

    elif option == chapters[4]:
        from gui.coming_soon import coming_soon
        set_title('Coming Soon | Visualization | Fundamentals of Statistics - QuantML')
        coming_soon.main(state, isAuthenticated)

    elif option == chapters[-1]:
        import gui.about as about
        set_title('About | Statistics App | Fundamentals of Statistics | Visualization - QuantML')
        about.main(state)
