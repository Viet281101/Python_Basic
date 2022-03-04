import random

mots = ["pomme", "fraise","kiwi", "cerise", "orange"]
choix = random.choice(mots)
vies = 7
longeur=len(choix)
liste_erreur = []
liste = []
tout_deviner = False
print("Bienvenu dans le jeu du pendu, vous allez devoir deviner un mot, une lettre par essaie, \nvous disposez de 7 vies, vous en perderais une à chaque essaie faux.")


while not tout_deviner:
    tout_deviner = True
    essaie = (input("Saissiez une lettre : "))
    liste.append(essaie)
    for l in choix:
        if l in liste:
            print(l, end=" ")
        else:
            tout_deviner = False
            print("_", end=" ")
    if tout_deviner:
        print("Bravo ! Tu a deviné le mot", "'",choix,"'","Félicitation !")
        break

    if essaie in choix:
        print("Bravo !, vous avez trouvé une lettre ! ")

    if essaie in liste_erreur:
        print("Vous avez déjà dit cette lettre !")

    elif essaie not in choix:
        print("Faux, cette lettre ou ce mot n'est pas bon !")
        vies-=1
        liste_erreur.append(essaie)
        print("Voici la liste des lettre qui ne sont pas dans le mot : ",liste_erreur,"\nIl vous reste ",vies," vies")

    if vies == 0:
        print("Vous avez perdu ! Le mot à deviner était : ", choix)
        break

