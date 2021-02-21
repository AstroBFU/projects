# pet-project "Jerk off the strings"
# developer: Pryadko Oleg
# git: https://github.com/Fellow-fiend
# description: this program makes a standed string and show her oscillations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 
low_l = 0
low_h = 10

frames = 1000

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
plt.axis('equal')
ax.set_xlim(low_l, low_h)
ax.set_ylim(low_l-10, low_h)

def garmonic_f(t, A = 0.5, B = -0.5, w = 0.07, k = 1, L = 2*np.pi, n = 3):
	# B must be equals -A to the left part is fixed
	# Length of x must be equals L*n/2 to the right part is fixed
  x = np.linspace(0, L*n/2, frames)
  y = A*np.cos(w*t - k*x) + B*np.cos(w*t + k*x)
  return x, y

def garmonic_sf(t, A, w, k):
	x = np.linspace(0, 2*np.pi, frames)
	y = 2*A*np.sin(w*t)*np.sin(k*x)
	return x, y


def update(frame):
	anim_object.set_data(garmonic_f(frame))

anim = FuncAnimation(fig, update, frames, interval=60)
plt.show()