import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Solver:
    def __init__(self, data_objects):
        self.data_objects = data_objects

        self.frame = 5000
        seconds_in_year = 365 * 24 * 60 * 60
        years = 0.1
        self.t = np.linspace(0, years * seconds_in_year, frame)

        G = 6.67 * 10 ** (-11)
        k = 8.98755 * 10 ** 9
        N = 0

        # Лист не изменяемых данных моделируемых объектов
        # Период = 2
        # Данные одного моделируемого объекта: 0 = масса, 1 = зарят
        self.not_variable_balls = []

        # Лист изменяемых данных моделируемых объектов
        # Период = 4
        # Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y
        self.variable = []

    """
    ################### Логика построения list[n * a + b] ###################
    n - элемент который мы хотим получить
    a - период list
    Период - это количесво вставляемых подрят данных одного объекта моделирования в определённый лист
    b - какие данные элемента мы хотим получить
    """


    def get_dv_dt(self, variable_balls, num, key):
        """
        :param variable_balls - все объекты моделирования
        :param num - номер объекта на который дейсвуют другие тела
        :param key - компонента скорость 'vx' или 'vy'
        :return out: взаимодействие variable_balls элементов на num-ый элемент по x
        """

        out = 0.0

        if key == 'vx':
            component = 0
        else:
            component = 2

        for i in range(N):
            if i != num:
                # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
                out += (-G * not_variable_balls[i * 2 + 0] *
                        (variable_balls[num * 4 + component] - variable_balls[i * 4 + component]) /
                        ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                                variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)

                # Вычисляем взаимодействие заряженных тел variable_balls элементов на num-ый элемент
                out += (k *
                        not_variable_balls[num * 2 + 1] * not_variable_balls[i * 2 + 1] /
                        not_variable_balls[num * 2 + 0] *
                        (variable_balls[num * 4 + component] - variable_balls[i * 4 + component]) /
                        ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                                variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)
        return out

    def move_func(variable, t):
        """
        :param variable: все изменияемые данные объектов моделирования
        :param t: linspace переода времяни
        :return: outs: решение диференциального уравнения
        """

        # Лист возвращяемых данных
        # Период = 4
        # Элементы объекта: 0 = dxdt, 1 = dv_xdt, 2 = dydt, 3 = dv_ydt
        outs = []

        # Для каждего моделируемого объекта вычислем возвращяемые даннные
        for j in range(N):
            # Вычисляем dxdt
            outs.append(variable[j * 4 + 1])
            # Вычисляем dv_xdt
            outs.append(self.get_dv_dt(variable, j, 'vx'))
            # Вычисляем dydt
            outs.append(variable[j * 4 + 3])
            # Вычисляем dv_ydt
            outs.append(get_dv_dt(variable, j, 'vy'))

        return outs





    def ball(self, mas, electric_charge, x, v_x, y, v_y):
        """
        Распределяет данные моделируемых объктов по листам
        :param mas: масса
        :param electric_charge: электрический заряр
        :param x: координата x
        :param v_x: вектор по x
        :param y: координата y
        :param v_y: вектор по y
        """
        self.not_variable_balls.append(mas)
        not_variable_balls.append(electric_charge)
        variable.append(x)
        variable.append(v_x)
        variable.append(y)
        variable.append(v_y)


    # Добавляем объекты моделирования
    # [[x0, vx0, y0, vy0, m0, q0],
    #  [x1, vx1, y1, vy0, m0, q0],
    #  [x1, vx1, y1, vy0, m0, q0]]

    def data_func(self):
        for i in range(len(self.data_objects)):
            for j in range(6):
                self.ball(self.data_objects[i, j])
        # ball(1.1 * 10 ** 30, 1.1 * 10 ** 20, 149 * 10 ** 8, 0, 0, 30000)
        # ball(2.1 * 10 ** 30, 2.1 * 10 ** 20, - 149 * 10 ** 8, 1, 0, -30000)
        # ball(3.6 * 10 ** 30, -3.1 * 10 ** 20, 0, 15000, 149 * 10 ** 8, 0)
        # ball(7 * 10 ** 30, -2.6 * 10 ** 20, 0, 0, 0, 0)
        # ball(7 * 10 ** 30, -2.6 * 10 ** 20, 349 * 10 ** 8, 0, 0, 0)

    # Вычесляем сколько всего мы моделируем объектов
    N = int(len(not_variable_balls) / 2)

    # Моделируем
    sol = odeint(move_func, variable, t)

    def odeint_eiler(self):
        x0 = []
        for i in range(len(self.data_objects)):
            x0.append(self.move_func(self.variable, self.t)[j * 4 + 1])

        for i in range(len(self.t)):
            x1 = x0 + t[i] * vx0
            vx1 = vx0 + t[i] * self.get_dv_dt(vx0, j, 'vx')
            y1 = y0 + t[i] * vy0
            vy1 = vy0 + t[i] * self.get_dv_dt(vy0, j, 'vx')

            x0 = x1
            vx0 = vx1
            y0 = y1
            vy0 = vy1

        return x, y

        # x = [[x1ball1, x2ball1, ..., x5000ball1],
        #      [x1ball2, x2ball2, ..., x5000ball2]]
        
    def solve_func(i, n, key):
        """
        :param i: время в которое мы берём координаты
        :param n: номер моделируемого объекта для которого мы получаем координаты
        :param key: ключь. Если point то получам координаты для моделирования точьки
            в ином случае получае координаты для моделирования пути моделирукмого объекта
        :return x, y: n-го моделируемого элемента в i-е время
        """

        if key == "point":
            x = sol[i, n * 4 + 0]
            y = sol[i, n * 4 + 2]
        else:
            x = sol[:i, n * 4 + 0]
            y = sol[:i, n * 4 + 2]

        return x, y


'''
fig, ax = plt.subplots()

# Лист графических элементов моделируемых объектов
# Переод = 2
# Данные одного моделируемого объекта: 0 = шар, 1 = путь
plots = []

# Создаём для каждего моделируемого объекта графические элементы
for i in range(N):
    # создаём рандомный цвет
    colors = np.random.rand(3, )

    # создаём графический элемент "шар"
    plot, = plt.plot([], [], 'o', c=colors, ms=5)
    plots.append(plot)

    # создаём графический элемент "лия"
    plot2, = plt.plot([], [], '-', c=colors)
    plots.append(plot2)


def animate(i):
    """
    Моделируем для каждего моделируемого объека графические элементы
    :param i: время в которое мы берём координаты
    """

    for j in range(N):
        plots[j * 2 + 0].set_data(solve_func(i, j, 'point'))
        plots[j * 2 + 1].set_data(solve_func(i, j, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=500,
                    interval=30)

plt.axis('equal')
edge = 2 * 300 * 10 ** 8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
'''
