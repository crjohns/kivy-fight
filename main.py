from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')


class Person:
    health = 100.0

    def isDead(self):
        return self.health < 1

class Player(Person):
    def __str__(self):
        return "[color=00ff00][YOU][/color] Health: " + str(int(self.health))

class Enemy(Person):
    def __str__(self):
        return "[color=ff0000][ENEMY][/color] Health: " + str(int(self.health))


class FightGame(Widget):

    console = ObjectProperty(None)

    def update(self, delta):
        pass

    def log(self, *args):
        self.console.text += "\n"
        for arg in args:
            self.console.text += str(arg)


class FightApp(App):
    def build(self):
        game = FightGame()
        game.player = Player()
        game.enemy = Enemy()
        game.log(game.player)
        game.log("An enemy appears!\n", game.enemy)
        Clock.schedule_interval(game.update, 1.0/60.0)

        return game



FightApp().run()
