import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from random import random as rnd

b = rnd()

fig, ax = plt.subplots()

num_bobbles = 500
bobbles = []
for i in range(num_bobbles):
    bobble, = plt.plot([], [], '-', color='b')
    bobbles.append(bobble)

delays = []
for i in range(num_bobbles):
    delays.append(300*rnd())

x_coords = []
for i in range(num_bobbles):
    x_coords.append(100*rnd())

y_coords = []
for i in range(num_bobbles):
    y_coords.append(100*rnd())

# t = int(input('Введите t:'))
t = 80


def circle_move(time, delay, x1, y1):
    phi = np.arange(0, 2 * np.pi, 0.01)
    if delay > time:
        x = 0
        y = 0
    else:
        if t >= 90:
            a = 0.0001 * b * 30 * t
        elif t >= 80 and t < 90:
            a = 0.0001 * b * 3 * t
        else:
            a = 0.0001 * b * 1.5 * t

        vy0 = 0.02 * t
        y0 = vy0 * (time - delay)
        y1 = 0
        R = a * time

        x = R * np.cos(phi) + x1
        y = y0 + R * np.sin(phi) + y1

    return x, y

edge = 100
plt.axis('equal')
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)


def animate(i):
    for j in range(num_bobbles):
        bobbles[j].set_data(circle_move(time=i,
                                        delay=delays[j],
                                        x1=x_coords[j],
                                        y1=y_coords[j]))


ani = FuncAnimation(fig,
                    animate,
                    frames=200,
                    interval=30
                    )
ani.save('kipenie(TEST!4).gif')
