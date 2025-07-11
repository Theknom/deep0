# coding: utf-8
import sys, os
# sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定

sys.path.append('/root/work/deep0')
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax

# print("hello")

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("/root/work/deep0/ch03/network/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f) # sample_weight.pklに保存されたモデルの学習済みパラメータを読み込む（dict型で読み込む）
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y



x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    # y = predict(network, x[i])
    # p= np.argmax(y) # 最も確率の高い要素のインデックスを取得
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))