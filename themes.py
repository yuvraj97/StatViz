import streamlit as st
def applyDarkTheme():
    st.markdown("""
    <style>
        .css-1v4eu6x a{
            color: rgba(255, 180, 100, 1);
        }
        .css-1v4eu6x a:hover{
            color: rgba(255, 180, 100, 0.8);
        }
        
        div[role=listbox]{
            box-shadow: .05rem .05rem 0.4rem 0rem rgb(255, 255, 255, 0.5);
        }
        div[role=listbox], 
        div[role=listbox] *{
            background-color:rgb(45, 45, 45);
            color: rgb(231, 232, 235);
        }

        .css-9eqr5v {
            background-color: transparent
        }
        .css-9eqr5v:hover {
            background-color: rgb(25, 25, 25)
        }
        
        .css-9eqr5v *{
            color: rgb(231, 232, 235);
        }
        /* Sidebar styling */
        .css-1aumxhk{
            background-color: rgb(45, 45, 45);
            background-image: none;
            color: rgb(231, 232, 235);
        }

        /*close sidebar*/
        .css-1iqkxsh, .css-1obttss, .css-xq1lnh-EmotionIconBase{
            color: rgb(231, 232, 235);
        }

        .stSlider > div  > div > div {
            background: none;
            background-color: rgb(25, 25, 25);
        }
        .stSlider > div  > div > div > div {
            background-color: rgb(255, 160, 102)
        }
        .css-1t42vg8 {
            background-color: transparent !important;
        }
        .css-a8dgif {
            color: rgb(231, 232, 235);
        }

        .stDataFrame {
            border: rgb(45, 45, 45);
        }
        .css-10r44n0, .css-1b32pqr {
            background: rgb(25, 25, 25);
        }
        .css-x0vgxp, .plot-container.plotly > div > svg:first-child {
            background: rgb(45, 45, 45) !important;
        }
        .g-xtitle > text, .g-ytitle > text, .g-gtitle > text{
            fill: aliceblue !important;

        }
        g.xtick > text, g.ytick > text {
            fill: rgb(231, 232, 235) !important; 
        }

        /*Expander*/
        .streamlit-expander * {
            color: rgb(231, 232, 235);
        }
        .streamlit-expanderHeader,
        .streamlit-expanderContent{
            border-bottom-color: rgb(150, 150, 150);
        }
        .streamlit-expanderHeader:hover svg{
            fill: rgb(255, 180, 100) !important;
        }
        .streamlit-expanderHeader:hover{
            color: rgb(255, 180, 100) !important;
            border-bottom-color: rgb(255, 180, 100) !important;
        }
        
        .row-widget.stSelectbox > div > div,
        .stNumberInput > div > div > div,
        .stNumberInput > div > div > div > input,
        .row-widget.stTextInput > div > div,
        .row-widget.stTextInput > div > div > input {
            background-color: rgb(25, 25, 25);
            border-color: rgb(25, 25, 25);
            color: rgb(231, 232, 235);
        }

        /*
        .row-widget.stSelectbox > div > div:focus,
        .stNumberInput > div > div > div:focus,
        .stNumberInput > div > div > div > input:focus,
        .row-widget.stTextInput > div > div:focus,
        .row-widget.stTextInput > div > div > input:focus {
            border-color: red;
        }
        */

        .stNumberInput > div > div > button *{
            color: rgb(25, 25, 25);
        }

        .stNumberInput > div > div > button {
            background-color: rgb(231, 232, 235)
        }

        .stNumberInput > div > div > button:hover {
            background-color: rgb(255, 180, 100)
        }

        .row-widget.stCheckbox > label{
            background-color: rgb(45, 45, 45);
        }

        .row-widget.stSelectbox *,
        .row-widget.stTextInput *,
        .stNumberInput *,
        .row-widget.stCheckbox *{
            color: rgb(231, 232, 235);
            
        }

        .stAlert > div{
            background-color: rgba(250, 202, 43, 0.1 );
        }
        .stAlert *{
            color:rgb(255, 200, 142);
        }

        /*Body styling*/
        .css-1v3fvcr{
            background-color: rgb(45, 45, 45);
            background-image: none;
            color: rgb(231, 232, 235);
        }

        /*button*/
        /*.css-1ch8ttb {
            background-color: rgb(200, 200, 200);
        }
        .css-1ch8ttb:hover {
            background-color: rgb(231, 232, 235);
            color: black
        }*/

        

        /*Text Color*/
        /*body,
        .css-145kmo2,
        .streamlit-expander,
        .streamlit-expanderHeader{
            color: rgb(231, 232, 235);
        }*/

        blockquote {
            border-left: solid 4px;
            margin: 10px 0 10px 0;
            padding: 1rem 2rem 0.1rem 2rem;
            background-color:#1C1B1B;
            border-left-color: rgb(207, 210, 214);
            border-radius: 10px;
        }

        /*slider*/
        /*.st-e4{
            background: linear-gradient(to right, rgb(255, 180, 100) 0%, rgb(255, 180, 100) 44.4444%, rgb(230, 234, 241) 44.4444%, rgb(230, 234, 241) 100%);
            background-image: linear-gradient(to right, rgb(255, 180, 100) 0%, rgb(255, 180, 100) 44.4444%, rgb(230, 234, 241) 44.4444%, rgb(230, 234, 241) 100%);
        }*/
        
        /* slider dot */
        /*.st-eg,{
            background-color: rgb(255, 180, 100)
        }*/

        /*.st-cw{
            background-color: rgb(25, 25, 25);
            border-color: rgb(25, 25, 25);
        }*/
        
    </style>
    
    """, unsafe_allow_html=True)