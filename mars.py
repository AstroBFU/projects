import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
G = 6.67 * 10**(-11)
M = 1.9885*10**30
a_earth = 50
g_sat = a_earth
a_mars = 70
a_sat = (a_earth + a_mars)/2
T_sat = ((4*(np.pi)**2)/(G*M) * a_sat**3)**0.5
t_fly = T_sat/2
Omega = 0.52
Beta = t_fly * Omega * np.pi/180
Gamma = np.pi - Beta

fig, ax = plt.subplots()
circle1, = plt.plot([], [], '-', color='grey', label='-')
circle2, = plt.plot([], [], '-', color='grey', label='-')
Earth, = plt.plot([], [], 'o', color='blue', label='Earth',ms=12)
circle3, = plt.plot([], [], '-', color='r', label='-')
Sun, = plt.plot([], [], 'o', color='gold', label='The Sun',ms=20)
Mars, = plt.plot([], [], 'o', color='r', label='Mars', ms=10)
Satellite, = plt.plot([], [], 'o', color='black', label='Satellite', ms=6)
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def Sun_move():
  x=0
  y=0
  return x, y

def object_move(R, T, t, a):
  W = 2*np.pi/T
  alpha = t * W
  x = np.cos(alpha) * R
  y = np.sin(alpha) * R - a
  return x, y

def trajectory(R):
  alpha = np.arange(0, 3 * np.pi, 0.1)
  x = np.cos(alpha) * R
  y = np.sin(alpha) * R
  return x, y

def traj_sat(R):
  alpha = np.arange(0, 3 * np.pi, 0.1)
  x = np.cos(alpha) * R
  y = np.sin(alpha) * R - 12
  return x, y

edge = 150
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def animate(i):
  #time_text.set_text(f'days: {i}')
  Sun.set_data(Sun_move())
  Earth.set_data(object_move(R=50, T=365, t=i, a=0))
  circle1.set_data(trajectory(R=50))
  circle2.set_data(trajectory(R=75))
  Mars.set_data(object_move(R=75, t=i, T=687, a=0))
  circle3.set_data(traj_sat(R=62))
  Satellite.set_data(object_move(R=62, T=515 ,t=i, a=12))


ani = FuncAnimation(fig,
                    animate,
                    frames=500,
                    interval=50)

plt.show()
#ani.save('project.gif')
