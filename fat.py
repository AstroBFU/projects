import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

low_l = 0
low_h = 150

frames = 500

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '.', lw=5)
plt.axis('equal')
ax.set_xlim(low_l, low_h)
ax.set_ylim(low_l, low_h)


b = 2
r = -100 + b
M = 10**6
G = 6.67*10**(-11)
c = 299792458

def muweng(t):
    global r
    alpha = G*M/(r*c**2)
    x0 = t
    y0 = t + b
    x2 = x0 * np.cos(alpha) - y0 * np.sin(alpha)
    y2 = x0 * np.sin(alpha) + y0 * np.cos(alpha)
    r = ((102-x2) ** 2 + (100 - y2) ** 2)**0.5
    return x2, y2


def update(frame):
	anim_object.set_data(muweng(frame))

anim = FuncAnimation(fig, update, frames, interval=100)
plt.show()
