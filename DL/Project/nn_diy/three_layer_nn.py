import numpy as np
from common.functions import sigmoid, identity


def init_network():
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["W2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    w1, w2, w3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = x @ w1 + b1
    z1 = sigmoid(a1)
    a2 = z1 @ w2 + b2
    z2 = sigmoid(a2)
    a3 = z2 @ w3 + b3
    z3 = identity(a3)

    return z3


network = init_network()
x = np.array([1, 0.5])
y = forward(network, x)
print(y)
