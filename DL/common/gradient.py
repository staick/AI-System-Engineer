import numpy as np
import copy


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x)) / h


def central_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def _numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp + h
        fxh1 = f(x)
        x[i] = tmp - h
        fxh2 = f(x)
        grad[i] = (fxh1 - fxh2) / (2 * h)
        x[i] = tmp
    return grad


def numerical_gradient(f, x):
    if x.ndim == 1:
        return _numerical_gradient(f, x)
    else:
        grad = np.zeros_like(x)
        for i, v in enumerate(x):
            grad[i] = _numerical_gradient(f, v)
        return grad


def gradient_descent(f, init_x, lr=0.01, step=100):
    x = init_x
    x_history = []
    for i in range(step):
        x_history.append(x.copy())
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x, np.array(x_history)
