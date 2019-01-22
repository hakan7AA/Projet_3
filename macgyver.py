import pygame
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

window = pygame.display.set_mode((window_corner, window_corner))

carryon = 1 
while carryon:
  home = pygame.image.load(image_home).convert()
  window.blit(home, (0,0))

  pygame.display.flip()

  carryon_home = 1
  carryon_game = 1
  carryon_treasure = 1
  carryon_piece = 1
  carryon_potion = 1
  while carryon_home:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_F1:
          carryon_home = 0
          choice = 'macgyverlaby'

  if choice != 0:
    empty = pygame.image.load(image_empty).convert()
    guardian = pygame.image.load(image_guardian).convert_alpha()
    potion = pygame.image.load(image_potion).convert_alpha()
    piece = pygame.image.load(image_piece).convert_alpha()
    treasure = pygame.image.load(image_treasure).convert_alpha()
    

    level = Level(choice)
    level.generate()
    level.display(window)


    mac = Character(macgyver, level)

  while carryon_game:
      
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
    window.blit(piece, (246,205))
    window.blit(potion,  (208,290))
    window.blit(treasure, (0,330))
    pygame.display.flip()

    if level.structure[mac.box_y][mac.box_x] == 'a':
      carryon_game = 0      

  while carryon_piece:
    if macgyver == (246,205):
      carryon_piece = 0

      pygame.display.flip()
    
    

