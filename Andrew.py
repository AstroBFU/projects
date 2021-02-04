import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

low_l = -500
low_h = 500

frames = np.arange(-2*np.pi, 2*np.pi, 0.01)

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
plt.axis('equal')
ax.set_xlim(low_l, low_h)
ax.set_ylim(low_l, low_h)

# координаты массивного тела (в будущем координаты фотона)
coord1 = 100
coord2 = 110

# y = (-p1/n) * x - p2/n
# параметры прямой фотона
p1 = 1
p2 = 0
n = 1

# distance
# abs(p1*coord1 + n*coord2 + p2)/(p1**2 + p2**2)**0.5
b = 50**0.5
# константы
M = 0.7*10**27
G = 6.67*10**(-11)
c = 299792458
k = b/((c**2)/(G*M))

xdata, ydata = [], []

def muweng(t):
	#x0 = t
	#y0 = (-p1/n)*t - p2/n
	#alpha = np.arange(-2*np.pi, 2*np.pi, 0.01)
	r = b*k / (1 + k*np.cos(t) + (np.sin(t))**2)
	x2 = r*np.cos(np.pi/2 + t)
	y2 = r*np.sin(np.pi/2 + t)
	xdata.append(x2)
	ydata.append(y2)


def update(frame):
		muweng(frame)
		anim_object.set_data(xdata, ydata)
		return anim_object,


anim = FuncAnimation(fig, update, frames, interval=100)
plt.show()
