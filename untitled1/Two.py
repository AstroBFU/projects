import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Mod import L,z
from CONST import R,h


fig, ax = plt.subplots()
sli, = plt.plot([], [], '-', color="b", lw=6,label="Guillotine")
point, = plt.plot([], [], '-', color="b", lw=0)
ball, = plt.plot([], [], '-', color="m", lw=10)
ball1, = plt.plot([], [], '-', color="m", lw=10,label="Object")
ball2, = plt.plot([], [], '-', color="m", lw=10)
ball6, = plt.plot([], [], '-', color="m", lw=10)
tabel, = plt.plot([], [], "-", lw=8,label="stump")
mas=[]
for g in range(R):
    b, = plt.plot([], [], '-', lw=10, color="m")
    mas.append(b)
x, y = [], []
def slace(x0, h, h1, t):
    by = np.arange(-h, R, 0.01)
    bx = np.arange(-h, h, 1)
    x = x0 + bx
    if t > len(by) - 1:
        t = len(by) - 1
    y = by[t]
    return x, -y
def slace2(x0, h, h1, t):
    by = np.arange(-h, 0, 0.01)
    bx = np.arange(-h,h, 0.1)
    x = x0 + bx
    if t > len(by) - 1:
        t = len(by) - 1
    y = by[t]
    return x, -y
def slace3(x0, h, h1, t):
    by = np.arange(-h, -R, 0.01)
    bx = np.arange(-h, h, 1)
    x = x0 + bx
    if t > len(by) - 1:
        t = len(by) - 1
    y = by[t]
    return x, -y
def blade(x0, y0, R, n, alpha):
    x = R * np.cos(alpha) + x0
    y = R * np.sin(alpha) + y0
    return x, y
def down(x0, y0, R, t):
    alpha = np.arange(0, np.pi * 2, 0.1)
    b1=np.arange(1,100,0.1)
    if t > 130:
        b = np.arange(-9.36, 10, 0.01)
        if t>165:
            b=np.arange(-9.6,200,0.01)
            b=-b
            if t>178:
                alpha=0
    else:
        b = np.arange(0.6, 10, 0.01)
    y = R * np.sin(alpha)
    x = R * np.cos(alpha)
    X = (R * np.sin(alpha) / 1.6) - (R * np.cos(alpha) / 1.6)#(R*(1/np.tan(b1[t]))) #Летающая тарелка
    Y = x * (1 / np.tan(b[t])) + y * (1 / np.tan(b[t])) + y0
    return X, Y
def up(x0, y0, R, t):
    alpha = np.arange(0, np.pi * 2, 0.1)
    b1=np.arange(1,100,0.1)
    if t > 130:
        b = np.arange(-9.36, 10, 0.01)
        if t>165:
            b=np.arange(-9.6,200,0.01)
            b=-b
            if t>178:
                alpha=0
    else:
        b = np.arange(0.6, 10, 0.01)
    y = R * np.sin(alpha)
    x = R * np.cos(alpha)
    X = (R * np.sin(alpha) / 1.6) - (R * np.cos(alpha) / 1.6)#(R*(1/np.tan(b1[t]))) #Летающая тарелка
    Y = x * (1 / np.tan(b[t])) + y * (1 / np.tan(b[t])) + y0
    return X, Y
def ok(x0, y0, R):
    alpha = np.arange(0, np.pi, 0.1)
    y = R * np.sin(alpha) + y0
    x = R * np.cos(alpha)
    return x, -y
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
def slace1(x0, h, t):
    bx = np.arange(-h, h, 1)
    x = x0 + bx
    y = R
    return x, -y
edge = 12+h
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
        if y[i] < -R:
            y[i] = -L
            ball.set_data(blade(x0=0, y0=0, R=100000, n=1, alpha=np.arange(0, 2 * np.pi, 0.1)))
            ball1.set_data(down(x0=0, y0=0, R=R+1 , t=i * 2))
            ball6.set_data(ok(x0=0, y0=0, R=R))
    if z==1:
        sli.set_data(slace2(x0=0, h=h, h1=L, t=i * 100))
        tabel.set_data(slace1(x0=0, h=h, t=i))
        if y[i] < -R:
            y[i] = -L
            ball.set_data(blade(x0=0, y0=0, R=100000, n=1, alpha=np.arange(0, 2 * np.pi, 0.1)))
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
ani.save("Two1.gif")

