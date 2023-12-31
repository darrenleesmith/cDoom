import pygame as pg # Module required to use the PyGame assets
import sys

# Details for modules used above:
# sys - https://docs.python.org/3/library/sys.html
# pygame - https://pypi.org/project/pygame/

from settings import * # Creates and link to the settings.py file
from map import * # Creates a link to the map.py file

# Main class below.
class Game:
    def __init__(self):
    # def: This keyword is used to define a function or method.
    # __init__: This is the name of the special method that serves as the constructor.
    # (self): The self parameter is a reference to the instance of the class. It allows you to refer to the instance's attributes and methods within the class.
        pg.init()
        self.screen = pg.display.set_mode(RES) # This sets the resolution set out in the settings.py file.
        self.clock = pg.time.Clock() # This controls the frame rate
        self.new_game()

    def new_game(self):
        self.map = Map(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'cDoom FPS: {self.clock.get_fps() :.1f}') # This shows the FPS on the bar at the top of the Window

    def draw(self):
        self.screen.fill('black') # This controls the background colour
        self.map.draw() # This draws the map from map.py

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
