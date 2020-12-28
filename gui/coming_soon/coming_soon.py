import streamlit as st
from auth.utils import send_email
def main(state):
    st.markdown("""
    <blockquote class="info">
        You should expect new concept <b>visualization</b> (and chapter for our
        <a rel='noreferrer' target='_blank' href="https://read.quantml.org/stats/">Statistics Guide</a>
        ) <b>every week</b>.
    </blockquote>
    """, unsafe_allow_html=True)
    st.markdown("""
    ## Concepts I plan to cover    
    (incomplete list)
    
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
    - Linear/Ridge Regression
    - [Don't know what future holds]
    
    These are the concepts for which I am confident that I can simulate/visualize these concepts.     
        
    ## Below are the concepts I wise to include/visualize     
    But am not much confident that I can make visualization that will aid you much in understanding the concept.     
    (but am also confident as time passes items from below list will move into the list above)     
    
    - Covariance Matrices
    - Multivariate Statistics
    - Multivariate Gaussian
    - Asymptotic Normality of MLE
    - Method of Moments
    - Bayesian Statistics
    - Jeffreys Prior(unlikely)
    - Bayesian Confidence Interval
    - Multinomial Bayesian Estimation,
    - GLM: Link Functions and the Canonical Link Function
    - [Don't know what future holds]
    """)

    if(state.isLoggedIn):
        st.markdown("""
        <blockquote class="info">
        If there is something you want to have visualization for in the realm of <b>Statistics</b>
        tell below.
        </blockquote>""", unsafe_allow_html=True)
        feature_request = st.text_area("Feature Request")
        if st.button("Send Request"):
            if feature_request == "":
                st.markdown("""
                <blockquote class="error">
                    There's nothing in Feature Request!
                </blockquote>
                """, unsafe_allow_html=True)
            else:
                response = send_email(None,
                                      f"Feature Request from {state.email}",
                                      f"Feature Request from {state.email}\n\n" + feature_request)
                if response == {}:
                    st.balloons()
                    st.markdown("""
                    <blockquote class="success">
                        Feature Request sent successfully.
                    </blockquote>
                    """, unsafe_allow_html=True)