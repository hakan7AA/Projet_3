import random
import pygame
from pygame.locals import *
from classes import *

def random_coordinates():
    """methode qui permet d'obrtenir des coordnée au hazard. retourne un objet de type cordonnées"""
    return Coordinates(random.randint(0,14), random.randint(0,14))

def generate_laby(player, exit):
    """
    Method to generate the grid.

    Transforms the .txt file into a list of lines, then each line into a list of characters.
    For each character it will generate a square, or set the player/exit's position.
    """
    with open('macgyverlaby.txt') as txt_laby:
        str_laby = ''.join(line.strip() for line in txt_laby)#expression generatrice (pour les element de ma list '' ), pour parcourir chaque element de la ligne c'est str(line) for ..
        chr_laby = list(str_laby) #on dit que les ligne sont des listes
        laby = [] # c'est le labyrinthe, la grande liste
        x = 0
        y = 0

        for entry in chr_laby:
            # Sets square as a wall if the character is 'W'
            if entry == 'm':
                laby.append(Square(Coordinates(x, y), True))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1
            

            elif entry == 'x':
                laby.append(Square(Coordinates(x,y), False))
                if x < 14:
                    x = x + 1 
                
                elif x == 14:
                    x = 0
                    y = y + 1


            elif entry == 'd':
                laby.append(Square(Coordinates(x, y), False))
                player.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1    

            elif entry == 'a':
                # Sets the position of the exit if the character is a 'E'
                laby.append(Square(Coordinates(x, y), False))
                exit.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

    return laby


def display_laby(laby, window, wall, background, exit, player):
    """Method to display the grid."""
    window.blit(background, (0, 0))
    window.blit(player.get_sprite(), (player.get_coord().get_x() * 30, player.get_coord().get_y() * 30))
    window.blit(exit.get_sprite(), (exit.get_coord().get_x() * 30, exit.get_coord().get_y() * 30))

    for square in laby:
        if square.get_is_wall() is True:
            window.blit(wall, (square.get_coord().get_x() * 30, square.get_coord().get_y() * 30))

        else:
            if square.get_has_item() is True:
                window.blit(square.get_item().get_sprite(), (square.get_coord().get_x() * 30, square.get_coord().get_y() * 30))
    pygame.display.flip()             #si ya des item bah affiche les sprite c a dire un des trois item


def put_item_in_laby(laby, item, player, exit):
    """method pour coller les item dans les position hazardeuse"""
    for square in laby:
        if square.get_coord().get_x() == item.get_coord().get_x() and square.get_coord().get_y() == item.get_coord().get_y(): 
            if (item.get_coord().get_x() != exit.get_coord().get_x() and item.get_coord().get_y() != exit.get_coord().get_y()) and (item.get_coord().get_x() != player.get_coord().get_x() and item.get_coord().get_y() != player.get_coord().get_y()):
                if square.get_has_item() is True: #  item(option oui)
                    item.set_coord(random_coordinates()) #choisir coordonner position hazardeuse
                    put_item_in_laby(laby, item, player, exit) #pour executer deja sa 
                    break
                elif square.get_is_wall() is True: #mur (option oui)
                    item.set_coord(random_coordinates()) #choisir coordonée position hazardeuse
                    put_item_in_laby(laby, item, player, exit)
                    break
                elif square.get_is_wall() is False and square.get_has_item() is False:#si ya pas de mur ni d'item alors 
                    square.set_has_item(True)# choisi l'item (ajoute quelque chose, mais quoi ?)
                    square.set_item(item) # ca(c a dire un des objet)
                    break
            else:                                      #si c la meme position que gardier et macgyver
                item.set_coord(random_coordinates())  # alors choisi des position hazardeuse
                put_item_in_laby(laby, item, player, exit)
                break

    return laby

# Si j'enleve les break j'ai des aiguiulle partt!
# si j'enleve les put_itzm_in_laby j'ai pas les items