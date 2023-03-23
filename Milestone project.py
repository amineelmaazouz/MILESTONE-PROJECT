# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:18:29 2023

@author: amine el maazouz
"""


import random
values={'Two': 2,'Three': 3,'Four': 4,'Five': 5,'Six': 6,'Seven': 7,'Eight': 8,'Nine': 9,'Ten': 10,'Jack': 11,'Queen': 12,'King': 13,'Ace': 14}
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
suits=('Hearts','Clubs','Spades','Diamonds')


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank +  " of "  +  self.suit
    
    
class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                new_card= Card(suit,rank)
                self.all_cards.append(new_card)
    def schuffle(self):  #elle est faite pour que nos cartes soient désordonnées 
         random.shuffle(self.all_cards) #on peut pas mettre return ici vu que la méthode shuffle ne retourne rien elle modifie notre liste aléatoirement 
    
    def deal_one(self):
        return self.all_cards.pop()# retourne et retire le dernier element de notre liste all_cards
    
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)#Car le principe du jeu est de retirer la première carte 
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            return self.all_cards.extend(new_cards)  #Pour + d'une carte  
        else :
            return self.all_cards.append(new_cards)# Pour une seule carte 
    def __str__(self):
        return f' Player {self.name} has {len(self.all_cards)} cards'
    
    
#Création des joeurs
player_one=Player("One")
player_two=Player("Two")
 
#Création des cartes
new_deck=Deck()
#On va changer leurs ordre en utilisant shuffle()  
new_deck.schuffle()

#Distribution de carte sur les joeurs
#ON a que le nombre total de carte c'est 52 donc chaque joueur aura 26 cartes 
for  x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
#On commence le jeu en utilisant une boucle 
game_on=True 
round_num=0
while game_on:#tant que aucun des 2 joeurs n'a perdu    
    round_num+=1
    
    if len(player_one.all_cards)==0:
        print("Player one lost! Player two wins !")
        game_on=False 
        break
    
    if len(player_two.all_cards)==0:
        print("Player two lost! Player one wins !")
        game_on=False 
        break
    
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
   
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    
    #Comparision entre les cartes pour voir qui gagne le round 
    
    at_war=True#cas d'égalité
    while at_war:
        if player_one_cards[-1].value>player_two_cards[-1].value:
             player_one.add_cards(player_one_cards)
             player_one.add_cards(player_two_cards)#il prend ses cartes et les cartes du 2eme joueurs 
             at_war=False
             
    
        elif player_one_cards[-1].value<player_two_cards[-1].value:
             player_two.add_cards(player_two_cards)
             player_two.add_cards(player_one_cards)
             at_war=False
             
        else:
            print('WAR')
            
            
            if len(player_one.all_cards)<5:#5 n'est qu'un exemple mais + le nombre est grand + la partie va rapidement se terminer 
                print("Player One can't declare War")
                print("Player Two Wins ")
                game_on=False#Jeu arreter
                break
            
            if len(player_one.all_cards)>5:#5 n'est qu'un exemple mais + le nombre est grand + la partie va rapidement se terminer 
                print("Player Two can't declare War")
                print("Player One Wins ")
                game_on=False#Jeu arreter
                break
            
            else:
                for x in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
    
    
    
    
    
    