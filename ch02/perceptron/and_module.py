import numpy as np

class AND1:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

        # Initialize weights and threshold
        self.w1 = 0.5
        self.w2 = 0.5
        self.theta = 0.8 
        # 0.7でも動く。
        # 閾値の関係で0.7をあらかじめ設定していただけで、0.5より大きくて1.0より小さい値であれば何でも良い。
    
    def output(self):
        temp = self.x1 * self.w1 + self.x2 * self.w2
        if temp<= self.theta:
            return 0
        elif temp > self.theta:
            return 1

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