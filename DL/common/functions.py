import numpy as np


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
