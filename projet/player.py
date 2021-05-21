#Stanley Jamais
#Hetic 2021
#Projet jeu d'insulte python


"""
Ceci est le createur de perso
  - Il initialise le eprsonnage // ok
  - Il disp lepersonnage // ok
  - il retourne le perso // ok
  - NEXT voir bloc // ok
"""

class player:

  def __init__(self,name,caracter):
    self.name = name
    self.caracter = caracter
    self.player_empty = [ ["name",""] , ["health",0] , ["caracter",""] , ["sentense",[] ] ]
  def creation_caracter(self):
    self.player = self.player_empty
    self.player[0][1] = self.name
    self.player[1][1] = 50
    self.player[2][1] = self.caracter
    self.player[3][1] = [["",0,""],["",0,""],["",0,""],["",0,""],["",0,""],["",0,""],["",0,""],["",0,""]]
    return self.player

  def listing_caracter(self):
    print(self.player)
