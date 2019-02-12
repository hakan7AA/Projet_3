import pygame
from pygame.locals import *
from classes import * 
from methods import *

pygame.init()

window = pygame.display.set_mode((615,615))
background = pygame.image.load('ressource/background.png').convert()
wall = pygame.image.load('ressource/wall.png').convert()
win = pygame.image.load('ressource/win.png').convert()
lose = pygame.image.load('ressource/lose.png').convert()

player = MacGyver()  # on instancie
exit = Exit()         # on instancie
laby = generate_laby(player, exit)

ether = Item('Ether', 'ressource/item1.png') #ici on met les nom des objet alors que quand on initialize item on met pas le nom
ether.set_coord(random_coordinates()) # on definitles coordonnée
laby = put_item_in_laby(laby, ether, player, exit) # on lui dis que generate_laby egale a put_item_in_laby mais avec ce nouvelle item precisé

tube = Item("Tube", 'ressource/item2.png')
tube.set_coord(random_coordinates())
laby = put_item_in_laby(laby, tube, player, exit)

needle = Item("Needle", 'ressource/item3.png')
needle.set_coord(random_coordinates())
laby = put_item_in_laby(laby, needle, player, exit)

display_laby(laby, window, wall, background, player, exit)

running = 1 #initialize running
capture = 1 #initialize capture
item_count = 0 #compteur d'item
pygame.key.set_repeat(400,30) #pour pourvoir choisir laa vitesse a laquel je vais 

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
            capture = 0
    while capture:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
                capture = 0        
            # Mouvement par capture d'événement
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    for square in laby:
                        # Vérifie si la case suivante n'est pas un mur et définit de nouvelles coordonnées pour le joueur si la condition est vraie
                        if square.get_coord().get_y() == (player.get_coord().get_y() + 1) and square.get_coord().get_x() == player.get_coord().get_x() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_laby(laby, window, wall, background, exit, player) #on remet sa a chaque fois pcq dans cette method ya pygame.display.flip  
                            # Verifie sil y a objet sur la case et le selectionne si la condition est vrai
                            if square.get_has_item() is True: # il y a (pas)
                                item_count += 1 #comme il le ramasse il le met dans son compteur donc il rajoute 1
                                square.set_has_item(False) # definir (supprime le )
                                square.get_item().set_got_item(True) #et met sa (le vide 'empty')
                                display_laby(laby, window, wall, background, exit, player)
                            pygame.display.flip()
                            # Vérifie si le carré est la sortie, et si c'est le cas, vérifie si le joueur a tous les objets
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Le joueur gagne s'il a tous les objets, perd s'il en manque un, le jeu attend la fermeture de la fenêtre
                                if item_count == 3:
                                    exit.empty()                                     # bah quand il attein troisil doit le laisser passer
                                    display_laby(laby, window, wall, background, exit, player) #mettre a jour
                                    window.blit(lose, (0, 150)) # affichage de ta perdu
                                    pygame.display.flip() #mettre a jour
                                    capture = 0 #donc cette boucle capture prend fin si ya tt sa 
                                else:
                                    player.empty()# sinon sil atteint pas 3 nah c'est MacGyver qui displarait a sa place
                                    display_laby(laby, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break # L'instruction break en Python termine la boucle en cours et reprend l'exécution à l'instruction suivante, tout comme la rupture traditionnelle trouvée dans C. L'utilisation la plus courante de break est le déclenchement d'une condition externe nécessitant la sortie précipitée d'une boucle. L'instruction break peut être utilisée dans les boucles while et for.

                if event.key == K_UP:
                    for square in laby:
                        # Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
                        if square.get_coord().get_y() == (player.get_coord().get_y() - 1) and square.get_coord().get_x() == player.get_coord().get_x() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_laby(laby, window, wall, background, exit, player)
                            # Checks if there's an item on the square, and picks it if the condition is true
                            if square.has_item is True:
                                item_count += 1
                                square.set_has_item(False)
                                square.get_item().set_got_item(True)
                                display_laby(laby, window, wall, background, exit, player)
                            pygame.display.flip()
                            # Checks if the square is the exit, and if it is, checks if the player has all the items
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
                                if item_count == 3:
                                    exit.empty()
                                    display_laby(laby, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                                else:
                                    player.empty()
                                    display_laby(laby, window, wall, background, exit, player)
                                    window.blit(lose, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break

                if event.key == K_LEFT:
                    for square in laby:
                        # Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
                        if square.get_coord().get_x() == (player.get_coord().get_x() - 1) and square.get_coord().get_y() == player.get_coord().get_y() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_laby(laby, window, wall, background, exit, player)
                            # Checks if there's an item on the square, and picks it if the condition is true
                            if square.get_has_item() is True:
                                item_count += 1
                                square.set_has_item(False)
                                square.get_item().set_got_item(True)
                                display_laby(laby, window, wall, background, exit, player)
                            pygame.display.flip()
                            # Checks if the square is the exit, and if it is, checks if the player has all the items
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
                                if item_count == 3:
                                    exit.empty()
                                    display_laby(laby, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                                else:
                                    player.empty()
                                    display_laby(laby, window, wall, background, exit, player)
                                    window.blit(lose, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break

                if event.key == K_RIGHT:
                    for square in laby:
                        # Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
                        if square.get_coord().get_x() == (player.get_coord().get_x() + 1) and square.get_coord().get_y() == player.get_coord().get_y() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_laby(laby, window, wall, background, exit, player)
                            # Checks if there's an item on the square, and picks it if the condition is true
                            if square.get_has_item() is True:
                                item_count += 1
                                square.set_has_item(False)
                                square.get_item().set_got_item(True)
                                display_laby(laby, window, wall, background, exit, player)
                            pygame.display.flip()
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
                                if item_count == 3:
                                    exit.empty()
                                    display_laby(laby, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                                else:
                                    player.empty()
                                    display_laby(laby, window, wall, background, exit, player)
                                    window.blit(lose, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break
