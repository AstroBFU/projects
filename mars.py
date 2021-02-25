import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.axisartist.axislines import Subplot

'''fig = plt.figure()
ax = Subplot(fig, 111)
fig.add_subplot(ax)'''

G = 6.67 * 10**(-11)
M = 1.9885*10**30

# Earth
q_earth = 1.470568 * 10**11
a_earth = 1.496 *10**11
b_earth = 1.49578 * 10**11
c_earth = 2.5432 * 10**9
T_earth = 31536000
omega_earth = 2*np.pi/T_earth

# Mars
q_mars = 2.0674504474 * 10**11
a_mars = 2.2794382 * 10**11
b_mars = 2.06745 * 10**11
c_mars = 2.119877526 * 10**10
T_mars = 59355072
omega_mars = 2*np.pi/T_mars

# Sat
q_sat = a_earth
# a_sat = (a_earth + a_mars)/2
a_sat = 199099999900
b_sat=(a_sat**2 - (a_sat-q_sat)**2)**0.5
c_sat = a_sat - q_sat
T_sat = ((4*(np.pi)**2)/(G*M) * a_sat**3)**0.5
t_fly = T_sat/2 
#2,23733*10**7,  B=2,36838
omega_sat = 2*np.pi/T_sat


fig, ax = plt.subplots()
circle1, = plt.plot([], [], '-', color='grey', label='-')
circle2, = plt.plot([], [], '-', color='grey', label='-')
Earth, = plt.plot([], [], 'o', color='blue', label='Earth',ms=12)
circle3, = plt.plot([], [], '-', color='r', label='-')
Sun, = plt.plot([], [], 'o', color='gold', label='The Sun',ms=20)
Mars, = plt.plot([], [], 'o', color='r', label='Mars', ms=10)
Satellite, = plt.plot([], [], 'o', color='black', label='Satellite', ms=6)


def Sun_move():
  x=0
  y=0
  return x, y

def object_move(omega, t, a, b, c, x_0=0, y_0=0):
  alpha = t * omega
  x = np.cos(alpha) * a - c + x_0
  y = np.sin(alpha) * b + y_0
  return x, y

def trajectory(a, b, c):
  alpha = np.arange(0, 3 * np.pi, 0.1)
  x = np.cos(alpha) * a - c
  y = np.sin(alpha) * b 
  return x, y

edge = 1.5*a_mars
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
'''ax.axis["right"].set_visible(False)
ax.axis["left"].set_visible(False)
ax.axis["bottom"].set_visible(False)
ax.axis["top"].set_visible(False)'''

def animate(i):
  Sun.set_data(Sun_move())
  Earth.set_data(object_move(omega = omega_earth,
                             t=i,
                             a = a_earth,
                             b = b_earth,
                             c = c_earth))
  circle1.set_data(trajectory(a = a_earth, 
                              b = b_earth,
                              c = c_earth))
  circle2.set_data(trajectory(a = a_mars, 
                              b = b_mars,
                              c = c_mars))
  Mars.set_data(object_move(omega = omega_mars,
                             t=i,
                             a = a_mars,
                             b = b_mars,
                             c = c_mars,
                             x_0 = a_mars * np.cos(0.77),
                             y_0 = a_mars * np.sin(0.77)))
  circle3.set_data(trajectory(a = a_sat, 
                              b = b_sat,
                              c = c_sat))
  Satellite.set_data(object_move(omega = omega_sat,
                                 t=i,
                                 a = a_sat,
                                 b = b_sat,
                                 c = c_sat))
  ax.set_title(f'Дни: {i}')

ani = FuncAnimation(fig,
                  animate,
                  frames=np.linspace(0, T_earth, 500),
                  interval=50)

plt.show()
