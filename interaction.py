import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from scipy.integrate import odeint

M = 1 # Масса ядра в Солнечных массах
R = 0.5  # Радиус ядра в Солнечных радиусах
G = 6.67430 * 10**(-11)
m_sun = 1.989*10**30
R_sun = 696340*10**3
r = 3
T = 2000 # Время анимации в секундах (соответствует примерно реальному времени коллапса оболочки)
n = 5  # Число шагов / кадров

tau = np.linspace(0,T,n) # Массив для одного временного шага


class Interaction:
    def __init__(self, x0, vx0, y0, vy0):
        self.x0 = x0
        self.vx0 = vx0
        self.y0 = y0
        self.vy0 = vy0
        # print('передача начальных значений')
        # print(self.x0)
        # print(self.y0)

    def move_func(self, s, t):
        # print('передача в решатель')
        # print(s)
        x, v_x, y, v_y = s

        # Система диф. уравнений на базе второго закона Ньютона
        g = G * m_sun * M / (R_sun**2*(x**2 + y**2))

        dxdt = v_x
        dv_xdt = - g * x / (R_sun * np.sqrt(x**2 + y**2))

        dydt = v_y
        dv_ydt = - g * y / (R_sun * np.sqrt(x**2 + y**2))

        return dxdt, dv_xdt, dydt, dv_ydt

    def collision(self,x1, vx1, y1, vy1, x2, vx2, y2, vy2, radius1, radius2, mass1, mass2, K):
        """Аргументы функции:
        x1,y1,vx1,vy1 - координаты и компоненты скорости 1-ой частицы
        x2,y2,vx2,vy2 - ... 2-ой частицы
        radius,mass1,mass2 - радиус частиц и их массы (массы разные можно задавать,
        радиус для простоты взят одинаковый)
        K - коэффициент восстановления (K=1 для абсолютного упругого удара, K=0
        для абсолютно неупругого удара, 0<K<1 для реального удара).
        В данном случае коэффициент ВАЖНО положить больше 1, чтобы учесть дополнительную
        кенетическую энергию, возникающую в результате взрыва.
        Функция возвращает компоненты скоростей частиц, рассчитанные по формулам для
        реального удара, если стокновение произошло. Если удара нет, то возвращаются
        те же значения скоростей, что и заданные в качестве аргументов.
        """
        r12 = np.sqrt((x1-x2)**2 + (y1-y2)**2) #расчет расстояния между центрами частиц
        # расчет модулей скоростей частиц
        v1 = np.sqrt(vx1**2 + vy1**2)
        v2 = np.sqrt(vx2**2 + vy2**2)

        #проверка условия на столкновение: расстояние должно быть меньше 2-х радиусов
        if r12 <= radius1 + radius2:
            '''вычисление углов движения частиц theta1(2), т.е. углов между
            направлением скорости частицы и положительным направлением оси X.
            Если частица  покоится, то угол считается равным нулю. Т.к. функция
            arccos имеет область значений от 0 до Pi, то в случае отрицательных
            y-компонент скорости для вычисления угла theta1(2) надо из 2*Pi
            вычесть значение arccos(vx/v)
            '''
            if v1!=0:
                theta1 = np.arccos(vx1 / v1)
            else:
                theta1 = 0
            if v2!=0:
                theta2 = np.arccos(vx2 / v2)
            else:
                theta2 = 0
            if vy1<0:
                theta1 = - theta1 + 2 * np.pi
            if vy2<0:
                theta2 = - theta2 + 2 * np.pi

            #вычисление угла соприкосновения.
            if (y1-y2)<0:
                phi = - np.arccos((x1-x2) / r12) + 2 * np.pi
            else:
                phi = np.arccos((x1-x2) / r12)

            # Пересчет  x-компоненты скорости первой частицы
            VX1 = v1 * np.cos(theta1 - phi) * (mass1 - K * mass2) \
            * np.cos(phi) / (mass1 + mass2)\
            + ((1 + K) * mass2 * v2 * np.cos(theta2 - phi))\
            * np.cos(phi) / (mass1 + mass2)\
            + K * v1 * np.sin(theta1 - phi) * np.cos(phi + np.pi / 2)

            # Пересчет y-компоненты скорости первой частицы
            VY1 = v1 * np.cos(theta1 - phi) * (mass1 - K * mass2) \
            * np.sin(phi) / (mass1 + mass2) \
            + ((1 + K) * mass2 * v2 * np.cos(theta2 - phi)) \
            * np.sin(phi) / (mass1 + mass2) \
            + K * v1 * np.sin(theta1 - phi) * np.sin(phi + np.pi / 2)

            # Пересчет x-компоненты скорости второй частицы
            VX2 = v2 * np.cos(theta2 - phi) * (mass2 - K * mass1) \
            * np.cos(phi) / (mass1 + mass2)\
            + ((1 + K) * mass1 * v1 * np.cos(theta1 - phi)) \
            * np.cos(phi) / (mass1 + mass2)\
            + K * v2 * np.sin(theta2 - phi) * np.cos(phi + np.pi / 2)

            # Пересчет y-компоненты скорости второй частицы
            VY2 = v2 * np.cos(theta2 - phi) * (mass2 - K * mass1) \
            * np.sin(phi) / (mass1 + mass2) \
            + ((1 + K) * mass1 * v1 * np.cos(theta1 - phi)) \
            * np.sin(phi) / (mass1 + mass2)\
            + K * v2 * np.sin(theta2 - phi) * np.sin(phi + np.pi / 2)

        else:
            #если условие столкновнеия не выполнено, то скорости частиц не пересчитываются
            VX1, VY1, VX2, VY2 = vx1,vy1,vx2,vy2

        return VX1, VY1, VX2, VY2


    def solve_func(self, N):

    # Решение задачи и проверка условий столковения
      self.X = []
      self.Y = []
      for k in range(0,n-1,1):
          t=[tau[k],tau[k+1]]
          for i in range(N):

              self.s0 = self.x0[i], 0, self.y0[i], 0
              sol = odeint(self.move_func, self.s0, t)

              self.x0[i] = sol[1,0]
              self.vx0[i] = sol[1,1]
              self.y0[i] = sol[1,2]
              self.vy0[i] = sol[1,3]

              res = self.collision(self.x0[i] ,self.vx0[i], self.y0[i],self.vy0[i], 0, 0, 0,0, 0.01, 0.5, 0, 1, 2)
              self.vx0[i], self.vy0[i] = res[0], res[1]

              self.X.append(self.x0[i]/(10**6))
              self.Y.append(self.y0[i]/(10**6))

      return self.X, self.Y
