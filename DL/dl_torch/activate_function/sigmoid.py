import matplotlib.pyplot as plt
import torch

x = torch.linspace(-10, 10, 1000, requires_grad=True)
x_d = x.detach().numpy()
y = torch.sigmoid(x)
y_d = y.detach().numpy()
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(12, 4)

ax[0].plot(x_d, y_d)
ax[0].set_title("sigmoid(x)")
ax[0].spines["top"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].spines["left"].set_position(("data", 0))
ax[0].spines["bottom"].set_position(("data", 0))
ax[0].axhline(y=0.5, color="gray", alpha=0.7, linewidth=1)
ax[0].axhline(y=1, color="gray", alpha=0.7, linewidth=1)

torch.sigmoid(x).sum().backward()
ax[1].plot(x_d, x.grad)
ax[1].set_title("sigmoid'(x)")
ax[1].spines["top"].set_visible(False)
ax[1].spines["right"].set_visible(False)
ax[1].spines["left"].set_position(("data", 0))
ax[1].spines["bottom"].set_position(("data", 0))
ax[1].set_ylim(0, 0.3)

plt.show()
