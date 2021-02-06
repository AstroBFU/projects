import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

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


def circle_move(phi, time):
    if t >= 90:
        a = 0.00001 * 70 * t
    else:
        a = 0.00001 * t
    vy0 = 0.02 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi)
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move1(phi, time):
    if t >= 90:
        a = 0.00001 * 70 * t
    else:
        a = 0.00001 * t
    vy0 = 0.02 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 30
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move2(phi, time):
    if t >= 90:
        a = 0.000016 * 70 * t
    else:
        a = 0.000016 * t
    vy0 = 0.023 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 60
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move3(phi, time):
    if t >= 90:
        a = 0.000018 * 70 * t
    else:
        a = 0.000018 * t
    vy0 = 0.029 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 30
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move4(phi, time):
    if t >= 90:
        a = 0.000014 * 70 * t
    else:
        a = 0.000014 * t
    vy0 = 0.022 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 60
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move5(phi, time):
    if t >= 90:
        a = 0.000011 * 70 * t
    else:
        a = 0.000011 * t
    vy0 = 0.026 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 50
    y = y0 + R * np.sin(phi) + 40
    return x, y


def circle_move6(phi, time):
    if t >= 90:
        a = 0.0000112 * 70 * t
    else:
        a = 0.0000112 * t
    vy0 = 0.0234 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 20
    y = y0 + R * np.sin(phi) + 35
    return x, y


def circle_move7(phi, time):
    if t >= 90:
        a = 0.0000193 * 70 * t
    else:
        a = 0.0000193 * t
    vy0 = 0.0272 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 10
    y = y0 + R * np.sin(phi) + 50
    return x, y


def circle_move8(phi, time):
    if t >= 90:
        a = 0.0000194 * 70 * t
    else:
        a = 0.0000194 * t
    vy0 = 0.0272 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 45
    y = y0 + R * np.sin(phi) + 20
    return x, y


def circle_move9(phi, time):
    if t >= 90:
        a = 0.00001964 * 70 * t
    else:
        a = 0.00001964 * t
    vy0 = 0.02722 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 50
    y = y0 + R * np.sin(phi) + 5
    return x, y


def circle_move10(phi, time):
    if t >= 90:
        a = 0.0000195744 * 70 * t
    else:
        a = 0.0000195744 * t
    vy0 = 0.02672 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 55
    y = y0 + R * np.sin(phi) + 35
    return x, y


def circle_move11(phi, time):
    if t >= 90:
        a = 0.0000192454 * 70 * t
    else:
        a = 0.0000192454 * t
    vy0 = 0.0276262 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 3
    y = y0 + R * np.sin(phi) - 10
    return x, y


def circle_move12(phi, time):
    if t >= 90:
        a = 0.000019744 * 70 * t
    else:
        a = 0.000019744 * t
    vy0 = 0.0272 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 20
    y = y0 + R * np.sin(phi) - 20
    return x, y


def circle_move13(phi, time):
    if t >= 90:
        a = 0.0000193674 * 70 * t
    else:
        a = 0.0000193674 * t
    vy0 = 0.0274672 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 45
    y = y0 + R * np.sin(phi) - 13
    return x, y


def circle_move14(phi, time):
    if t >= 90:
        a = 0.000019446424 * 70 * t
    else:
        a = 0.000019446424 * t
    vy0 = 0.02724235 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 35
    y = y0 + R * np.sin(phi) - 30
    return x, y


def circle_move15(phi, time):
    if t >= 90:
        a = 0.00001937634 * 70 * t
    else:
        a = 0.00001937634 * t
    vy0 = 0.0273672 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 50
    y = y0 + R * np.sin(phi) - 3
    return x, y


def circle_move16(phi, time):
    if t >= 90:
        a = 0.0000193674 * 70 * t
    else:
        a = 0.0000193674 * t
    vy0 = 0.02757632 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 6
    y = y0 + R * np.sin(phi) - 12
    return x, y


def circle_move17(phi, time):
    if t >= 90:
        a = 0.000019284 * 70 * t
    else:
        a = 0.000019284 * t
    vy0 = 0.0273732 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 55
    y = y0 + R * np.sin(phi) - 4
    return x, y


def circle_move18(phi, time):
    if t >= 90:
        a = 0.0000190384 * 70 * t
    else:
        a = 0.0000190384 * t
    vy0 = 0.0279452 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 11
    y = y0 + R * np.sin(phi) - 30
    return x, y


def circle_move19(phi, time):
    if t >= 90:
        a = 0.0000199254 * 70 * t
    else:
        a = 0.0000199254 * t
    vy0 = 0.0282572 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 40
    y = y0 + R * np.sin(phi) - 1
    return x, y


