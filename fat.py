import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

low_l = -500
low_h = 500

frames = np.arange(0.66*np.pi, 2*0.67*np.pi, 0.01)

plt.style.use('dark_background')
fig, ax = plt.subplots()
anim_object, = plt.plot([], [],'-', lw=1, color='maroon', label='Эффект гравитационного линзирования',)
ax.set_title('Voltage vs. time chart', color='darkgray')
ax.set_facecolor('darkgray')
ax.legend('Ф')
ax.tick_params(labelcolor='maroon')
ax.set_ylabel('Coord: y', color='darkgray')
ax.set_xlabel('Coord: x', color='darkgray')
plt.grid()
plt.title('Гравитационная линза')
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
#abs(p1*coord1 + n*coord2 + p2)/(p1**2 + p2**2)**0.5
b = 50**0.5
# константы
M = 0.7*10**27
G = 6.67*10**(-11)
c = 299792458
k = b/((c**2)/(G*M))

xdata, ydata = [], []

def muweng(t):
	y0 = (-p1/n)*t - p2/n
	r = b*k / (1 + k*np.cos(t) + (np.sin(t))**2)
	x2 = r*np.cos(np.pi/2 + t)
	y2 = r*np.sin(np.pi/2 + y0)
	xdata.append(x2)
	ydata.append(y2)

# alpha = np.arange(-2*np.pi, 2*np.pi, 0.01)
# r = b*k / (1 + k*np.cos(alpha) + (np.sin(alpha))**2)

# plt.plot(alpha, r)
def update(frame):
		muweng(frame)
		anim_object.set_data(xdata, ydata)
		return anim_object,


anim = FuncAnimation(fig, update, frames=frames, interval=3)
plt.show()