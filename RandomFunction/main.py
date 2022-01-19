import numpy as np
import pandas as pd
import mathplotlib.pyplot as plt

def randomBinning(count, loopCount, return_string=False):
    import numpy as np

    sum_count = 0
    functionList = []

    for i in range(loopCount-1):
        function = np.random.randint(0, count+1)
        if return_string:
            functionList.append(str(function))
        else:
            functionList.append(function)