def circle_move20(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 55
    y = y0 + R * np.sin(phi) - 40
    return x, y


def circle_move21(phi, time):
    if t >= 90:
        a = 0.000019272169324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 45
    y = y0 + R * np.sin(phi) - 40
    return x, y


def circle_move22(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 13
    y = y0 + R * np.sin(phi) - 50
    return x, y


def circle_move23(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 16
    y = y0 + R * np.sin(phi) - 55
    return x, y


def circle_move24(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 16
    y = y0 + R * np.sin(phi) - 35
    return x, y


def circle_move25(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 25
    y = y0 + R * np.sin(phi) - 45
    return x, y


def circle_move26(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 8
    y = y0 + R * np.sin(phi) - 34
    return x, y


def circle_move27(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 17
    y = y0 + R * np.sin(phi) - 52
    return x, y


def circle_move28(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 50
    y = y0 + R * np.sin(phi) - 25
    return x, y


def circle_move29(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 23
    y = y0 + R * np.sin(phi) - 46
    return x, y


def circle_move30(phi, time):
    if t >= 90:
        a = 0.000015459279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 23
    y = y0 + R * np.sin(phi) - 55
    return x, y


def circle_move31(phi, time):
    if t >= 90:
        a = 0.000019275479324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 100
    y = y0 + R * np.sin(phi) + 5
    return x, y


def circle_move32(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 125
    y = y0 + R * np.sin(phi) + 75
    return x, y


def circle_move33(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 100
    y = y0 + R * np.sin(phi) + 55
    return x, y


def circle_move34(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 100
    y = y0 + R * np.sin(phi) - 55
    return x, y


def circle_move35(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 100
    y = y0 + R * np.sin(phi) - 50
    return x, y


def circle_move36(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 75
    y = y0 + R * np.sin(phi) + 100
    return x, y


def circle_move37(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 75
    y = y0 + R * np.sin(phi) + 105
    return x, y


def circle_move38(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 125
    y = y0 + R * np.sin(phi) - 5
    return x, y


def circle_move39(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 125
    y = y0 + R * np.sin(phi) - 5
    return x, y


def circle_move40(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 98
    y = y0 + R * np.sin(phi) - 25
    return x, y


def circle_move41(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 15
    y = y0 + R * np.sin(phi) - 40
    return x, y


def circle_move42(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 88
    y = y0 + R * np.sin(phi) - 60
    return x, y


def circle_move43(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 89
    y = y0 + R * np.sin(phi) - 59
    return x, y


def circle_move44(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 4
    y = y0 + R * np.sin(phi) + 50
    return x, y


def circle_move45(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 90
    y = y0 + R * np.sin(phi) - 15
    return x, y


def circle_move46(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 24
    y = y0 + R * np.sin(phi) + 105
    return x, y


def circle_move47(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 45
    y = y0 + R * np.sin(phi) + 100
    return x, y


def circle_move48(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 12
    y = y0 + R * np.sin(phi) - 7
    return x, y


def circle_move49(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 130
    y = y0 + R * np.sin(phi) - 17
    return x, y


def circle_move50(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 51
    y = y0 + R * np.sin(phi) + 4
    return x, y


def circle_move51(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 56
    y = y0 + R * np.sin(phi) - 49
    return x, y


def circle_move52(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 59
    y = y0 + R * np.sin(phi) - 48
    return x, y


def circle_move53(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 101
    y = y0 + R * np.sin(phi) - 38
    return x, y


def circle_move54(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 99
    y = y0 + R * np.sin(phi) - 9
    return x, y


def circle_move55(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 74
    y = y0 + R * np.sin(phi) + 78
    return x, y


def circle_move56(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 88
    y = y0 + R * np.sin(phi) - 16
    return x, y


def circle_move57(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 19
    y = y0 + R * np.sin(phi) + 102
    return x, y


def circle_move58(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 13
    y = y0 + R * np.sin(phi) - 1
    return x, y


def circle_move59(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 104
    y = y0 + R * np.sin(phi) - 2
    return x, y


def circle_move60(phi, time):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 105
    y = y0 + R * np.sin(phi) - 10
    return x, y


edge = 200
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)


def animate(i):
    ball.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball1.set_data(circle_move1(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball2.set_data(circle_move2(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball3.set_data(circle_move3(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball4.set_data(circle_move4(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball5.set_data(circle_move5(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball6.set_data(circle_move6(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball7.set_data(circle_move7(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball8.set_data(circle_move8(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball9.set_data(circle_move9(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball10.set_data(circle_move10(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball11.set_data(circle_move11(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball12.set_data(circle_move12(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball13.set_data(circle_move13(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball14.set_data(circle_move14(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball15.set_data(circle_move15(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball16.set_data(circle_move16(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball17.set_data(circle_move17(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball18.set_data(circle_move18(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball19.set_data(circle_move19(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball20.set_data(circle_move20(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball21.set_data(circle_move21(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball22.set_data(circle_move22(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball23.set_data(circle_move23(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball24.set_data(circle_move24(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball25.set_data(circle_move25(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball26.set_data(circle_move26(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball27.set_data(circle_move27(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball28.set_data(circle_move28(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball29.set_data(circle_move29(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball30.set_data(circle_move30(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball31.set_data(circle_move31(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball32.set_data(circle_move32(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball33.set_data(circle_move33(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball34.set_data(circle_move34(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball35.set_data(circle_move35(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball36.set_data(circle_move36(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball37.set_data(circle_move37(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball38.set_data(circle_move38(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball39.set_data(circle_move39(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball40.set_data(circle_move40(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball41.set_data(circle_move41(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball42.set_data(circle_move42(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball43.set_data(circle_move43(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball44.set_data(circle_move44(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball45.set_data(circle_move45(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball46.set_data(circle_move46(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball47.set_data(circle_move47(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball48.set_data(circle_move48(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball49.set_data(circle_move49(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball50.set_data(circle_move50(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball51.set_data(circle_move51(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball52.set_data(circle_move52(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball53.set_data(circle_move53(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball54.set_data(circle_move54(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball55.set_data(circle_move55(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball56.set_data(circle_move56(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball57.set_data(circle_move57(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball58.set_data(circle_move58(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball59.set_data(circle_move59(phi=np.linspace(0, 2 * np.pi, 50), time=i))
    ball60.set_data(circle_move60(phi=np.linspace(0, 2 * np.pi, 50), time=i))


ani = FuncAnimation(fig,
                    animate,
                    frames=150,
                    interval=30
                    )
ani.save('kipenie.gif')
