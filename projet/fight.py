#Stanley Jamais
#Hetic 2021
#Projet jeu d'insulte python

from random import *
from player import *
from wordpicker import *


"""
Ceci est le combat
  - Il initialise le eprsonnage // ok
  - Il disp lepersonnage // ok
  - il retourne le perso // ok
  - NEXT voir bloc // ok
"""   

class combat:

  def __init__(self,player1,player2):
    self.player1 = player1
    self.player2 = player2

  def is_dead(self,player1,player2): # ok
    if player1[1][1] == 0:
      return 2
    elif player2[1][1] == 0:
      return 1
    else:
      return 0

      
  def check_correct(self,sentense):
    x = 2
    if sentense[0][2] == "sub":

      if sentense[1][2] == "verb":
        while x < 8:
          if sentense[x][2] == "":#Fin de chaine
            x = 8
          elif sentense[x][2] == "more":
            x += 1
          else: # else si c'est pas == "more" 
            return sentense[x][1]
      elif  sentense[1][2] == "": 
        return True
      else : 
        return sentense[1][1]
    else : 
      return sentense[0][1]

    

  def calculus(self,player):

    x = 0 
    acc = 0
    while player[3][1][x][1] != "":
      acc = acc + player[3][1][x][1]
      x+=1
    return acc



  def fight(self,player1,player2):

    key = 0
    turn = 0
    p1 = ""
    p2 = ""

    verbs = [ ['are',50,'verb'] , ['is',50,'verb'] ]
    subjects = [ ['You',50,'sub'] , ['Your mom',50,'sub'] ]
    negations = [ ['isn\'t',50,'neg'] , ['not',50,'neg'] ]
    more = [ ['a train',50,'more'] , ['a slut',50,'more'] ]
    words = verbs + subjects + negations + more

    instance = wordpicker(words,verbs,subjects,negations,more)
    
    while key == 0: #Tant que personne n'es mort
 
    
      if turn == 0: #si on débute crée une list
        the_list = instance.random_maker_words()

      if len(the_list) == 0: #si la liste est vide call le compteur
        dmg_player1 = self.calculus(player1)
        dmg_player2 = self.calculus(player2)
        
        player1[1][1] = player1[1][1] - dmg_player2
        player2[1][1] = player2[1][1] - dmg_player1
        if self.is_dead(player1,player2) == 0: # si ça return 0, refaire une liste
          the_list = instance.random_maker_words()

      key = self.is_dead(player1,player2)#Key de sortie  

      if turn%2 == 0 and p1!="pass":

        instance.listing_words(the_list)
        print("9 | Stop picking | 9")
        print("hp",player1[1][1])
        print("Player 1's turn\n------------------------\nPlease select a word using the following numbers :")
        
        input_player = int(input())
        verif = isinstance(input_player, int) 
        if verif == False:
          print("Try again.1")
        else : # si c'est bien un int 
          if input_player == 9:
            turn +=1
            p1 = "pass"  
          elif input_player>len(the_list) or input_player<0:
            print("Try again.2")
          else : #patché 
            player1[3][1].insert(int(turn/2),the_list[input_player])
            player1[3][1].pop(7)
            printer = self.check_correct(player1[3][1])
            print(printer)
            if printer != True :
              player1[3][1].pop(0)
              player1[3][1].append("")
              player1[1][1] = player1[1][1] - printer
              key = self.is_dead(player1,player2)
            the_list.pop(input_player)
            print("hp",player1[1][1])
            turn += 1
      elif p1 == "pass":
        turn +=1

      if turn%2 == 1 and p2!="pass":

        instance.listing_words(the_list)
        print("9 | Stop picking | 9")
        print("hp",player2[1][1])
        print("Player 2's turn\n------------------------\nPlease select a word using the following numbers :")
        
        input_player = int(input())
        verif = isinstance(input_player, int) 
        if verif == False:
          print("Try again.1")
        else : # si c'est bien un int 
          if input_player == 9:
            turn +=1
            p2 = "pass"  
          elif input_player>len(the_list) or input_player<0:
            print("Try again.2")
          else : #patché 
            player2[3][1].insert(int(turn/2),the_list[input_player])
            player2[3][1].pop(7)
            printer = self.check_correct(player1[3][1])
            print(printer)
            if printer != True :
              player2[3][1].pop(0)
              player2[3][1].append("")
              player2[1][1] = player2[1][1] - printer
              key = self.is_dead(player1,player2)
            the_list.pop(input_player)
            print("hp",player2[1][1])
            turn += 1
      elif p1 == "pass":
        turn +=1

    if key == 1:
      print("player 1 wins")
      sys.exit()
    elif key == 2:
      print("player 2 wins")
      sys.exit()
