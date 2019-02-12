import pygame
from pygame.locals import *


class MacGyver:
  def __init__(self):
    self.coord = Coordinates(None, None)
    self.sprite = pygame.image.load('ressource/MacGyver.png').convert_alpha()

  def get_coord(self):
    return self.coord

  def set_coord(self, coord):
    self.coord = coord

  def get_sprite(self):
    return self.sprite

  def empty(self):
    self.sprite = pygame.image.load('ressource/empty.png').convert_alpha()          



class Exit:
  def __init__(self):
    self.coord = Coordinates(None, None) #onn a rien dans les coordonées encore 
    self.sprite = pygame.image.load('ressource/exit.png').convert_alpha()

  def get_coord(self): # on veut savoir les coordonée
    return self.coord

  def set_coord(self, coord): #on defini les coordonée
    self.coord = coord

  def get_sprite(self):  #on renvoi au sprite
    return self.sprite

  def empty(self):  #pour l'estethic
    self.sprite = pygame.image.load('ressource/empty.png').convert_alpha()        


class Coordinates:
  def __init__(self, x, y): #on initialise x et y
    self.x = x
    self.y = y

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y    


class Square:
  def __init__(self, coord, is_wall):
    self.coord = coord
    self.is_wall = is_wall #on met is wall des le debut parce que les mur doivent etre coler direct sinon sa sert a rien on a rien #pour precision que c un mur aussi pour faire difference quand on va coller les item et dire que si on precise pas item.is_wall etc bah on colle pas sur le mur l'item mais sur le vide
    self.has_item = False #boléens qui va nous servir dans le code
    self.item = Item(None, 'ressource/empty.png') #on doit mettre deux coordonée et le premier je met vide pcq le nom n'est pas encore connu c quel item et le deuxieme comme j'initialize je met empty le vide

  def get_is_wall(self): #c'est un mur c vrai ou faux 
    return self.is_wall

  def get_has_item(self): #c'est un item vrai ou faux
    return self.has_item

  def get_coord(self):
    return self.coord

  def get_item(self): #get item sa va nous envoyer vers la class item
    return self.item

  def set_has_item(self, state): # choisir l'etat de notre item
    self.has_item = state

  def set_item(self, item):
    self.item = item            #c'est dans cette methode quil y a sa seulement, dans la methode set_item bah self.item =item c a dire les photo dobjet

class Item:
  def __init__(self, name, sprite):
    self.name = name # pour initialiser et montrer que dans item(none, etc) le none sera remplacer par le nom que j'ai initialiser et qui se trouve dans macgyver.py
    self.coord = Coordinates(None, None)
    self.got_item = False
    self.sprite = pygame.image.load(sprite).convert_alpha() #pour dire affiche les sprite c a dire les item tous 

  def get_coord(self):
    return self.coord

  def get_got_item(self):
    return self.got_item

  def get_sprite(self):
    return self.sprite 

  def set_got_item(self, state):
    self.got_item = state

  def set_coord(self, coord):
    self.coord = coord          
        


      
    




