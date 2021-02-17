import streamlit as st
# from auth.utils import send_email
from utils import set_get_URL

def main(state, isAuthenticated):
    set_get_URL(parameters={
        "dist" : "remove",
        "topic": "remove"
    })
    st.markdown("""
    <blockquote class="info">
        You should expect new concept <b>visualization</b> (and chapter for our
        <a rel='noreferrer' target='_blank' href="https://read.quantml.org/statistics/">Statistics Guide</a>
        ) <b>every other week</b>.
    </blockquote>
    """, unsafe_allow_html=True)

    if not isAuthenticated:
        st.markdown("""
            <blockquote class="warning">
            This app is under development so currently <a rel='noreferrer' target='_blank' href="https://www.patreon.com/quantml">patreons</a>
            that opt for Statistics App, are able to access all upcoming visualizations.<br>
            Once this Statistics App is concluded plan is to make all visualizations of this Statistics App to be available
            to everyone.<br>
        </blockquote>
        """, unsafe_allow_html=True)

    st.markdown("""
    ## Concepts that are planned to be covered:    
    
    - Confidence Intervals
    - Hypothesis Testing
    - Type 1 and Type 2 errors
    - p-value
    - Maximum Likelihood Estimation
    - TV distance
    - KL-Divergence
    - Fisher Information 
    - M-Estimation
    - Chi Squared Distribution
    - T-Test
    - Wald's Test
    - Likelihood Ratio Test
    - Goodness of Fit Test
    - Kolmogorov-Smirnov test
    - Kolmogorov-Lilliefors test
    - Quantile-Quantile Plots
    - Linear/Ridge Regression""" +
                # - [etc.]
                #
                # These are the concepts for which I am confident that I can simulate/visualize these concepts.
                #
                # ## Below are the concepts I wish to include/visualize
                # For following concepts am not much confident that I can make visualization that will
                # aid you much in understanding the concept.
                # (But am also considerate enough that in future following concepts can be included.)
                #
    """
    - Covariance Matrices
    - Multivariate Statistics
    - Multivariate Gaussian
    - Asymptotic Normality of MLE
    - Method of Moments
    - Bayesian Statistics
    - Jeffreys Prior
    - Bayesian Confidence Interval
    - Multinomial Bayesian Estimation,
    - GLM: Link Functions and the Canonical Link Function
    - [etc.]
    """)

    # if isAuthenticated:
    #     st.markdown("""
    #     <blockquote class="info">
    #     If there is something you want to have visualization for in the realm of <b>Statistics</b>
    #     tell below.
    #     </blockquote>""", unsafe_allow_html=True)
    #     feature_request = st.text_area("Feature Request")
    #     if st.button("Send Request"):
    #         if feature_request == "":
    #             st.markdown("""
    #             <blockquote class="error">
    #                 There's nothing in Feature Request!
    #             </blockquote>
    #             """, unsafe_allow_html=True)
    #         else:
    #             response = send_email(None,
    #                                   f"Feature Request from {state.email}",
    #                                   f"Feature Request from {state.email}\n\n" + feature_request)
    #             if response == {}:
    #                 # st.balloons()
    #                 st.markdown("""
    #                 <blockquote class="success">
    #                     Feature Request sent successfully.
    #                 </blockquote>
    #                 """, unsafe_allow_html=True)