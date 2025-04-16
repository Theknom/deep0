from .and_module import AND1
# and_moduleだと、挙動がおかしくなる可能性があるため、.and_module
import numpy as np

class AND2(AND1):
    def __init__(self, x1, x2):
        super().__init__(x1, x2) # x1, x2, w1, w2, thetaは親クラスのAND1から継承して、変更しない。新しくb=-0.7を追加。
        self.b = -0.7
        # self.w = np.array([0.5, 0.5])
        self.w = np.array([self.w1, self.w2])
        self.x = np.array([x1, x2])

    def output(self):
        tmp = np.sum(self.w * self.x) + self.b
        if tmp <= 0:
            return 0
        else:
            return 1