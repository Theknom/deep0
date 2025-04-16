# ステップ関数を実数だけでなく、実数配列に対応できるようにする

# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0


import numpy as np 
def step_function(x):
    return np.array(x > 0, dtype=int)