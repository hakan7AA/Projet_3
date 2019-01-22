import pygame
from pygame.locals import *

from constantes import *

class Level:
  def __init__(self, file):
    self.file = file
    self.structure = 0

  def generate(self):
    with open(self.file, 'r') as file:
      structure_level = []
      for line in file:
        line_level = []
        for sprite in line:
          if sprite != '\n':
            line_level.append(sprite)
        structure_level.append(line_level)
      self.structure = structure_level
      
  def display(self, window):
    wall = pygame.image.load(image_wall).convert()
    start = pygame.image.load(image_start).convert()
    arrive = pygame.image.load(image_arrive).convert()

    num_line = 0
    for line in self.structure:
      num_box = 0
      for sprite in line:
        x = num_box * size_sprite
        y = num_line * size_sprite
        if sprite == 'm':
          window.blit(wall, (x,y))
        elif sprite == 'd':
          window.blit(start, (x,y))
        elif sprite == 'a':
          window.blit(arrive, (x,y))
        num_box += 1
      num_line += 1  

class Character:
  def __init__(self, macgyver, level):
    self.macgyver = pygame.image.load(macgyver).convert()

    self.box_x = 0
    self.box_y = 0
    self.x = 0
    self.y = 0

    self.level = level

  def move(self, macgyver):
    if macgyver == 'right':
      if self.box_x < (number_sprite_corner - 1):
        if self.level.structure[self.box_y][self.box_x + 1] != 'm':
          self.box_x += 1

          self.x = self.box_x * size_sprite

     
    if macgyver == 'left':
      if self.box_x > 0:
        if self.level.structure[self.box_y][self.box_x - 1] != 'm':
          self.box_x -= 1

          self.x = self.box_x * size_sprite


    if macgyver == 'up':
      if self.box_y > 0:
        if self.level.structure[self.box_y - 1][self.box_x] != 'm':
          self.box_y -= 1

          self.y = self.box_y * size_sprite


    if macgyver == 'down':
      if self.box_y < (number_sprite_corner - 1):
        if self.level.structure[self.box_y + 1][self.box_x] != 'm':
          self.box_y += 1

          self.y = self.box_y * size_sprite  

    
               