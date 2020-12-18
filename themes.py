import streamlit as st
def applyDarkTheme():
    st.markdown("""
    <style>
        /*
        .row-widget.stSelectbox > div > div:focus,
        .stNumberInput > div > div > div:focus,
        .stNumberInput > div > div > div > input:focus,
        .row-widget.stTextInput > div > div:focus,
        .row-widget.stTextInput > div > div > input:focus {
            border-color: red;
        }
        */

        /*top bar*/
        .css-158te0l {
            background-image: linear-gradient(90deg, rgb(0, 115, 177), rgb(255, 253, 128))
        }

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
        .stSlider *{
            color: rgb(231, 232, 235);
        }
        .css-1t42vg8 {
            background-color: transparent !important;
        }
        .css-a8dgif {
            /*margin-bottom: 0.533333rem;
            padding-bottom: 0%;
            border-radius: 5px;
            background-color: rgb(25, 25, 25);*/
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

        .row-widget.stTextInput > div > div > input:hover,
        .row-widget.stTextInput > div > div > input:focus{
            color: rgba(255, 180, 100, 1);
        }

        .stNumberInput > div > div > div > input:hover,
        .stNumberInput > div > div > div > input:focus {
            color: rgba(255, 180, 100, 1);
        }

        .stNumberInput > div > div > button *{
            color: rgb(25, 25, 25);
        }

        .stNumberInput > div > div > button {
            background-color: rgb(231, 232, 235, 0.8)
        }

        .stNumberInput > div > div > button:hover {
            background-color: rgb(231, 232, 235)
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

def mainStyle():
    st.markdown("""
        <style>
        .css-1aumxhk {
            padding: 0em 0em;
            /*width: 100%;*/
        }
        .streamlit-expanderContent{
            margin-bottom: 30px;
        }
        .css-hx4lkt{
            padding: 2rem 1rem 3rem;
        }
        /*rgb(230, 234, 241)*/
        .streamlit-expanderHeader{
            border-block-color:rgb(210, 210, 210);
        }
        .streamlit-expanderHeader:hover{
            border-block-color:#0073b1;
        }
        .streamlit-expanderContent{
            border-block-color:rgb(210, 210, 210);
        }
        blockquote {
            border-left: solid 4px;
            margin: 10px 0 10px 0;
            padding: 1rem 2rem 0.1rem 2rem;
            background-color:#ECF1F6;
            border-left-color: #467AAC;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )