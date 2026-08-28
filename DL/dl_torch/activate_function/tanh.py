import torch
import matplotlib.pyplot as plt

x = torch.linspace(-5, 5, 1000, requires_grad=True)
x_d = x.detach().numpy()
y = torch.tanh(x)
y_d = y.detach().numpy()

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(12, 4)
ax[0].plot(x_d, y_d)
ax[0].set_title("tanh(x)")
ax[0].spines["top"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].spines["left"].set_position(("data", 0))
ax[0].spines["bottom"].set_position(("data", 0))


torch.tanh(x).sum().backward()
ax[1].plot(x_d, x.grad)
ax[1].set_title("tanh'(x)")

plt.show()
