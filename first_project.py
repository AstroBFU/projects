# pet-project "Jerk off the strings"
# developer: Pryadko Oleg
# git: https://github.com/Fellow-fiend
# description: this program makes a standed string and show her oscillations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib


'''
import matplotlib.cbook as cbook

with cbook.get_sample_data('C:/Users/Олег/Desktop/q/qq/small_ship.png') as image_file:
    image = plt.imread(image_file)
'''


# limits
low_l = 0
low_h = 50

frames = 1000


fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
ship_object, = plt.plot([], [], marker=matplotlib.markers.CARETDOWNBASE, markersize=30)

plt.axis('equal')
ax.set_xlim(low_l, low_h)
ax.set_ylim(-low_h, low_h)







def garmonic_f(t, A = 0.5, B = -0.5, w = 0.07, k = 1, L = 4*np.pi, n = 1):
	# B must be equals -A to the left part is fixed
	# Length of x must be equals L*n/2 to the right part is fixed
	x = np.linspace(0, L*n/2, frames)
	y = (A*np.sin(w*t - k*x) + B*np.sin(w*t + k*x))
	return x, y

def garmonic_sf(t, A, w, k, L = 4*np.pi, n = 1):
	x = np.linspace(0, L*n/2, frames)
	y = A*np.sin(k*x - w*t)*np.sin(w*t)
	#ax.fill_between(x, y, x*0-2, facecolor = "white")
	ax.collections.clear()
	ax.fill_between(x, y, x*0-10, color = "blue")
	return x, y

def ship(t, A, w, k, L = 4*np.pi, n = 1):
	temp = np.linspace(0, L*n/2, frames)
	x = temp[t]
	y = A*np.sin(k*x - w*t)*np.sin(w*t) + 1.5
	return x, y


'''def ship(t, A, w, k, L = 4*np.pi, n = 1):
	temp = np.linspace(0, L*n/2, frames)
	x = temp[t]
	y = A*np.sin(k*x - w*t)*np.sin(w*t) + 1.5
	ax.imshow(image)
'''


def update(frame):
	ship_object.set_data(ship(t = frame, A = 0.8, L = 15*np.pi, w = 0.09, k = 1, n = 2))
	anim_object.set_data(garmonic_sf(t = frame, A = 0.8, L = 15*np.pi, w = 0.09, k = 1, n = 2))
	ship(t = frame, A = 0.8, L = 15*np.pi, w = 0.9, k = 1, n = 2)

anim = FuncAnimation(fig, update, frames, interval=30)
plt.show()
