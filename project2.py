import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random

b = random.random()

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='b')
ball1, = plt.plot([], [], '-', color='b')
ball2, = plt.plot([], [], '-', color='b')
ball3, = plt.plot([], [], '-', color='b')
ball4, = plt.plot([], [], '-', color='b')
ball5, = plt.plot([], [], '-', color='b')
ball6, = plt.plot([], [], '-', color='b')
ball7, = plt.plot([], [], '-', color='b')
ball8, = plt.plot([], [], '-', color='b')
ball9, = plt.plot([], [], '-', color='b')
ball10, = plt.plot([], [], '-', color='b')
ball11, = plt.plot([], [], '-', color='b')
ball12, = plt.plot([], [], '-', color='b')
ball13, = plt.plot([], [], '-', color='b')
ball14, = plt.plot([], [], '-', color='b')
ball15, = plt.plot([], [], '-', color='b')
ball16, = plt.plot([], [], '-', color='b')
ball17, = plt.plot([], [], '-', color='b')
ball18, = plt.plot([], [], '-', color='b')
ball19, = plt.plot([], [], '-', color='b')
ball20, = plt.plot([], [], '-', color='b')
ball21, = plt.plot([], [], '-', color='b')
ball22, = plt.plot([], [], '-', color='b')
ball23, = plt.plot([], [], '-', color='b')
ball24, = plt.plot([], [], '-', color='b')
ball25, = plt.plot([], [], '-', color='b')
ball26, = plt.plot([], [], '-', color='b')
ball27, = plt.plot([], [], '-', color='b')
ball28, = plt.plot([], [], '-', color='b')
ball29, = plt.plot([], [], '-', color='b')
ball30, = plt.plot([], [], '-', color='b')
ball31, = plt.plot([], [], '-', color='b')
ball32, = plt.plot([], [], '-', color='b')
ball33, = plt.plot([], [], '-', color='b')
ball34, = plt.plot([], [], '-', color='b')
ball35, = plt.plot([], [], '-', color='b')
ball36, = plt.plot([], [], '-', color='b')
ball37, = plt.plot([], [], '-', color='b')
ball38, = plt.plot([], [], '-', color='b')
ball39, = plt.plot([], [], '-', color='b')
ball40, = plt.plot([], [], '-', color='b')
ball41, = plt.plot([], [], '-', color='b')
ball42, = plt.plot([], [], '-', color='b')
ball43, = plt.plot([], [], '-', color='b')
ball44, = plt.plot([], [], '-', color='b')
ball45, = plt.plot([], [], '-', color='b')
ball46, = plt.plot([], [], '-', color='b')
ball47, = plt.plot([], [], '-', color='b')
ball48, = plt.plot([], [], '-', color='b')
ball49, = plt.plot([], [], '-', color='b')
ball50, = plt.plot([], [], '-', color='b')
ball51, = plt.plot([], [], '-', color='b')
ball52, = plt.plot([], [], '-', color='b')
ball53, = plt.plot([], [], '-', color='b')
ball54, = plt.plot([], [], '-', color='b')
ball55, = plt.plot([], [], '-', color='b')
ball56, = plt.plot([], [], '-', color='b')
ball57, = plt.plot([], [], '-', color='b')
ball58, = plt.plot([], [], '-', color='b')
ball59, = plt.plot([], [], '-', color='b')
ball60, = plt.plot([], [], '-', color='b')
t = int(input('Введите t:'))


def circle_move(phi, time, delay, x1, y1):
    if delay < time:
        x = 0
        y = 0
    else:
        if t >= 90:
            a = 0.0001 * b * 70 * t
        else:
            a = 0.0001 * b * t
        vy0 = 0.02 * t
        y0 = vy0 * (time-delay)
        alpha = a * (np.pi / 180) * (time-delay)
        R = alpha * (time-delay)
        x = R * np.cos(phi) + x1
        y = y0 + R * np.sin(phi) + y1
    return x, y


edge = 200
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)


def animate(i):
    ball.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=0, x1=0, y1=0))
    ball1.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=1, x1=30, y1=0))
    ball2.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=2, x1=60, y1=0))
    ball3.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=3, x1=-30, y1=0))
    ball4.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=4, x1=-60, y1=0))
    ball5.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=5, x1=-50, y1=40))
    ball6.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=6, x1=-20, y1=35))
    ball7.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=7, x1=-10, y1=50))
    ball8.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=8, x1=-45, y1=20))
    ball9.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=9, x1=-50, y1=5))
    ball10.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=10, x1=-55, y1=35))
    ball11.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=11, x1=3, y1=-10))
    ball12.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=12, x1=-20, y1=-20))
    ball13.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=13, x1=-45, y1=-13))
    ball14.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=14, x1=35, y1=-30))
    ball15.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=15, x1=50, y1=-3))
    ball16.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=16, x1=6, y1=-12))
    ball17.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=17, x1=55, y1=-4))
    ball18.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=18, x1=-11, y1=-30))
    ball19.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=19, x1=40, y1=-1))
    ball20.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=20, x1=-55, y1=-40))
    ball21.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=21, x1=-45, y1=-40))
    ball22.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=22, x1=-13, y1=-50))
    ball23.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=23, x1=-16, y1=-55))
    ball24.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=24, x1=16, y1=-35))
    ball25.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=25, x1=25, y1=-45))
    ball26.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=26, x1=8, y1=-34))
    ball27.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=27, x1=17, y1=-52))
    ball28.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=28, x1=50, y1=-25))
    ball29.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=29, x1=-23, y1=-46))
    ball30.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=30, x1=-23, y1=-55))
    ball31.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=31, x1=-100, y1=5))
    ball32.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=32, x1=-125, y1=75))
    ball33.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=33, x1=100, y1=55))
    ball34.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=34, x1=-100, y1=-55))
    ball35.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=35, x1=100, y1=-50))
    ball36.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=36, x1=-75, y1=100))
    ball37.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=37, x1=75, y1=105))
    ball38.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=38, x1=125, y1=-5))
    ball39.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=39, x1=-125, y1=-5))
    ball40.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=40, x1=-98, y1=-25))
    ball41.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=41, x1=15, y1=-40))
    ball42.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=42, x1=-88, y1=-60))
    ball43.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=43, x1=89, y1=-59))
    ball44.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=44, x1=-4, y1=50))
    ball45.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=45, x1=90, y1=-15))
    ball46.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=46, x1=-24, y1=105))
    ball47.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=47, x1=45, y1=100))
    ball48.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=48, x1=-12, y1=-7))
    ball49.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=49, x1=130, y1=-17))
    ball50.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=50, x1=-51, y1=4))
    ball51.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=51, x1=-56, y1=-49))
    ball52.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=52, x1=59, y1=-48))
    ball53.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=53, x1=101, y1=-38))
    ball54.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=54, x1=-99, y1=-9))
    ball55.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=55, x1=-74, y1=78))
    ball56.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=56, x1=88, y1=-16))
    ball57.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=57, x1=-19, y1=102))
    ball58.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=58, x1=-13, y1=-1))
    ball59.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=59, x1=104, y1=-2))
    ball60.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, delay=60, x1=-105, y1=-10))


ani = FuncAnimation(fig,
                    animate,
                    frames=150,
                    interval=30
                    )
ani.save('kipenie(TEST1).gif')
