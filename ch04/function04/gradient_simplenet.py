import sys, os 
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # (2,3)の行列を重みとして初期化       
    
    def predict(self, x):
        return np.dot(x, self.W) # P.61のニューラルネットワークと同様の計算
    
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z) # softmax関数で確率に変換
        loss = cross_entropy_error(y, t) # 交差エントロピーを損失関数とする
        return loss