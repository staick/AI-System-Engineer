import numpy as np


def identity(x):
    return x


def binary_step(x):
    return np.array(x > 0, dtype=int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def tanh(x):
    # return np.tanh(x)
    return (1 - np.exp(-2 * x)) / (1 + np.exp(-2 * x))


def relu(x):
    return np.maximum(0, x)


def softmax_basis(x):
    return np.exp(x) / np.sum(np.exp(x))


def softmax_advanced(x):
    x -= np.max(x)
    return np.exp(x) / np.sum(np.exp(x))


def softmax(x):
    if x.ndim == 2:
        # 转置是为了方便进行广播
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x))
        return y.T

    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))


def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


def cross_entropy_error(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    if y.size == t.size:
        t = np.argmax(t, axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
