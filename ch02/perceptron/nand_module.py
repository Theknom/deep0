import numpy as np

class NAND:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.w = np.array([-0.5, -0.5])
        self.x = np.array([x1, x2])
        self.b = 0.8 # 本来0.7

    def output(self):
        tmp = np.sum(self.w * self.x) + self.b
        if tmp <= 0:
            return 0
        else:
            return 1