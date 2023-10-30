import pygame as pg
from settings import *

_ = False 
mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,_,_,_,_,1,1,1,1,1],
    [1,_,_,_,_,1,1,_,_,_,_,1,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,1,_,_,_,_,_,1,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

boxWidth = 100 * RESMULTX
boxHeight = 100 * RESMULTY

class Map:
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self): #Fillout the world_map dictionary, so it that only contains the cells that have boxes from the mini_map.
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value #Notice that it is a dictionary of tuples, x and y for each point.

    def draw(self): #Draw each box, according to coordinates.
        [pg.draw.rect(self.game.screen, 'white', (pos[0] * boxWidth, pos[1] * boxHeight, boxWidth, boxHeight), 2)
         for pos in self.world_map]
  