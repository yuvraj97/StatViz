import traceback

import streamlit as st

# NEED TO BE CHANGE
# NEED TO BE CHANGE
# NEED TO BE CHANGE
# NEED TO BE CHANGE
# NEED TO BE CHANGE


def main():
    """
    We will never use it in production it will came handy in development
    :return: None
    """

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

    st.sidebar.write("-----")
    chapter: str = st.selectbox("Choose Chapter", chapters, index=prev_idx)
    chosen_idx = chapters.index(chapter)
    if prev_idx != chosen_idx:
        st.session_state["chapter"] = chosen_idx
        st.experimental_rerun()
    st.experimental_set_query_params(**{"chapter": chapter})

    chapter = chapters[prev_idx]
    exec(f"from Chapters.{chapter.replace(' ', '_')}.run import main;main()")


if __name__ == '__main__':

    try:
        main()
    except Exception as e:
        traceback.print_exc()
        st.error("Something went wrong!")
