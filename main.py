
"""
Проект Сверхновая звезда. По умолчанию в центре генерируется массивное тело. 
Пользователь на экране рисует окружность, которая после отпускания кнопки мыши (убирания пальца с экрана),
начинает падать на массивное тело (ядро).
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.button import Button

class Object(Widget):

    def __init__(self, **kw):
        super(Object, self).__init__()

        self.step = kw['step']
        self.color = kw['color']
        self.pos = kw['pos']
        self.size = kw['size']

        # ------------- odein ---------------------
        self.coords = []
        a = randint(0, 15)
        b = randint(10, 20)
        for i in range(self.step):
            self.coords.append((self.pos[0]+a*i, self.pos[1]+i**(b*0.1)))
        # ------------- odein ---------------------

    def draw(self):
        self.canvas.add(self.color)
        self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.canvas.add(self.ellipse)

    def move(self, i):
        self.pos = Vector(self.coords[i])
        self.ellipse.pos = self.pos


class Move(Widget):

    def __init__(self, N):
        super(Move, self).__init__()
        self.counter = 0
        self.n = N

    def update(self, dt):
        if self.counter == self.n-1:
            self.counter = 0
        self.counter += 1
        self.object.move(self.counter)

    def create(self, color, pos, size):
        self.object = Object(step=self.n, color=color, pos=pos, size=size)
        self.object.draw()
        self.add_widget(self.object)


class PlanetApp(App):

    def create_object(self, instance):
        self.object = Move(1000)
        self.object.create(color=Color(1, 0, 0), pos=(0, 250), size=(50, 50))
        Clock.schedule_interval(self.object.update, 0.1)
        self.parent.add_widget(self.object)

    def build(self):
        self.parent = Widget()
        btn = Button(text='Create')
        btn.bind(on_press=self.create_object)
        self.parent.add_widget(btn)

        return self.parent

if __name__ == '__main__':
    PlanetApp().run()
