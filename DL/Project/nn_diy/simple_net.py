from common.gradient import numerical_gradient
from common.functions import softmax, cross_entropy_error
import numpy as np


class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def forward(self, x):
        z = np.dot(x, self.W)
        y = softmax(z)
        return y

    def loss(self, x, t):
        y = self.forward(x)
        loss = cross_entropy_error(y, t)
        return loss


if __name__ == "__main__":
    net = SimpleNet()
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])

    f = lambda _: net.loss(x, t)
    dW = numerical_gradient(f, net.W)
    print(dW)
