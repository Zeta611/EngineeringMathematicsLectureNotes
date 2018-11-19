from matplotlib import pyplot as plt
import numpy as np

y_1, y_2 = np.meshgrid(np.arange(-7, 7, .1), np.arange(-7, 7, .1))

y_1_dot = -y_1 + y_2
y_2_dot = -y_1 - y_2

start = [
    [4, 4],
    [4, -4],
    [0, 4],
    [4, 0],
    [-4, -4],
    [-4, 4],
    [0, -4],
    [-4, 0],
    [np.sqrt(3), 1],
    [1, np.sqrt(3)],
    [-np.sqrt(3), -1],
    [-1, -np.sqrt(3)],
    [-np.sqrt(3), 1],
    [-1, np.sqrt(3)],
    [np.sqrt(3), -1],
    [1, -np.sqrt(3)],
]

fig = plt.figure(1, figsize=(5, 5))
ax = fig.add_subplot(111)
ax.axis('equal')
ax.streamplot(
    y_1, y_2, y_1_dot, y_2_dot,
    density=.5,
    linewidth=1,
    start_points=start,
    maxlength=5,
)

ax.set_xlabel(r"$y_1$")
ax.set_ylabel(r"$y_2$")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.tick_params(top="off", right="off", bottom="off", left="off")

plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())

circle = plt.Circle((0, 0), 0.8, color='white', zorder=10)
ax.add_artist(circle)

#  plt.show()
plt.savefig("spiral_point.pdf", bbox_inches="tight", transparent=True)
plt.clf()
