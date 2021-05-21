#Stanley Jamais
#Hetic 2021
#Projet jeu d'insulte python

from random import *
from player import *
from wordpicker import *
from fight import *




def menu():
  print("welcome to the game")
  print("1 - Start")
  print("2 - About us")
  print("3 - Quit")
  value = int(input())
  if value == 1:
    print("Player 1's name :")
    username1 = input()
    print("Player 1's caracter :")
    caracter1 = input()
    print("Player 2's name :")
    username2 = input()
    print("Player 2's caracter :")
    caracter2 = input()

    instance_player = player(username1,caracter1)
    player1 = instance_player.creation_caracter()
    instance_player = player(username2,caracter2)
    player2 = instance_player.creation_caracter()
    instance_combat =  combat(player1,player2)
    instance_combat.fight(player1,player2)

  if value == 2:
    print("about us")
    menu()
  if value == 3:
    exit()
  else:
    print("error")
    menu()

menu()