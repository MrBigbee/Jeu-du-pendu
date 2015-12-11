def dis_mot_masque(mot, liste_dits):

    """
    Fonction qui affiche un mot masqué tout ou en partie, en fonction :
    - du mot d'origine (type str mot)
    - des lettres déjà trouvées (type list liste_dits)
    
    On renvoie le mot d'origine avec des - remplaçant les lettres que l'on
    n'a pas encore trouvées.
    """
    
    #Variable qui va contenir le mot masqué
    mot_masque = ""
    #Pour chaque lettre dans le mot
    for lettre in mot:
        #Si une des lettres a été dite
        if lettre in liste_dits:
            #Le mot masqué s'incrémente de la lettre
            mot_masque += lettre
        else:
            #On ajoute des tirets
            mot_masque += "-"
    #On affiche le mot à l'utilisateur en majuscule
    print(mot_masque.upper())