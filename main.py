import pygame as pg
import sys
import random
from settings import *
from map import *
from player import *

import DebuggingDisplay

class Game:
  def __init__(self):
    pg.init()
    self.screen = pg.display.set_mode(res)
    self.clock = pg.time.Clock()
    self.deltaTime = self.clock.tick(fps) / 1000

    self.debugDisplay = DebuggingDisplay.DebugDisplay(self)

    self.new_game()
    
  def new_game(self): #Initialize any new objects here.

    #Creating group objects to contain sprites
    self.playerGroup = pg.sprite.Group()
    #self.obstacleGroup

    #Creating individual objects. These objects should add themselves to the groups in their init.
    self.map = Map(self)
    self.player = player(self)

  def update(self): #Any logic that must be run per frame must be added to this loop, or must be called by a method called in this loop.
    self.player.update()
    pg.display.flip()
    self.deltaTime = self.clock.tick(fps) / 1000
    pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    self.debugDisplay.update()
    
  def draw(self): #Anything that must be drawn on screen per frame must be added to this loop.
    self.screen.fill('black')
    self.map.draw()
    self.player.draw()
    self.playerGroup.draw(self.screen)

    self.debugDisplay.draw()

  def check_events(self): #Any events that the main game loop must check for should be added here. So far, it only has QUIT.
    for event in pg.event.get():

      if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): #For quitting the game.
        pg.quit()
        sys.exit()
    
  def run(self): #The main game loop. 
    while True:
      self.check_events()
      self.update()
      self.draw()
  
if __name__ == '__main__':
  game = Game()
  game.run()
  