from functions import sigmoid
import numpy as np

class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        y = x.copy()
        y[self.mask] = 0
        return y

    def backward(self, dy):
        dx = dy.copy()
        dx[self.mask] = 0
        return dx


class Sigmoid:
    def __init__(self):
        self.y = None

    def forward(self, x):
        y = sigmoid(x)
        self.y = y
        return y

    def backward(self, dy):
        dx = dy * self.y * (1.0 - self.y)
        return dx

class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.X = None
        self.original_x_shape = None
        self.dW = None
        self.db = None

    def forward(self, X):
        self.original_x_shape = X.shape
        self.X = X.reshape(X.shape[0], -1)
        y = np.dot(X, self.W) + self.b
        return y

    def backward(self, dy):
        dX = np.dot(dy, self.W.T)
        dX = dX.reshape(*self.original_x_shape)
        self.dW = np.dot(self.X.T, dy)
        self.db = np.sum(dy, axis=0)
        return dX

