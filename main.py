from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

class TextArea(Widget):
    pass

class FightGame(Widget):
    def update(self, delta):
        pass

class FightApp(App):
    def build(self):
        game = FightGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game



FightApp().run()
