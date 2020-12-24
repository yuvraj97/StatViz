import streamlit as st
def applyDarkTheme():
    st.markdown("""
    <style>
        /*Body styling*/
            .css-1v3fvcr{
                background-color: rgb(45, 45, 45);
                background-image: none;
                color: rgb(231, 232, 235);
            }
        
        /* setting white text color */
            .row-widget.stSelectbox *,
            .row-widget.stTextInput *,
            .stNumberInput *,
            .row-widget.stCheckbox * {
                color: rgb(231, 232, 235);
            }

        div[role=listbox]{
            box-shadow: .05rem .05rem 0.4rem 0rem rgb(255, 255, 255, 0.3);
        }
        div[role=listbox], 
        div[role=listbox] *{
            background-color:rgb(25, 25, 25);
            color: rgb(231, 232, 235);
        }
        
        /* options to select */
        div[role=listbox] > ul > div > div > li > span {
            background-color: transparent;
        }
        div[role=listbox] > ul > div > div > li:hover {
            background-color:rgb(45, 45, 45);
        }
        
        
        /*top bar*/
            .css-158te0l {
                background-image: linear-gradient(90deg, rgb(0, 115, 177), rgb(255, 253, 128))
            }

        /* anchor tags */
            .css-1v4eu6x a{
                color: rgba(255, 180, 100, 1);
            }
            .css-1v4eu6x a:hover{
                color: rgba(255, 180, 100, 0.8);
            }

        /* Expand Button [plots, tables, etc.] */
            .css-n6u23q, .css-9eqr5v {
                background-color: transparent
            }
            .css-n6u23q:hover, .css-9eqr5v:hover {
                background-color: rgb(25, 25, 25)
            }
            .css-n6u23q *, .css-9eqr5v * {
                color: rgb(231, 232, 235);
            }
        
        /* Sidebar styling */
            .css-1aumxhk{
                background-color: rgb(45, 45, 45);
                background-image: none;
                color: rgb(231, 232, 235);
            }

        /*close sidebar X */
            .css-1iqkxsh, .css-1obttss, .css-xq1lnh-EmotionIconBase{
                color: rgb(231, 232, 235);
            }
        
        /* st slider */
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
            /* slider min max labels */
                .css-1t42vg8 {
                    background-color: transparent !important;
                }
            /* slider current value labels */            
                .css-a8dgif {
                    /*margin-bottom: 0.533333rem;
                    padding-bottom: 0%;
                    border-radius: 5px;
                    background-color: rgb(25, 25, 25);*/
                    color: rgb(231, 232, 235);
                }

        /* stDataFrame [TABLES] */
            .stDataFrame {
                border: rgb(45, 45, 45);
            }
            /* stDataFrame top left box */
                .css-10r44n0, .css-1b32pqr {
                    background: rgb(25, 25, 25);
                }
        
        /* opened plot, image background  */
            .css-x0vgxp {
                background: rgb(45, 45, 45) !important;
            }
        /* plotly plots */
            .plot-container.plotly > div > svg:first-child {
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
        
        /*  BG and Colors */
            .row-widget.stSelectbox > div > div,
            .stNumberInput > div > div > div,
            .stNumberInput > div > div > div > input,
            .row-widget.stTextInput > div > div,
            .row-widget.stTextInput > div > div > input {
                background-color: rgb(25, 25, 25);
                border-color: rgb(25, 25, 25);
                color: rgb(231, 232, 235);
            }

        /* stTextInput text color  */
            .row-widget.stTextInput > div > div > input:hover,
            .row-widget.stTextInput > div > div > input:focus{
                color: rgba(255, 180, 100, 1);
            }

        /* stSelectbox */
            .row-widget.stSelectbox > div > div:hover,
            .row-widget.stSelectbox > div > div:focus {
                border-color: rgb(255, 180, 100, 0.5);
            }
        
        /* stNumberInput */
            /*.stNumberInput > div > div > div > input:hover,*/
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
            .stNumberInput > div > div > div:hover,
            .stNumberInput > div > div > div:active {
                border-top-color: rgb(255, 180, 100, 0.5);
                border-bottom-color: rgb(255, 180, 100, 0.5);
                border-left-color: rgb(255, 180, 100, 0.5);
            }

        /* stCheckbox */
            .row-widget.stCheckbox > label{
                background-color: rgb(45, 45, 45);
            }

        /* stAlert */        
            .stAlert > div{
                /*background-color: rgba(250, 202, 43, 0.1 );*/
                background-color: rgba(150, 206, 255, 0.05);
                border-color: rgb(150, 206, 255, 0.5);
            }
            .stAlert *{
                /*color:rgb(255, 200, 142);*/
                color:rgb(150, 206, 255);
            }

        /* st Button */
            .stButton > button {
                border-color: rgb(25, 25, 25);
                background-color: rgb(25, 25, 25);
            }
            .stButton > button:hover {
                border-color: rgb(255, 180, 100, 0.5);
                color: rgb(255, 180, 100, 1);
            }

        /* ================================================================ */
        /* ================================================================ */

        .l1 {    color: rgb(255, 150, 150);     }
        .l2 {    color: rgb(150, 206, 255);     }
        .l3 {    color: rgb(150, 255, 150);     }
        .l4 {    color: rgb(255, 255, 200);     }

        blockquote.info {
            border-top-color: rgba(150, 206, 255, 0.5);
            border-bottom-color: rgba(150, 206, 255, 0.5);
            border-left-color: rgba(150, 206, 255, 0.5);
            border-right-color: rgba(150, 206, 255, 0.5);
            color: rgb(150, 206, 255);
            background-color: rgba(150, 206, 255, 0.05);   
        }
        blockquote.info > b {
            color: rgb(150, 206, 255);            
        }
        
        blockquote.warning {
            border-top-color: rgba(255, 255, 200, 0.5);
            border-bottom-color: rgba(255, 255, 200, 0.5);
            border-left-color: rgba(255, 255, 200, 0.5);
            border-right-color: rgba(255, 255, 200, 0.5);
            color: rgb(255, 255, 200);
            background-color: rgba(255, 255, 200, 0.05);   
        }
        blockquote.warning > b {
            color: rgb(255, 255, 200);
        }
        
        blockquote.success {
            border-top-color: rgba(150, 255, 150, 0.5);
            border-bottom-color: rgba(150, 255, 150, 0.5);
            border-left-color: rgba(150, 255, 150, 0.5);
            border-right-color: rgba(150, 255, 150, 0.5);
            color: rgb(150, 255, 150);
            background-color: rgba(150, 255, 150, 0.05);   
        }
        blockquote.success > b {
            color: rgb(150, 255, 150);
        }
        
        blockquote.error {
            border-top-color: rgba(255, 150, 150, 0.5);
            border-bottom-color: rgba(255, 150, 150, 0.5);
            border-left-color: rgba(255, 150, 150, 0.5);
            border-right-color: rgba(255, 150, 150, 0.5);
            color: rgb(255, 150, 150);
            background-color: rgba(255, 150, 150, 0.05);   
        }
        blockquote.error > b {
            color: rgb(255, 150, 150);
        }
        .quant-bb{
            background-color: rgb(0, 0, 0, 0.07);
            border: 1px rgb(194, 199, 204) solid;
        }        
    </style>
    
    """, unsafe_allow_html=True)

