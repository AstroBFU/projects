import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Mod import L, D,z
from CONST import R,h
fig, ax = plt.subplots()
sli, = plt.plot([], [], '-', color="b", lw=5,label="Guillotine")
point, = plt.plot([], [], '-', color="b", lw=0)
point1, = plt.plot([], [], '-', color="b", lw=5)
ball, = plt.plot([], [], '-', color="m", lw=10,label="Object")
ball1, = plt.plot([], [], '-', color="m", lw=10)
ball2, = plt.plot([], [], '-', color="m", lw=10)
x, y = [], []
x1, y1 = [], []
tabel, = plt.plot([], [], "-", lw=8,label="stump")
def slace(x0, h, h1, t):
    d = 0
    by = np.arange(-h, R, 0.01)
    bx = np.arange(-0.1, 0.2, 0.1)
    x = x0 + bx
    if t > len(by) - 1:
        t = len(by) - 1
    x1.append(t * 0)
    y1.append(-by[t])
    for g in np.arange(-h, h1, 0.01):
        if d < 1:
            point1.set_data(x1, y1)
            d += 1
    y = by[t]
    return x, -y
def slace2(x0, h, h1, t):
    d = 0
    by = np.arange(-h, 0, 0.01)
    bx = np.arange(-0.1, 0.2, 0.1)
    x = x0 + bx
    if t > len(by) - 1:
        t = len(by) - 1
    x1.append(t * 0)
    y1.append(-by[t])
    for g in np.arange(-h, h1, 0.01):
        if d < 1:
            point1.set_data(x1, y1)
            d += 1
    y = by[t]
    return x, -y
def slace3(x0, h, h1, t):
    d=0
    by = np.arange(-h, -R, 0.01)
    bx = np.arange(-0.1, 0.2, 1)
    x = x0 + bx
    if t > len(by) - 1:
        t = len(by) - 1
    x1.append(t * 0)
    y1.append(-by[t])
    for g in np.arange(-h, h1, 0.01):
        if d < 1:
            point1.set_data(x1, y1)
            d += 1

    y = by[t]
    return x, -y
def slace1(x0, h, t):
    bx = np.arange(-h, h, 1)
    by = np.arange(5, 11, 0.1)
    x = x0 + bx
    y = R
    return x, -y
def blade(x0, y0, R, n, alpha):
    x = R * np.cos(alpha) + x0
    y = R * np.sin(alpha) + y0
    return x, y
def blade1(x0, y0, R, n, t):
    alpha = np.arange(np.pi * (3 / 2), np.pi * (5 / 2), 0.1)
    b = np.arange(0, np.pi, 0.01) * 1.5
    if t > 100:
        y = R * np.sin(alpha)
        x = R * np.cos(alpha)
    else:
        x = R * np.cos(alpha)
        y = R * np.sin(alpha) + y0
    if t > 100:
        b = np.arange(np.pi * (4 / 6), np.pi * (3 / 2), 0.01) * 1.5
        b = -b
    if t > 120:
        b = np.arange(-np.pi * (3 / 2), np.pi * (1 / 2), 0.01) * 1.4
    if t > 140:
        b = np.arange(np.pi * (1 / 2), np.pi, 0.01) * 1.55
        b = -b
    else:
        b = b
    if t > 100:
        X = x * np.cos(b[t]) - y * np.sin(b[t]) + x0
    else:
        X = x * np.cos(b[t]) - y * np.sin(b[t])
    Y = y * np.cos(b[t]) + x * np.sin(b[t])
    if t > 20:
        by = np.arange(-5, 0, 0.1)
        if t > len(by) - 1:
            t = len(by) - 1
        Y = Y - by[t]
    else:
        Y = Y + R
    return -X, -Y
def blade2(x0, y0, R, n, t):
    alpha = np.arange(np.pi * (3 / 2), np.pi * (5 / 2), 0.1)
    b = np.arange(0, np.pi, 0.01) * 1.5
    if t > 100:
        y = R * np.sin(alpha)
        x = R * np.cos(alpha)
    else:
        x = R * np.cos(alpha)
        y = R * np.sin(alpha) + y0
    if t > 100:
        b = np.arange(np.pi * (4 / 6), np.pi * (3 / 2), 0.01) * 1.5
        b = -b
    if t > 120:
        b = np.arange(-np.pi * (3 / 2), np.pi * (1 / 2), 0.01) * 1.4
    if t > 140:
        b = np.arange(np.pi * (1 / 2), np.pi, 0.01) * 1.55
        b = -b
    else:
        b = b
    if t > 100:
        X = x * np.cos(b[t]) - y * np.sin(b[t]) + x0
    else:
        X = x * np.cos(b[t]) - y * np.sin(b[t])
    Y = y * np.cos(b[t]) + x * np.sin(b[t])
    if t > 20:
        by = np.arange(-5, 0, 0.1)
        if t > len(by) - 1:
            t = len(by) - 1
        Y = Y - by[t]
    else:
        Y = Y + R
    return X, -Y
def blade4(x0, y0, R, n, t):
    alpha = np.arange(np.pi * (5 / 4), np.pi * (5 / 2), 0.1)
    b = np.arange(0, np.pi, 0.03) / 1.55
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    X = x * np.cos(b[t]) - y * np.sin(b[t]) + x0
    Y = y * np.cos(b[t]) + x * np.sin(b[t]) + y0
    return -X, -Y
def blade3(x0, y0, R, n, t):
    alpha = np.arange(np.pi * (5 / 4), np.pi * (5 / 2), 0.1)
    b = np.arange(0, np.pi, 0.03) / 1.55
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    X = x * np.cos(b[t]) - y * np.sin(b[t]) + x0
    Y = y * np.cos(b[t]) + x * np.sin(b[t]) + y0
    return X, -Y
edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(i):
    ball.set_data(blade(x0=0, y0=0, R=R, n=1, alpha=np.arange(0, 2 * np.pi, 0.1)))
    x.append(i * 0)
    y.append(h + (-i))
    point.set_data(x, y)
    if z==0:
        sli.set_data(slace(x0=0, h=h, h1=L, t=i * 100))
        tabel.set_data(slace1(x0=0, h=h, t=i))
        if y[i] <-R:
            y[i] = -L
            ball.set_data(blade(x0=0, y0=0, R=1000, n=1, alpha=np.arange(0, 2 * np.pi, 0.1)))
            ball1.set_data(blade1(x0=5, y0=-5, R=R, n=1, t=i * 2))
            ball2.set_data(blade2(x0=5, y0=-5, R=R, n=1, t=i * 2))
    if z==1:
        sli.set_data(slace2(x0=0, h=h, h1=L, t=i * 100))
        tabel.set_data(slace1(x0=0, h=h, t=i))
        if y[i] <-R:
            y[i] = -L
            ball.set_data(blade(x0=0, y0=0, R=1000, n=1, alpha=np.arange(0, 2 * np.pi, 0.1)))
            ball1.set_data(blade3(x0=0, y0=0, R=R, n=1, t=i))
            ball2.set_data(blade4(x0=0, y0=0, R=R, n=1, t=i))
    if z==2:
        sli.set_data(slace3(x0=0, h=h, h1=L, t=i * 100))
        print("не разрезал")
ani = FuncAnimation(fig,
                    animate,
                    frames=100,
                    interval=100)
plt.legend()
plt.show()