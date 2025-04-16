import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# ブロードキャストにより、配列に対しても適用できる