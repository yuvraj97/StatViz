import streamlit as st

from SessionState import set_title
from logic.gauss import gauss
from utils import set_get_URL
from gui.gauss import random_walk_1D, random_walk_2D, multiple_die_rolls

def main(state):
    option: str = st.sidebar.selectbox("Topic", gauss.topics, index=0)
    set_get_URL(dist="remove", parameters={
        "topic": option
    })
    if option == gauss.topics[0]:
        set_title('Random walk 1D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_1D.run()
    if option == gauss.topics[1]:
        set_title('Random walk 2D | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        random_walk_2D.run()
    if option == gauss.topics[2]:
        set_title('Multiple Die Rolls | Gaussian Distribution | Visualization | Fundamentals of Statistics - QuantML')
        multiple_die_rolls.run()