def applyLightTheme():
    st.markdown("""
    <style>
        blockquote.info {
            border-top-color: rgba(0, 104, 201, 0.1);
            border-bottom-color: rgba(0, 104, 201, 0.1);
            border-left-color: rgba(0, 104, 201, 0.1);
            border-right-color: rgba(0, 104, 201, 0.1);
            color: rgb(30, 103, 119);
            background-color: rgba(0, 104, 201, 0.1);   
        }
        blockquote.warning {
            border-top-color: rgba(250, 202, 43, 0.8);
            border-bottom-color: rgba(250, 202, 43, 0.8);
            border-left-color: rgba(250, 202, 43, 0.8);
            border-right-color: rgba(250, 202, 43, 0.8);
            color: rgb(148, 124, 45);
            background-color: rgba(250, 202, 43, 0.2);   
        }
        blockquote.success {
            border-top-color: rgba(9, 171, 59, 0.2);
            border-bottom-color: rgba(9, 171, 59, 0.2);
            border-left-color: rgba(9, 171, 59, 0.2);
            border-right-color: rgba(9, 171, 59, 0.2);
            color: rgb(23, 108, 54);
            background-color: rgba(9, 171, 59, 0.2);   
        }
        blockquote.error {
            border-top-color: rgba(255, 43, 43, 0.2);
            border-bottom-color: rgba(255, 43, 43, 0.2);
            border-left-color: rgba(255, 43, 43, 0.2);
            border-right-color: rgba(255, 43, 43, 0.2);
            color: rgb(157, 41, 45);
            background-color: rgba(255, 43, 43, 0.2);   
        }
        .quant-bb{
            background-color: #f6f8fa;
            border: 1px rgb(160, 160, 160) solid;
        }
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
        /*blockquote {
            border-left: solid 4px;
            margin: 10px 0 10px 0;
            padding: 1rem 2rem 1rem 2rem;
            background-color:#ECF1F6;
            border-left-color: #467AAC;
            border-radius: 10px;
        }*/
        blockquote.noborder {
            border-left: unset;
        }
                
        blockquote {
            border: 1px solid;
            opacity: 1;
            -webkit-box-pack: justify;
            justify-content: space-between;
            /*display: flex;*/
            transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
            transition-duration: 200ms;
            transition-property: all;
            box-shadow: none;
            
            border-top-left-radius: 0.25rem;
            border-top-right-radius: 0.25rem;
            border-bottom-left-radius: 0.25rem;
            border-bottom-right-radius: 0.25rem;
            
            margin-top: 0px;
            margin-bottom: 1rem;
            margin-left: 0px;
            margin-right: 0px;
            
            padding-left: 16px;
            padding-right: 16px;
            padding-top: 16px;
            padding-bottom: 16px;
            
            height: auto;
            pointer-events: auto;
            
            line-height: 1.6;
            font-weight: normal;
            font-family: "IBM Plex Sans", sans-serif;
            font-size: 1rem;
        }
        .quant-bb{
        	display: inline-block;
            padding-left: 10px;
            padding-right: 10px;
            border-radius: 6px;
            margin-top: 3px;
        }
        </style>
        """, unsafe_allow_html=True
    )
