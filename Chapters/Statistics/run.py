import streamlit as st


def main():
    st.markdown("""
    # Statistics Concepts Visualization
    
    Here you can see **visualization** of some **Statistical Concepts**.  
    You can also **interact** with those **statistical concepts** and get a better understanding of the concept.
    
    -----
    """)

    st.markdown("""
    ## Table of Content
    [$1.$ **Introduction:**](https://app.quantml.org/statistics/introduction/)  
    
    [$2.$ **Law of Large Number:**](https://app.quantml.org/statistics/law-of-large-number/)  
    
    [$3.$ **Central Limit Theorem**](https://app.quantml.org/statistics/central-limit-theorem/)  
    
    [$4.$ **Gaussian Distribution**](https://app.quantml.org/statistics/gaussian-distribution/)  
      - [**Random Walk 2D**](https://app.quantml.org/statistics/gaussian-distribution/?topic=Random+Walk+1D)  
      - [**Random Walk 3D**](https://app.quantml.org/statistics/gaussian-distribution/?topic=Random+Walk+2D)  
    """)

    st.write("")
    st.write("")

    st.warning("""
    This app is on hold for time being, at-least till **November 2021**.
    """)

    st.markdown("""
    ## Concepts planned to be covered:
            
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
