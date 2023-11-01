from settings import *
import pygame as pg
import math

class player(pg.sprite.Sprite):
  def __init__(self,game):

    #Load in settings.
    self.game = game
    self.x, self.y = player_pos
    self.angle = player_angle
    self.speed = 0
    self.x_change = x_change
    self.y_change = y_change

    self.accelerating = False
    self.stopped = True

    #Preparing the sprite functionality of the object, and adding it to the playerGroup
    pg.sprite.Sprite.__init__(self) #Always call the sprite init.
    self.baseImage = pg.image.load(tankSpritePath).convert_alpha()
    self.baseImage = pg.transform.scale(self.baseImage, TANKDIMENSIONS)
    self.image = self.baseImage #Both self.image and self.rect are used by the Group object to draw the sprite onto the screen.
    self.rect = self.baseImage.get_rect(center=(self.x * RESMULTX,self.y * RESMULTY)) 

    self.game.playerGroup.add(self)

  def check_wall(self,x,y): #Check for wall collision by comparing that point with the world_map.
    return(x,y) not in self.game.map.world_map
  
  def get_movement(self): #Get movement from the player.
    keys = pg.key.get_pressed() #dictionary of keys pressed this frame
    if keys[pg.K_w]: #Forward 
      if self.speed < 0: #If the tank is moving backward and is now trying to move forward, it should also deccelerate.
        self.speed *= 1 - (player_deccel * self.game.deltaTime)
      self.stopped = False
      self.speed += player_accel * self.game.deltaTime
    elif keys[pg.K_s]: #Backward acceleration
      if self.speed > 0: #If the tank is moving forward and is now trying to move backward, then the tank should also deccelerate
        self.speed *= 1 - (player_deccel * self.game.deltaTime)
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

  def updateSprite(self): #Getting self.image ready to be blitted by game.playerGroup group. https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw 
    xDisplay = self.x * TANKCOORDINATEMULTX #The xy coordinates for display purposes.
    yDisplay = self.y * TANKCOORDINATEMULTY 
    self.image = pg.transform.rotate(self.baseImage,-(math.degrees(self.angle)))
    self.rect = self.image.get_rect(center=(xDisplay, yDisplay))


  def draw(self): #Obsolete, as the sprite object is now drawn by game.playerGroup.draw.
    xDisplay = self.x * TANKCOORDINATEMULTX #The xy coordinates for display purposes.
    yDisplay = self.y * TANKCOORDINATEMULTY 

    pg.draw.line(self.game.screen, 'red', (xDisplay, yDisplay), 
                 (xDisplay + WIDTH * math.cos(self.angle),
                 yDisplay + WIDTH * math.sin(self.angle)), 2) #Drawing the aiming line. 
    
  def update(self):
    self.get_movement()
    if not self.stopped:
      self.apply_movement()
    self.updateSprite()
  
  @property
  def pos(self):
    return self.x, self.y
  @property
  def map_pos(self):
    return int(self.x), int(self.y)