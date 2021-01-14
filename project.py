import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball1, = plt.plot([], [], 'o', color='b', label='Ball1')
ball2, = plt.plot([], [], 'o', color='r', label='Ball2')

def circle_move1(R1, v1x0, v1y0, time):
    x01 = 10+v1x0*time
    y01 = 0
    alpha = np.arange(0,2*np.pi, 0.1)
    x1 = x01 + R1*np.cos(alpha)
    y1 = y01 + R1*np.sin(alpha)
    return x1, y1

def circle_move2(R2, v2x0, v2y0, time):
    x02 = -10+v2x0*time
    y02 = 0
    alpha = np.arange(0,2*np.pi, 0.1)
    x2 = x02 + R2*np.cos(alpha)
    y2 = y02 + R2*np.sin(alpha)
    return x2, y2

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(i):
    ball1.set_data(circle_move1(R1=0.5, v1x0=-0.1, v1y0=0.1, time=i))
    ball2.set_data(circle_move2(R2=0.5, v2x0=0.1, v2y0=0.1, time=i))

ani = animation.FuncAnimation(fig,animate,frames=100,interval=30)

def move1(R1, v1x0, v1y0, time):
    x01 = v1x0*time
    y01 = 0
    alpha = np.arange(0,2*np.pi, 0.1)
    x1 = x01 + R1*np.cos(alpha)
    y1 = y01 + R1*np.sin(alpha)
    return x1, y1

def move2(R2, v2x0, v2y0, time):
    x02 = v2x0*time
    y02 = 0
    alpha = np.arange(0,2*np.pi, 0.1)
    x2 = x02 + R2*np.cos(alpha)
    y2 = y02 + R2*np.sin(alpha)
    return x2, y2

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def anim(i):
    ball1.set_data(move1(R1=0.5, v1x0=-0.1, v1y0=0.1, time=i))
    ball2.set_data(move2(R2=0.5, v2x0=0.1, v2y0=0.1, time=i))
ani = anim.FuncAnimation(fig,animate,frames=100,interval=30)

ani.save('lec_7_complex_animation.gif')