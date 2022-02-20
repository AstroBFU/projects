import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Solver:
    def __init__(self, data_objects ):
        self.data_objects = data_objects
        self.data = sum(data_objects, [])


        self.G = 6.67 * 10 ** (-11)
        self.k = 8.98755 * 10 ** 9



        self.variable = []
        self.not_variable_balls =[]

      
        self.N = int(len(self.data_objects))

        # Лист не изменяемых данных моделируемых объектов
        # Период = 2
        # Данные одного моделируемого объекта: 0 = масса, 1 = заряд
        
        # Лист изменяемых данных моделируемых объектов
        # Период = 4
        # Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y
        

    """
    ################### Логика построения list[n * a + b] ###################
    n - элемент который мы хотим получить
    a - период list
    Период - это количесво вставляемых подряд данных одного объекта моделирования в определённый лист
    b - какие данные элемента мы хотим получить
    """
    def ball( self  ):
      """
      Распределяет данные моделируемых объктов по листам
      :param mas: масса
      :param electric_charge: электрический заряр
      :param x: координата x
      :param v_x: вектор по x
      :param y: координата y
      :param v_y: вектор по y
      """

      for i in range(self.N):
        # 0 mas, 1 electric_charge, 2 x, 3 v_x, 4 y,5 v_y
        self.not_variable_balls.append(self.data[i*6+0])
        self.not_variable_balls.append(self.data[i*6+1])
        self.variable.append(self.data[i*6+2])
        self.variable.append(self.data[i*6+3])
        self.variable.append(self.data[i*6+4])
        self.variable.append(self.data[i*6+5])
        
      return self.variable, self.not_variable_balls


    def get_dv_dt(self, num, key):
        """
        :param variable_balls - все объекты моделирования
        :param num - номер объекта на который дейсвуют другие тела
        :param key - компонента скорость 'vx' или 'vy'
        :return out: взаимодействие variable_balls элементов на num-ый элемент по x
        """

        out = 0.0
        
        a = self.ball()
        
        v = a[0]
        nv= a[1]
        
        if key == 'vx':
            component = 0
        else:
            component = 2

        for i in range(self.N):
            if i != num:
                # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
                out += (-self.G *nv[i * 2 + 0] *
                        (v[num * 4 + component] - v[i * 4 + component]) /
                        ((v[num * 4 + 0] - v[i * 4 + 0]) ** 2 + (
                                v[num * 4 + 2] - v[i * 4 + 2]) ** 2) ** 1.5)

                # Вычисляем взаимодействие заряженных тел variable_balls элементов на num-ый элемент
                out += (self.k *
                        nv[num * 2 + 1] * nv[i * 2 + 1] /
                        nv[num * 2 + 0] *
                        (v[num * 4 + component] - v[i * 4 + component]) /
                        ((v[num * 4 + 0] - v[i * 4 + 0]) ** 2 + (
                                v[num * 4 + 2] - v[i * 4 + 2]) ** 2) ** 1.5)
        return out

  
    def euler(self, step=0.1, frame = 50 ):
      x_all= []
      y_all= []
      a = self.ball()
      v = a[0]
      
      for j in range(self.N):
          x0 = v[j*4 + 0]
          y0 = v[j*4 + 1]
          vx0 = v[j*4 + 2]
          vy0 = v[j*4 + 3]

            
          x = x0  
          y= y0
          vx = vx0
          vy = vy0
          
          x_list = [x]
          y_list = [y]
          
          for _ in range(frame):
              x = x + step * vx
              vx = vx + step * self.get_dv_dt( j, 'vx')
              y = y + step * vy
              vy = vy + step * self.get_dv_dt( j, 'vy')
              x_list.append(x)
              y_list.append(y)
            
          x_all.append(x_list)
          y_all.append(y_list)
          
      return x_all, y_all
    def solve_func(self, i, n, key):
        """
        :param i: время в которое мы берём координаты
        :param n: номер моделируемого объекта для которого мы получаем координаты
        :param key: ключ. Если point то получам координаты для моделирования точьки
            в ином случае получае координаты для моделирования пути моделирукмого объекта
        :return x, y: n-го моделируемого элемента в i-е время
        """
        sol = self.euler()
        sol_x = sol[0]
        sol_y = sol [1]
        if key == "point":
            x = sol_x[  n ]
            y = sol_y[  n ]
        else:
            x = sol_x[n ]
            y = sol_y[ n ]
  
        return x, y

  

list1 = [ 1.1 * 10 ** 30, 1.1 * 10 ** 20, 149 * 10 ** 8, 0, 0, 30000]
list2 = [2.1 * 10 ** 30, 2.1 * 10 ** 20, - 149 * 10 ** 8, 1, 0, -30000]
        
balls = Solver ([list1, list2])
balls.get_dv_dt(1, 'vx')

fig, ax = plt.subplots()
      # Лист графических элементов моделируемых объектов
      # Период = 2
      # Данные одного моделируемого объекта: 0 = шар, 1 = путь
plots = []
      # Создаём для каждего моделируемого объекта графические элементы
for i in range(balls.N):
    # создаём рандомный цвет
    colors = np.random.rand(3, )
    # создаём графический элемент "шар"
    plot, = plt.plot([], [], 'o', c=colors, ms=5)
    plots.append(plot)
    # создаём графический элемент "линия"
    plot2, = plt.plot([], [], '-', c=colors)
    plots.append(plot2)
  
def animate(i):
  for j in range(balls.N):
      plots[j * 2 + 0].set_data(balls.solve_func(i, j, 'point'))
      plots[j * 2 + 1].set_data(balls.solve_func(i, j, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=500,
                    interval=30)
plt.axis('equal')
edge = 2 * 300 * 10 ** 8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.show()