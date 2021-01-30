import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

low_l = 0
low_h = 10

frames = 1000

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
plt.axis('equal')
ax.set_xlim(low_l, low_h)
ax.set_ylim(low_l-10, low_h)

def garmonic_f(t, A = 1, B = 1, w = np.pi, k = np.pi):
  x = np.linspace(0, 2*np.pi, frames)
  y = A*np.cos(w*t - k*x) + B*np.cos(w*t + k*x)
  return x, y


def update(frame):
	anim_object.set_data(garmonic_f(A = 0.5, t = frame))

anim = FuncAnimation(fig, update, frames, interval=300)
plt.show()
