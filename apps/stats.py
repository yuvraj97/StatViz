import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from auth.stInputs import stSlider, stNumberInput, stEmpty

def get_sample_with_true_p(population,p):
    a=[0]*population
    _1_s = int(population*p)
    for i in range(0,_1_s):
        a[i]=1
    np.random.shuffle(a)
    return a

def simulate(n_population, n_sample, true_p, n_simulation):
    population_sample = get_sample_with_true_p(n_population, true_p)
    estimators = []
    for i in range(0,n_simulation):
        # Here we randomly select 124 couples out of 5000
        sample = np.random.choice(population_sample,n_sample)
        estimators.append(sum(sample)/n_sample)
    fig = plt.figure()
    ax = fig.gca()
    ax.hist(estimators, histtype='bar', rwidth=0.95)
    #ax.set_xlim(0,1)
    ax.set_xlabel("Proportion of people turning their head to right (p)")
    ax.set_ylabel("# occurence of certain (p) in our simulation")
    return fig, sum(estimators)/ n_simulation, estimators

def main(state, GlobalElements):
    e_population = stEmpty(sidebar=True)
    e_sample = stEmpty(sidebar=True)
    e_true_p = stEmpty(sidebar=True)
    e_simulation = stEmpty(sidebar=True)
    GlobalElements.extend([e_population, e_sample, e_true_p, e_simulation])

    n_population = e_population.number_input("Enter population size (Total Population)", min_value=100, max_value=5000, value=3000)
    n_sample = e_sample.number_input("Enter sample size (# couples observed)", min_value=10, max_value=200, value=124)
    true_p = e_true_p.slider("Enter proportion of people turning their head to right (p)", min_value=0.0, max_value=1.0, value=0.35, step=0.05)
    n_simulation = e_simulation.number_input("Enter number of simulation", min_value=10, max_value=200, value=50)
    
    fig, estimate, estimators = simulate(n_population, n_sample, true_p, n_simulation)
    estimate = "{:.4f}".format(estimate)

    tex = []
    for i in range(5):
        t = "$\widehat{p}$ = " + f"**{int(estimators[i]*n_sample)}/{n_sample} = "+"{:.4f}".format(estimators[i])+"**"
        tex.append(t)

    e_plot = stEmpty()
    GlobalElements.append(e_plot)
    e_plot.pyplot(fig)

    image_path = os.path.join(os.getcwd(), "img","dogma.png")
    image = Image.open(image_path)
    e_img = stEmpty()
    GlobalElements.append(e_img)
    e_img.image(image, use_column_width=True)

    e_markdown = stEmpty()
    GlobalElements.append(e_markdown)
    e_markdown.markdown(f"""
    [Remember the Central Dogma of Probability and Statistics](https://read.quantml.org/stats/#dogma)
    ## Truth    
    Here the **truth** is, "proportion of people turning their head to the right = **{true_p}**"    
    ## Probability    
    **Probability** tell us what our data look like, so we know that **p = {true_p}**
    so using this probability we generate(synthatic) data.   
    ### Data    
    Here we specify,    
    - A population of **{n_population}** kissing couples.   
    - Out of **{n_population}** kissing couples we observe **{n_sample}** couples and record where they turn there head.   
    - We repeat this experiment **{n_simulation}** times.   
    ## Statistics    
    **Statistics** gives us an estimate of true "proportion" (that we set to **{true_p}**).    
    Here we don't know what the real proportion is we just have a data of **{n_simulation}** experiments
    with **{n_sample}** data points each.    
    We use Statistics to estimate the true proportion (of all **{n_population}** couples),
    in this case we just see how many couples turn there head to the right,
    and divide by total number of couples observed.    

    ### Observation     
    We have data for **{n_simulation}** experiments, lets see the data for first 3 experiments.      
    #### Experiment 1: 
    *   In first experiment out of **{n_sample}**.  **{int(estimators[0]*n_sample)}** couples turn there head to right.    
        So estimate for first experiment is {tex[0]}    
    #### Experiment 2: 
    *   In second experiment out of **{n_sample}**.  **{int(estimators[1]*n_sample)}** couples turn there head to right.    
        So estimate for first experiment is {tex[1]}    
    #### Experiment 3: 
    *   In first experiment out of **{n_sample}**.  **{int(estimators[2]*n_sample)}** couples turn there head to right.    
        So estimate for first experiment is {tex[2]}    
    

    .    
    .    
    .



    """)
    e_success = stEmpty()
    GlobalElements.append(e_success)
    e_success.success("Here our estimate is $\\bf{\widehat{p} = "+ estimate +"}$")
