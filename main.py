from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.button import Button
import numpy as np
import interaction as inter
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 600)

class Object(Widget):
    def __init__(self, **kw):
        super(Object, self).__init__()
        self.step = kw['step']
        self.pos_x = kw['pos'][0]
        self.pos_y = kw['pos'][1]
        self.vel_vx = kw['vel'][0]
        self.vel_vy = kw['vel'][1]
        self.count = kw['count']
        self.color = kw['color']

        self.COORDS_X = np.ndarray((self.step, self.count))
        self.COORDS_Y = np.ndarray((self.step, self.count))

        self.interect = inter.Interaction(x0=self.pos_x,
                                      vx0=self.vel_vx,
                                      y0=self.pos_y,
                                      vy0=self.vel_vy)

        print('Particle number: ', self.count)
        print('solve_func', self.interect.solve_func(self.count)[0])
        print('solve_func[0][0]', self.interect.solve_func(self.count)[0][0])

        for j in range(self.step):
            for k in range(self.count):
                self.COORDS_X[j, k] = float(self.interect.solve_func(self.count)[0][k])
                self.COORDS_Y[j, k] = float(self.interect.solve_func(self.count)[1][k])


    def draw(self):
        self.canvas.add(Color(1., 1., 1, 1))
        for i in range(self.count):
          self.ellipse = Ellipse(pos=(self.pos_x[i],self.pos_y[i]), size=(inter.r, inter.r))
          self.canvas.add(self.ellipse)

    def move(self, c):
      for i in range(self.count):
          cord = (self.COORDS_X[c, i], self.COORDS_Y[c, i])
          print(type(cord))
          self.pos = Vector(cord)
          self.ellipse.pos = self.pos


class Move(Widget):
    def __init__(self, count):
        super(Move, self).__init__()
        self.n = inter.n
        self.counter = 0
        self.count = count

    def update(self, dt):
        if self.counter == self.n - 1:
            self.counter = 0
        self.counter += 1
        self.object.move(self.counter)

    def create(self, color, pos, vel):
        self.object = Object(key=True,
                            color=color,
                            step=self.n,
                            pos=pos,
                            vel=vel,
                            count=self.count)

        self.object.draw()
        self.add_widget(self.object)

class Painter(Widget):
    def __init__(self, **kw):
      super(Painter, self).__init__(**kw)
      self.count = 0
      self.X = []
      self.Y = []
      self.VX = []
      self.VY = []


    def on_touch_move(self, touch):
        with self.canvas:
          Ellipse(pos=(touch.x, touch.y), size=(3,3))
          self.count += 1
          self.X.append(touch.x*10**6)
          self.Y.append(touch.y*10**6)
          self.VX.append(touch.y*0)
          self.VY.append(touch.y*0)

    def on_touch_up(self, touch):
        with self.canvas:
          Ellipse(pos=(touch.x, touch.y), size =(3,3))
          self.object = Move(count=self.count)
          self.object.create(color=(1,1,1,1),
                          pos=(self.X, self.Y),
                          vel=(self.VX, self.VY))
          Clock.schedule_interval(self.object.update, .04)
          self.parent.add_widget(self.object)

class SupernovaApp(App):

    def build(self):
        return Painter()

if __name__ == '__main__':
    SupernovaApp().run()
