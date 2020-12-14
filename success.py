from gui.stats import stats
from gui.lln import lln
from gui.clt import clt
from auth.stInputs import stEmpty
from utils import chapters, chapters_acronyms, chapter2idx, getChapterIndexByURL, set_get_URL
import streamlit as st

def clear(elements):
    #print("      clear(elements)")
    for element in elements:
        element.empty()

def main(elements, email, state, GlobalElements):
    #print("    ======== success.py [START] ========")
    #print("    ARGUMENTS: elemants, email=" + email + ", state, GlobalElements")
    clear(elements)
    #stwrite(":floppy_disk:")
    idx = getChapterIndexByURL(state.url)# if state.TOTAL_RELOADS==1 else state.url)
    option  =  st.selectbox("", chapters , index = idx)
    url = set_get_URL(ch = chapters_acronyms[chapter2idx(option)])
    
    #print("          * idx: ",idx)
    #print("          * option: ",option)
    #print("          * url: ",url)
    
    #if(option==chapters[0]):
    #    stats.main(state, GlobalElements)
    #    set_get_URL(dist = "remove")
    if(option==chapters[0]):
        lln.main(state, GlobalElements)
    elif(option==chapters[1]):
        clt.main() 

    #print("    ======== success.py  [END]  ========")
    