"""

Fichier contenant certaines données indispensables pour le jeu

"""


#VARIABLES


#Lettres autorisés présentés au joueur
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Lettre saisie par l'utilisateur
lettre = ""

#Coups du joueur
nb_coups = 10

#Liste qui va contenir les lettres déjà tapés par l'utilisateur
liste_dits = []

#Variable pour sortir du programme
quitter = ""

#Variable pour sortir du jeu
continuer_partie = True

# Mise en place d'un compteur qui va permettre de mettre fin au jeu en cas de victoire
compteur = 0

#Base de données des mots faciles
liste_easy = ["lapin","chat","renard","canard","cheval","chien","elephant","poule","lion","singe","sanglier",
              "baignoire","rideau","television","chaise","buffet","cuisine","ordinateur","clavier","brosse" ]

#Base de données des mots moyens
liste_medium = ["guitare","trompette","saxophone","rubis","python","testicule","boomerang","planete","seisme","terrestre"]
              
#Base de données des mots difficiles        
liste_hard = ["polymerisation","jazz","plastronner","flamboyant","haptique","limpide","turbide","pancreas","inodore"]  
    
#Compteur pendu pour afficher les dessins
pendu = 0       
       
#Liste contenant les dessins du pendu
dessins = [
"""
      
 
 
 
 
 _ _ _ 
 """,
"""
 |     
 |
 |
 |
 |
 |_ _ _ 
 """,
 """
 ---------
 |     
 |
 |
 |
 |
 |_ _ _
 """,
 """
---------
 |     |
 |
 |
 |
 |
 |_ _ _
 """,
 """
 ---------
 |     |
 |     o
 |
 |
 |
 |_ _ _
 """,
 """
 ---------
 |     |
 |     O
 |     |
 |
 |
 |_ _ _
 """,
 """
 ---------
 |     |
 |     O
 |    /|
 |
 |
 |_ _ _
 """,
 """
 ---------
 |     |
 |     O
 |    /|/
 |
 |
 |_ _ _
 """,
 """
 ---------
 |     |
 |     O
 |    /|/
 |    / 
 |
 |_ _ _
 """,
 """
 ---------
 |     |
 |     O     PENDU :p
 |    /|/
 |    //
 |
 |_ _ _
 """
 ]         
              

