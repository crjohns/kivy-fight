from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics','resizable',0)


game = None

class Person:
    name = ""
    color = "ffffff"
    health = 100.0

    def isDead(self):
        return self.health < 1

    def hit_by(self, other):
        val = randint(1,20)
        self.health = max(0,self.health - val)
        game.log("%s hit %s for %d\n%s" % (other.color_name(), self.color_name(), val, str(self)))

    def __str__(self):
        return "[color=%s][%s][/color] Health: %d" % (self.color, self.name, int(self.health))

    def color_name(self):
        return "[color=%s]%s[/color]" % (self.color, self.name)
        

class Player(Person):

    def __init__(self):
        self.name = "YOU"
        self.color = "00ff00"

class Enemy(Person):
    def __init__(self):
        self.name = "ENEMY"
        self.color = "ff0000"


class FightGame(Widget):

    console = ObjectProperty(None)
    attack = ObjectProperty(None)

    def update(self, delta):
        pass

    def log(self, *args):
        self.console.text += "\n"
        for arg in args:
            self.console.text += str(arg)

    def isGameOver(self):
        return self.player.isDead() or self.enemy.isDead()

    def press_attack(self, btn):
        if self.isGameOver():
            return

        self.enemy.hit_by(self.player)
        if self.enemy.isDead():
            self.log("%s killed %s!" % (self.player.color_name(), self.enemy.color_name()))
        else:
            self.player.hit_by(self.enemy)

        if self.player.isDead():
            self.log("%s killed %s!" % (self.enemy.color_name(), self.player.color_name()))


class FightApp(App):
    def build(self):
        global game
        game = FightGame()
        game.player = Player()
        game.enemy = Enemy()
        game.log(game.player)
        game.log("An enemy appears!\n", game.enemy)
        Clock.schedule_interval(game.update, 1.0/60.0)

        return game



FightApp().run()
