import streamlit as st
# from auth.utils import send_email
from utils.utils import set_get_URL


def main():
    set_get_URL(parameters={
        "dist": "remove",
        "topic": "remove"
    })

    st.markdown("""
    # Concepts that are planned to be covered:    
    
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
