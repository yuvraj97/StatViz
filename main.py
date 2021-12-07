import traceback
import streamlit as st
from utilities.ui import intialize, reset_session, footer


def main():
    """
    We will never use it in production it will came handy in development
    :return: None
    """

    intialize("Statistics Visualization")

    chapters = [
        "Table of Content",
        "Introduction",
        "Law of Large Number",
        "Central Limit Theorem",
        "Gaussian Distribution",
    ]

    if "chapter" in st.session_state:
        prev_idx = st.session_state["chapter"]
    else:
        params = st.experimental_get_query_params()
        prev_idx = chapters.index(params["chapter"][0]) if "chapter" in params else 0

    st_chapter, st_reset = st.columns([9, 1])

    if st_reset.button("🔄", help="Reset Variables (Necessary to reset Manually Increment Steps)"):
        reset_session()

    chapter: str = st_chapter.selectbox("Choose Chapter", chapters, index=prev_idx)
    chosen_idx = chapters.index(chapter)
    if prev_idx != chosen_idx:
        st.session_state["chapter"] = chosen_idx
        st.experimental_rerun()
    st.experimental_set_query_params(**{"chapter": chapter})

    chapter = chapters[prev_idx]
    exec(f"from Chapters.{chapter.replace(' ', '_')}.run import main;main()")
    footer()


if __name__ == '__main__':

    try:
        main()
    except Exception as e:
        traceback.print_exc()
        st.error("Something went wrong!")
