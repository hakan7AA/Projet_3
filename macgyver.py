import pygame
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

window = pygame.display.set_mode((window_corner, window_corner))

choice = 'macgyverlaby'

empty = pygame.image.load(image_empty).convert()
guardian = pygame.image.load(image_guardian).convert_alpha()
    
level = Level(choice)
level.generate()
level.display(window)

mac = Character(macgyver, level)
pygame.display.flip()

carryon = 1
while carryon:
  pygame.time.Clock().tick(30)

  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_RIGHT:
        mac.move('right')
      elif event.key == K_LEFT:
        mac.move('left')  
      elif event.key == K_UP:
        mac.move('up')
      elif event.key == K_DOWN:
        mac.move('down')

      
  window.blit(empty, (0,0))
  level.display(window) 
  window.blit(mac.macgyver, (mac.x, mac.y))
  window.blit(guardian, (492,492))
  
  pygame.display.flip()

  if level.structure[mac.box_y][mac.box_x] == 'a':
    carryon = 0      

  
    
    

