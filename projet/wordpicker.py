#Stanley Jamais
#Hetic 2021
#Projet jeu d'insulte python

from random import *

"""
Ceci est le picker de mot, penser a insert le tab des mots 
  - Il initialise la lise // ok
  - Il disp la liste // ok
  - il retourne les mots random pick // ok
  - faire re-remplissage de liste //
  - NEXT voir bloc // ok
"""

class wordpicker: 

  def __init__(self,words,verbs,subjects,negations,more):
    self.words = words
    self.verbs = verbs
    self.subjects = subjects
    self.negations = negations
    self.more = more 

  def listing_words(self,the_list):
    i = 0
    for word in the_list:
      print(i,"|",word[0],"|",i)
      i+=1

  def random_maker_words(self):
    final_list=[]
    while len(final_list)!= 8:
      final_list.append(self.verbs[randint(0,len(self.verbs)-1)])
      final_list.append(self.subjects[randint(0,len(self.subjects)-1)])
      final_list.append(self.negations[randint(0,len(self.negations)-1)])
      final_list.append(self.more[randint(0,len(self.more)-1)])
    return final_list

