import numpy as np
import pandas as pd

items = [[3,4,3,1],[1,3,3,5],[2,4,1,5],[3,3,5,2],[3,5,4,1]]
cols = [f'item{i}' for i in range(1,6)]



print(pd.DataFrame(np.corrcoef(items),columns=cols,index=cols))
