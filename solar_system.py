import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()
ax = Subplot(fig, 111)
fig.add_subplot(ax)

ellips1, = plt.plot([], [], '-', color='black', label='ellips1', lw=0.5)
ellips2, = plt.plot([], [], '-', color='black', label='ellips2', lw=0.5)
ellips3, = plt.plot([], [], '-', color='black', label='ellips3', lw=0.5)
ellips4, = plt.plot([], [], '-', color='black', label='ellips4', lw=0.5)
ellips5, = plt.plot([], [], '-', color='black', label='ellips5', lw=0.5)
ellips6, = plt.plot([], [], '-', color='black', label='ellips6', lw=0.5)
ellips7, = plt.plot([], [], '-', color='black', label='ellips7', lw=0.5)
ellips8, = plt.plot([], [], '-', color='black', label='ellips8', lw=0.5)
ellips9, = plt.plot([], [], '-', color='black', label='ellips9', lw=0.5)
Sun, = plt.plot([], [], 'o', color='orange', label='Sun', lw=1, ms=18)
Mercury, = plt.plot([], [], 'o',color='darkslategrey',label='Mercury',lw=1,ms=3)
Venus, = plt.plot([], [], 'o', color='chocolate', label='Venus', lw=1, ms=5)
Earth, = plt.plot([], [], 'o', color='green', label='Earth', lw=1, ms=5)
Mars, = plt.plot([], [], 'o', color='red', label='Mars', lw=1, ms=4)
Jupiter, = plt.plot([], [], 'o', color='peru', label='Jupiter', lw=1, ms=14)
Saturn, = plt.plot([], [], 'o', color='tan', label='Saturn', lw=1, ms=12)
Uranus, = plt.plot([], [],'o', color='lightskyblue',label='Uranus',lw=1,ms=7)
Neptune, = plt.plot([], [], 'o', color='blue', label='Neptune', lw=1, ms=6)
Pluto, = plt.plot([], [], 'o',color='darkslategray',label='Pluto',lw=1,ms=4)

def Sun_move():
	x = 0
	y = 0
	return x, y

def Planet_move(T, a, b, time):
	angle_vel = 2 * np.pi / T
	alpha = time * angle_vel
	x = a * np.cos(alpha)
	y = b * np.sin(alpha)
	return x, y

def Trajectory_move(a, b):
	alpha = np.arange(0, 3 * np.pi, 0.1)
	x = a * np.cos(alpha)
	y = b * np.sin(alpha)
	return x, y

plt.axis('equal')
ax.set_xlim(-350, 350)
ax.set_ylim(-350, 350)
ax.axis["right"].set_visible(False)
ax.axis["left"].set_visible(False)
ax.axis["bottom"].set_visible(False)
ax.axis["top"].set_visible(False)

def animate(i):
    Sun.set_data(Sun_move())
    Mercury.set_data(Planet_move(T=88, a=35, b=22, time=i))
    Mercury.set_data(Planet_move(T=88, a=35, b=22, time=i))
    Venus.set_data(Planet_move(T=225, a=55, b=32, time=i))
    Earth.set_data(Planet_move(T=365, a=80, b=44, time=i))
    Mars.set_data(Planet_move(T=687, a=110, b=58, time=i))
    Jupiter.set_data(Planet_move(T=4329, a=145, b=74, time=i))
    Saturn.set_data(Planet_move(T=10753, a=185, b=92, time=i))
    Uranus.set_data(Planet_move(T=30667, a=230, b=112, time=i))
    Neptune.set_data(Planet_move(T=60145, a=280, b=134, time=i))
    Pluto.set_data(Planet_move(T=90553, a=335, b=158, time=i))
    ellips1.set_data(Trajectory_move(a=35, b=22))
    ellips2.set_data(Trajectory_move(a=55, b=32))
    ellips3.set_data(Trajectory_move(a=80, b=44))
    ellips4.set_data(Trajectory_move(a=110, b=58))
    ellips5.set_data(Trajectory_move(a=145, b=74))
    ellips6.set_data(Trajectory_move(a=185, b=92))
    ellips7.set_data(Trajectory_move(a=230, b=112))
    ellips8.set_data(Trajectory_move(a=280, b=134))
    ellips9.set_data(Trajectory_move(a=335, b=158))
    ax.set_title(f'Дни: {i}')


ani = animation.FuncAnimation(fig, animate, frames=365, interval=30)

plt.show()
