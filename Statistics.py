import streamlit as st
import SessionState
import success


def main():
    cover_img = st.sidebar.empty()
    state.experimental_rerun = False
    state.url = state.url if state.url is not None else st.experimental_get_query_params()
    state.isMobile = True if (SessionState.get_cookie("notDesktop") == "true") else False

    cover_img.markdown(f"""
    <br><br>
    <a rel='noreferrer' target='_blank' href="https://www.quantml.org/">
        <img src="https://cdn.quantml.org/img/cover.webp" alt="QuantML" width="100%">
    </a><br>""", unsafe_allow_html=True)

    success.main(state)


if __name__ == '__main__':
    st.set_page_config(
        layout='centered',
        initial_sidebar_state='expanded'
    )
    error = st.empty()
    state = SessionState.get_state()

    # noinspection PyBroadException
    # try:
    main()
    # except Exception:
    #     error.markdown("""
    #     Unexpected error occurred please **try refreshing page**.
    #     **"CTRL + R"** or **"F5"**
    #     """)
