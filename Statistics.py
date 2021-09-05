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
    # st.set_page_config(
    #     layout='centered',
    #     initial_sidebar_state='expanded'
    # )
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

    st.sidebar.write("-----")
    st.sidebar.write("""
    If you like this project, <br> then give it a ⭐ on [GitHub](https://github.com/yuvraj97/apps)
    <iframe 
        src="https://ghbtns.com/github-btn.html?user=yuvraj97&repo=apps&type=star&count=true&size=large" 
        frameborder="0" scrolling="0" width="170" height="30" title="GitHub">
    </iframe>""", unsafe_allow_html=True)

    st.sidebar.markdown("## Connect")
    st.sidebar.write("""
    <iframe 
        src="https://ghbtns.com/github-btn.html?user=yuvraj97&type=follow&count=true&size=large" 
        frameborder="0" scrolling="0" width="250" height="30" title="GitHub">
    </iframe>""", unsafe_allow_html=True)
    st.sidebar.markdown("""
    [Donate Here if you like this project](http://www.quantml.org/donate)    
    LinkedIn: [yuvraj97](https://www.linkedin.com/in/yuvraj97/)    
    Github: [yuvraj97](https://github.com/yuvraj97/)    
    Email: [yuvraj@quantml.org](mailto:yuvraj@quantml.org)
    """, unsafe_allow_html=True)
