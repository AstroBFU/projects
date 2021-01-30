import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
plt.axis('equal')
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-2*np.pi, 2*np.pi)

def garmonic_f(t, A = 1, B = 1, w = np.pi, k = np.pi):
	x = t
	y = A*np.cos(w*t - k*x) + B*np.cos(w*t + k*x)
	return x, y

'''def oscillation(x, t):	
	phi = np.arange(0, 2*np.pi, 0.01)
	y = r*np.sin(phi)
	return x, y
'''

def update(frame):
	anim_object.set_data(garmonic_f(t = frame))

anim = FuncAnimation(fig, update, frames = 500, interval=30)
anim.save('oscillation.gif')