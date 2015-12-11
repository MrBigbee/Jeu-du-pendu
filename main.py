"""

Programme principal du pendu

"""


#Import du module random pour pouvoir selectionner un mot au hasard dans les listes
import random

#Import des variables
from variables import *

#Import des fonctions
from fonctions import *


#Tant que le joueur ne quitte pas le jeu
while quitter != "o" and "O":
    
    
    #Intro du jeu
    print("Bienvenue dans le Bigbee Pendu." )
    print("Voici les lettres dont le mot caché est composé : {0}".format(alphabet))
    
    #Demande du pénom au joueur
    pseudo = input("Quel est votre pseudo ? ")
    
    #Demande de la difficulté
    difficulte = input("Veuillez choisir votre difficulté : Pour Facile, taper 1, pour Intermédiaire, taper 2, pour Difficile, taper 3. Puis appuyer sur entrée : ")
    
    #Tant qu'un chiffre n'a pas été saisi
    while not difficulte.isdigit():
        #On réaffiche les propositions
        difficulte = input("Vous devez saisir 1 pour Facile, 2 pour Intermédiaire, 3 pour Difficile : ")
                
    #Si la difficulté vaut 1
    if difficulte == str(1):
        #Sélection du mot parmi ceux de la BDD facile
        mot = random.choice(liste_easy)
        #On indique la longueur du mot
        print("C'est un mot en {0} lettres ! ".format(len(mot)))
        #On affiche le mot masque grace à sa fonction
        dis_mot_masque(mot, liste_dits)
        
    #Si la dificulté vaut 2
    elif difficulte == str(2):
        mot = random.choice(liste_medium)
        print("C'est un mot en {0} lettres ! ".format(len(mot)))
        dis_mot_masque(mot, liste_dits)
        
    #Si la difficulté vaut 3
    elif difficulte == str(3):
        mot = random.choice(liste_hard)
        print("C'est un mot en {0} lettres ! ".format(len(mot)))
        dis_mot_masque(mot, liste_dits)

    #Tant que le joueur n'a pas gagné ou perdu
    while continuer_partie is True:

        #Demande de saisie au joueur
        lettre = input("Saississez une lettre de l'alphabet : ")
        
        
        #PLUSIEURS LETTRES SAISIES + CONTROLE SUR ALPHABET
        
        #Tant que plusieurs lettres sont tapés:
        while len(lettre) > 1:
            #Seule la première est prise en compte
            lettre = lettre[0]
            print("Vous avez tapés plusieurs lettres ! Seule la première a été prise en compte.")
            #Tant que la lettre n'est pas autorisée
            while lettre not in alphabet:
                #Demande de saisie au joueur
                print("Erreur ! Vous avez saisi au moins un caractère non autorisé (majuscule, chiffre ou autre)")
                lettre = input("Saississez une lettre de l'alphabet : ")  
                
        
        #PLUSIEURS LETTRES SAISIES + CONTROLE SUR LISTE_DITS
        
        #Tant que plusieurs lettres sont tapés:
        while len(lettre) > 1:
            #Seule la première est prise en compte
            lettre = lettre[0]
            print("Vous avez tapés plusieurs lettres ! Seule la première a été prise en compte.")
            #Tant que la lettre a déjà été dictee
            while lettre in liste_dits:
                #On informe le joueur
                print("Cette lettre a déjà été dite !")
                #Il doit resaisir une lettre
                lettre = input("Saississez une lettre de l'alphabet : ")
        
        
        #UNE SEULE LETTRE SAISIE

        #Tant que la lettre saisie est autorisée
        while lettre not in alphabet:
                #Demande de saisie au joueur
                print("Erreur ! Vous avez saisi au moins un caractère non autorisé (majuscule, chiffre ou autre)")
                lettre = input("Saississez une lettre de l'alphabet : ")
                
        #Tant que la lettre a déjà été dictee
        while lettre in liste_dits:
            #On informe le joueur
            print("Cette lettre a déjà été dite !")
            #Il doit resaisir une lettre
            lettre = input("Saississez une lettre de l'alphabet : ")  
            #Tant que plusieurs lettres sont tapés:
            while len(lettre) > 1:
                #Seule la première est prise en compte
                lettre = lettre[0]
                print("Vous avez tapés plusieurs lettres ! Seule la première a été prise en compte.")
                #Tant que la lettre a déjà été dictee
                while lettre in liste_dits:
                    #On informe le joueur
                    print("Cette lettre a déjà été dite !")
                    #Il doit resaisir une lettre
                    lettre = input("Saississez une lettre de l'alphabet : ")   
        
        #Si la lettre est contenu dans le mot:
        if lettre in mot:
            #Pour chaque indice avec sa lettre contenus dans le mot:
            for indice, elem  in enumerate(mot):
                #Si une lettre du mot correspond avec celle donnee par l'utilisateur:
                if lettre == elem:
                    #On incrémente le compteur de 1
                    compteur += 1
                    #On ajoute à la liste des lettres dites la lettre
                    liste_dits.append(lettre)
                    #On donne la position de la lettre au joueur:
                    print("Ok ! La lettre se trouve en position {0}".format(indice + 1))
                    #Affichage du mot masqué
                    dis_mot_masque(mot, liste_dits)
                    #Si notre compteur devient égal à la longueur du mot
                    if compteur == len(mot):
                        #On indique au joueur que c'est gagné ! Et on confirme le mot en majuscule
                        print("Bravo, c'est gagné ! C'était bien {0} !".format(mot.upper()))
                        #La partie se termine
                        continuer_partie = False
            
        #Sinon
        else:
            #On désincremente nb_coups de 1
            nb_coups -= 1
            #Indique au joueur le nombre de coups restants
            print("Zut ! Il vous reste {0} coup(s) ".format(nb_coups))
            #Affichage d'un dessin du pendu 
            print(dessins[pendu])
            #Incrémentation du compteur pendu pour pouvoir passer au dessin suiant en cas d'une autre erreur
            pendu += 1
            #Ajoute la lettre donnée à la liste de lettres déjà dictées
            liste_dits.append(lettre)
            #Affichage du mot masqué
            dis_mot_masque(mot, liste_dits)
                
            #Si le nombre de coups restants vaut zéro:
            if nb_coups == 0:
                #Le joueur ne peut plus continuer la partie car il a perdu
                continuer_partie = False
                #On indique au joueur qu'il n'a plus de coups et le mot qu'il devait trouver en majuscule
                print("Vous avez épuisé tous vos coups ! C'est perdu.\nLe mot était {0}".format(mot.upper()))
                               
    #On indique que la partie est terminé
    print("La partie est terminé.")
    
    #Le nombre de coups restant devient le score du joueur
    score = nb_coups
    
    #Ouverture du fichier de sauvegarde des scores en ecriture avec ajout. S'il n'existe pas, il est crée dans le repertoire courant du jeu
    fichier_score = open("score.txt", "a")
    
    #Enregistrement des donnes relatives au score dans le fichier
    fichier_score.write("\n" + pseudo + "\t" + str(score) + "\t" + mot)
    
    #Fermeture du fichier
    fichier_score.close()
    
    #Indication de l'enregistrement du score
    print("Votre score a été enregistré dans le répertoire du jeu")
    
    #On demande au joueur si il veut quitter le programme, si non, il recommence à jouer et les paramètres sont réinitialisés
    quitter = input("Voulez-vous quitter le jeu ? o / n. ")

    continuer_partie = True
    nb_coups = 10
    compteur = 0
    liste_dits = []
    pendu = 0
     
