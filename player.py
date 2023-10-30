from settings import *
import pygame as pg
import math
class player:
  def __init__(self,game):
    self.game = game
    self.x, self.y = player_pos
    self.angle = player_angle
    self.speed = 0
    self.x_change = x_change
    self.y_change = y_change
    self.dx, self.dy = 0, 0


    self.accelerating = False
    self.stopped = True

  def check_wall(self,x,y): #Check for wall collision by comparing that point with the world_map.
    return(x,y) not in self.game.map.world_map
  
  def get_movement(self): #Get movement from the player.
    keys = pg.key.get_pressed() #dictionary of keys pressed this frame
    if keys[pg.K_w]: #Forward acceleration
      self.stopped = False
      self.speed += player_accel * self.game.deltaTime
    elif keys[pg.K_s]: #Backward acceleration
      self.stopped = False
      self.speed -= player_accel * self.game.deltaTime
    else: #No input, begin decelerating
      if not self.stopped:
        if abs(self.speed) > accelsens:
          self.speed *= 1 - (player_deccel * self.game.deltaTime)
        else:
          self.stopped = True
          self.speed = 0

    if keys[pg.K_LEFT]: #Turning
      self.angle -= player_rot_speed * self.game.deltaTime
    if keys[pg.K_RIGHT]:
      self.angle += player_rot_speed * self.game.deltaTime
    self.angle %= math.tau # To keep the player angle below 2pi. Clever.

  def apply_movement(self): #Apply the current velocity (self.angle as direction, self.speed as magnitude)
    self.x_change = self.speed * math.cos(self.angle) * self.game.deltaTime
    self.y_change = self.speed * math.sin(self.angle) * self.game.deltaTime

    #Throttle if max speed is reached.
    if self.speed > max_speed: 
        self.speed = max_speed

    #Check for collisions before applying movement.
    if self.check_wall(int(self.x + self.x_change),int(self.y)): #If not colliding with a wall on the x axis,
      self.x += self.x_change #Then apply for that axis
    if self.check_wall(int(self.x),int(self.y+self.y_change)):
      self.y += self.y_change

  def draw(self):
    xDisplay = self.x * TANKCOORDINATEMULTX #The X coordinate for display purposes.
    yDisplay = self.y * TANKCOORDINATEMULTY
    pg.draw.line(self.game.screen, 'red', (xDisplay, yDisplay), 
                 (xDisplay + WIDTH * math.cos(self.angle),
                 yDisplay + WIDTH * math.sin(self.angle)), 2) #Drawing the aiming line. 
    pg.draw.rect(self.game.screen,'red', pg.Rect(xDisplay , yDisplay , tankWidth, tankHeight )) #Drawing the rectangle.

  def update(self):
    self.get_movement()
    if not self.stopped:
      self.apply_movement()
  
  @property
  def pos(self):
    return self.x, self.y
  @property
  def map_pos(self):
    return int(self.x), int(self.y)