from gui.stats import stats
from gui.lln import lln
from auth.stInputs import stEmpty

def clear(elements):
    for element in elements:
        element.empty()

def main(elements, email, state, GlobalElements):
    clear(elements)
    #stwrite(":floppy_disk:")
    element = stEmpty()
    option  =  element.selectbox(
                                    "", # Label
                                    (
                                        "Introduction", 
                                        "Law of Large Number (patreon)", 
                                        "Central Limit Theorem (patreon)"
                                    ),
                                    index = 1
                                )
    GlobalElements.append(element)
    if(option=="Introduction"):
        stats.main(state, GlobalElements)
    elif(option=="Law of Large Number (patreon)"):
        lln.main(state, GlobalElements)
    """
    elif(option=="Central Limit Theorem (patreon)"):
        clt.main()
    """