import pygame as pg # Module required to use the PyGame assets
import sys

# Details for modules used above:
# sys - https://docs.python.org/3/library/sys.html
# pygame - https://pypi.org/project/pygame/

from settings import * # Creates and link to the settings.py file
from map import * # Creates a link to the map.py file
from player import *
from raycasting import *
from object_renderer import *

# Main class below.
class Game:
    def __init__(self):
    # def: This keyword is used to define a function or method.
    # __init__: This is the name of the special method that serves as the constructor.
    # (self): The self parameter is a reference to the instance of the class. It allows you to refer to the instance's attributes and methods within the class.
        pg.init()
        self.screen = pg.display.set_mode(RES) # This sets the resolution set out in the settings.py file.
        self.clock = pg.time.Clock() # This controls the frame rate
        self.delta_time = 1 # Delta Time is the amount of time that has passed since the last frame
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'cDoom FPS: {self.clock.get_fps() :.1f}') # This shows the FPS on the bar at the top of the Window

    def draw(self):
        self.screen.fill('black') # This controls the background colour
        self.object_renderer.draw()
        #self.map.draw() # This draws the map from map.py
        #self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()