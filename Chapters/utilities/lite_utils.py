# Why lite_utils?
# Each subfolder in Chapters have there own requirements.txt.
# These folders uses utils folders and if a subfolder don't uses a heavy module,
# but utils file import that module then we have to take that heavy module into that requirements.txt
# And these lite_utils solves exactly that problem.

import numpy as np
import pandas as pd


def stPandas(npArray: np.ndarray, label: str = "Random Draws") -> pd.DataFrame:
    npArray = npArray.reshape((1, len(npArray)))
    npArray = pd.DataFrame(data=npArray, index=[label])
    npArray.columns += 1
    return npArray
