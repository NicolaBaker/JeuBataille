#------------------------------------------------------------------------------------------------------
# Nom : Nicola Baker
# Titre : Projet final du cours
# Description : Bataille
#-------------------------------------------------------------------------------------------------------

# - Programmes import ----------------------------------------------------------
import random
import tkinter as tk

# - Programmes principal
fenetre = tk.Tk()
fenetre.iconbitmap("bataille.ico")
fenetre.title("Bataille")
fenetre.geometry("500x620")
fenetre.minsize(500, 620)
fenetre.maxsize(500, 620)
fenetre['bg']= "#ffffff"

# - Tableau de carte
jeucarte = []

# - Tableau du joueur 1
joueur = []

# - Tableau du joueur 2
joueur1 = []

# - Formation de carte
for i in range(1,14):
    jeucarte.append(i)
    jeucarte.append(i)
    jeucarte.append(i)
    jeucarte.append(i)

# - Séparation des cartes pour le joueur 1
for i in range(26):
    poscarte = random.randint(0,len(jeucarte)-1)
    joueur.append(jeucarte[poscarte])
    jeucarte.pop(poscarte)

# - Séparation des cartes pour le joueur 2
for i in range(26):
    poscarte = random.randint(0,len(jeucarte)-1)
    joueur1.append(jeucarte[poscarte])
    jeucarte.pop(poscarte)

# - Carte de combat
cartej1 = joueur[0]
cartej2 = joueur1[0]

# - Image arrière-plan beaucoup de cartes
jeubg = tk.PhotoImage(file="bataillebg.png")

# - Image arrière-plan
jeupeudecartebg = tk.PhotoImage(file="jeubg.png")

# - Images du dos de la carte
carf = tk.PhotoImage(file="0.png")

# - Sorte de carte pour le joueur 1
sortec = random.randint(1, 2)

# - Sorte de carte pour le joueur 2
sortej2 = random.randint(1, 2)

# - Les images des cartes de pique
if sortec == 1:
    p2 = tk.PhotoImage(file="2.png")
    p3 = tk.PhotoImage(file="3.png")
    p4 = tk.PhotoImage(file="4.png")
    p5 = tk.PhotoImage(file="5.png")
    p6 = tk.PhotoImage(file="6.png")
    p7 = tk.PhotoImage(file="7.png")
    p8 = tk.PhotoImage(file="8.png")
    p9 = tk.PhotoImage(file="9.png")
    p10 = tk.PhotoImage(file="10.png")
    p11 = tk.PhotoImage(file="11.png")
    p12 = tk.PhotoImage(file="12.png")
    p13 = tk.PhotoImage(file="13.png")
    pA = tk.PhotoImage(file="A.png")

# - Les images des cartes de cœur
elif sortec == 2:
    p2 = tk.PhotoImage(file="2c.png")
    p3 = tk.PhotoImage(file="3c.png")
    p4 = tk.PhotoImage(file="4c.png")
    p5 = tk.PhotoImage(file="5c.png")
    p6 = tk.PhotoImage(file="6c.png")
    p7 = tk.PhotoImage(file="7c.png")
    p8 = tk.PhotoImage(file="8c.png")
    p9 = tk.PhotoImage(file="9c.png")
    p10 = tk.PhotoImage(file="10c.png")
    p11 = tk.PhotoImage(file="11c.png")
    p12 = tk.PhotoImage(file="12c.png")
    p13 = tk.PhotoImage(file="13c.png")
    pA = tk.PhotoImage(file="Ac.png")

# - Les images des cartes de trèfle
if sortej2 == 1:
    l2 = tk.PhotoImage(file="2t.png")
    l3 = tk.PhotoImage(file="3t.png")
    l4 = tk.PhotoImage(file="4t.png")
    l5 = tk.PhotoImage(file="5t.png")
    l6 = tk.PhotoImage(file="6t.png")
    l7 = tk.PhotoImage(file="7t.png")
    l8 = tk.PhotoImage(file="8t.png")
    l9 = tk.PhotoImage(file="9t.png")
    l10 = tk.PhotoImage(file="10t.png")
    l11 = tk.PhotoImage(file="11t.png")
    l12 = tk.PhotoImage(file="12t.png")
    l13 = tk.PhotoImage(file="13t.png")
    lA = tk.PhotoImage(file="At.png")

# - Les images des cartes de carreau
elif sortej2 == 2:
    l2 = tk.PhotoImage(file="2q.png")
    l3 = tk.PhotoImage(file="3q.png")
    l4 = tk.PhotoImage(file="4q.png")
    l5 = tk.PhotoImage(file="5q.png")
    l6 = tk.PhotoImage(file="6q.png")
    l7 = tk.PhotoImage(file="7q.png")
    l8 = tk.PhotoImage(file="8q.png")
    l9 = tk.PhotoImage(file="9q.png")
    l10 = tk.PhotoImage(file="10q.png")
    l11 = tk.PhotoImage(file="11q.png")
    l12 = tk.PhotoImage(file="12q.png")
    l13 = tk.PhotoImage(file="13q.png")
    lA = tk.PhotoImage(file="Aq.png")

# - Arrière-plan avec beaucoup de carte
tablebg = tk.Label(fenetre)
tablebg['image'] = jeubg
tablebg.place(x=-2, y=-2)

# - Les sortes de cartes pour joueur 1 ----------------------

# - La carte 2
if cartej1 == 1:

    # - Carte entre pique et cœur
    carte1 = p2

# - La carte 3
elif cartej1 == 2:

    # - Carte entre du trèfle et carreau
    carte1 = l3

# - La carte 4
elif cartej1 == 3:

    # - Carte entre pique et cœur
    carte1 = p4

# - La carte 5
elif cartej1 == 4:

    # - Carte entre du trèfle et carreau
    carte1 = l5

# - La carte 6
elif cartej1 == 5:

    # - Carte entre pique et cœur
    carte1 = p6

# - La carte 7
elif cartej1 == 6:

    # - Carte entre du trèfle et carreau
    carte1 = l7

# - La carte 8
elif cartej1 == 7:

    # - Carte entre pique et cœur
    carte1 = p8

# - La carte 9
elif cartej1 == 8:

    # - Carte entre du trèfle et carreau
    carte1 = l9

# - La carte 10
elif cartej1 == 9:

    # - Carte entre pique et cœur
    carte1 = p10

# - La carte 11
elif cartej1 == 10:

    # - Carte entre du trèfle et carreau
    carte1 = l11

# - La carte 12
elif cartej1 == 11:

    # - Carte entre pique et cœur
    carte1 = p12

# - La carte 13
elif cartej1 == 12:

    # - Carte entre du trèfle et carreau
    carte1 = l13

# - La carte A
elif cartej1 == 13:

    # - Carte entre pique et cœur
    carte1 = pA

# - Les sortes de cartes pour joueur 2 ----------------------

# - La carte 2
if cartej2 == 1:

    # - Carte entre du trèfle et carreau
    carte2 = l2

# - La carte 3
elif cartej2 == 2:

    # - Carte entre pique et cœur
    carte2 = p3

# - La carte 4
elif cartej2 == 3:

    # - Carte entre du trèfle et carreau
    carte2 = l4

# - La carte 5
elif cartej2 == 4:

    # - Carte entre pique et cœur
    carte2 = p5

# - La carte 6
elif cartej2 == 5:

    # - Carte entre du trèfle et carreau
    carte2 = l6

# - La carte 7
elif cartej2 == 6:

    # - Carte entre pique et cœur
    carte2 = p7

# - La carte 8
elif cartej2 == 7:

    # - Carte entre du trèfle et carreau
    carte2 = l8

# - La carte 9
elif cartej2 == 8:

    # - Carte entre pique et cœur
    carte2 = p9

# - La carte 10
elif cartej2 == 9:

    # - Carte entre du trèfle et carreau
    carte2 = l10

# - La carte 11
elif cartej2 == 10:

    # - Carte entre pique et cœur
    carte2 = p11

# - La carte 12
elif cartej2 == 11:

    # - Carte entre du trèfle et carreau
    carte2 = l12

# - La carte 13
elif cartej2 == 12:

    # - Carte entre pique et cœur
    carte2 = p13

# - La carte A
elif cartej2 == 13:

    # - Carte entre du trèfle et carreau
    carte2 = lA

# - Titre du joueur 1
joueurx1 = tk.Label(fenetre)
joueurx1['text'] = "Joueur 1"
joueurx1['foreground'] = "#ff0000"
joueurx1['bg'] = "#023502"
joueurx1['font'] = "Times 24 "
joueurx1.place(x=50, y=65)

# - Titre du joueur 2
joueurx2 = tk.Label(fenetre)
joueurx2['text'] = "Joueur 2"
joueurx2['foreground'] = "#ff0000"
joueurx2['bg'] = "#023502"
joueurx2['font'] = "Times 24 "
joueurx2.place(x=350, y=65)

# - Carte du joueur 1
carte = tk.Label(fenetre)
carte['image'] = carte1
carte.place(x=50, y=100)

# - Carte du joueur 2
carte = tk.Label(fenetre)
carte['image'] = carte2
carte.place(x=350, y=100)

# - Message d'acceuil
acceuil = tk.Label(fenetre)
acceuil['text'] = " Voici vos cartes pour le jeu vous être le joueur 1"
acceuil['foreground'] = "#ff0000"
acceuil['bg'] = "#023502"
acceuil['font'] = "Times 12"
acceuil.place(x=98, y=530)

# - Message d'explication
acceuil2 = tk.Label(fenetre)
acceuil2['text'] = "Appuyer sur la carte pour commencer une nouvelle partie."
acceuil2['foreground'] = "#ff0000"
acceuil2['bg'] = "#023502"
acceuil2['font'] = "Times 12"
acceuil2.place(x=74, y=550)

# - Sélectionner le gagnant est le Joueur 1
if cartej1>cartej2:

    # - message du gagnant
    message = "joueur 1 a gagné"

    # - Prends la carte et donne la carte
    joueur.append(joueur1[0])
    joueur1.pop(0)
    joueur.append(joueur[0])
    joueur.pop(0)

# - Sélectionner le gagnant est le Joueur 2
elif cartej1<cartej2:

    # - message du gagnant
    message = "joueur 2 a gagné"

    # - Prends la carte et donne la carte
    joueur1.append(joueur[0])
    joueur.pop(0)
    joueur1.append(joueur1[0])
    joueur1.pop(0)

# - Une bataille
elif cartej1==cartej2:

    # - Message qui dit qu'il a une bataille
    messagebat = tk.Label(fenetre)
    messagebat['text'] = "Bataille"
    messagebat['foreground'] = "#ff0000"
    messagebat['bg'] = "#023502"
    messagebat['font'] = "Times 24 "
    messagebat.place(x=200, y=100)

    # - Le dos des cartes Joueur 1
    carte0 = tk.Label(fenetre)
    carte0['image'] = carf
    carte0.place(x=50, y=200)

    # - Le dos des cartes Joueur 2
    carte0 = tk.Label(fenetre)
    carte0['image'] = carf
    carte0.place(x=350, y=200)

    # - les cartes qui sont sur la table
    bataillej1 = []
    bataillej2 = []

    # - Prends la carte et donne la carte
    bataillej1.append(cartej1)
    bataillej2.append(cartej2)
    joueur1.pop(0)
    joueur.pop(0)

    # - Une boucle jusqu'à tant qu'il y a un gagnant
    while cartej1 == cartej2:

        # - Prends la carte et donne la carte
        bataillej1.append(joueur[0])
        bataillej2.append(joueur1[0])
        joueur.pop(0)
        joueur1.pop(0)

        # - Prends la carte et donne la carte
        bataillej1.append(joueur[0])
        bataillej2.append(joueur1[0])

        # - Nouvelle carte
        cartej1 = joueur[0]
        cartej2 = joueur1[0]
        joueur.pop(0)
        joueur1.pop(0)

        # - Les sortes de cartes pour joueur 1 ----------------------

        # - La carte 2
        if cartej1 == 1:

            # - Carte entre pique et cœur
            carte1 = p2

        # - La carte 3
        elif cartej1 == 2:

            # - Carte entre du trèfle et carreau
            carte1 = l3

        # - La carte 4
        elif cartej1 == 3:

            # - Carte entre pique et cœur
            carte1 = p4

        # - La carte 5
        elif cartej1 == 4:

            # - Carte entre du trèfle et carreau
            carte1 = l5

        # - La carte 6
        elif cartej1 == 5:

            # - Carte entre pique et cœur
            carte1 = p6

        # - La carte 7
        elif cartej1 == 6:

            # - Carte entre du trèfle et carreau
            carte1 = l7

        # - La carte 8
        elif cartej1 == 7:

            # - Carte entre pique et cœur
            carte1 = p8

        # - La carte 9
        elif cartej1 == 8:

            # - Carte entre du trèfle et carreau
            carte1 = l9

        # - La carte 10
        elif cartej1 == 9:

            # - Carte entre pique et cœur
            carte1 = p10

        # - La carte 11
        elif cartej1 == 10:

            # - Carte entre du trèfle et carreau
            carte1 = l11

        # - La carte 12
        elif cartej1 == 11:

            # - Carte entre pique et cœur
            carte1 = p12

        # - La carte 13
        elif cartej1 == 12:

            # - Carte entre du trèfle et carreau
            carte1 = l13

        # - La carte A
        elif cartej1 == 13:

            # - Carte entre pique et cœur
            carte1 = pA

        # - Les sortes de cartes pour joueur 2 ----------------------

        # - La carte 2
        if cartej2 == 1:

            # - Carte entre du trèfle et carreau
            carte2 = l2

        # - La carte 3
        elif cartej2 == 2:

            # - Carte entre pique et cœur
            carte2 = p3

        # - La carte 4
        elif cartej2 == 3:

            # - Carte entre du trèfle et carreau
            carte2 = l4

        # - La carte 5
        elif cartej2 == 4:

            # - Carte entre pique et cœur
            carte2 = p5

        # - La carte 6
        elif cartej2 == 5:

            # - Carte entre du trèfle et carreau
            carte2 = l6

        # - La carte 7
        elif cartej2 == 6:

            # - Carte entre pique et cœur
            carte2 = p7

        # - La carte 8
        elif cartej2 == 7:

            # - Carte entre du trèfle et carreau
            carte2 = l8

        # - La carte 9
        elif cartej2 == 8:

            # - Carte entre pique et cœur
            carte2 = p9

        # - La carte 10
        elif cartej2 == 9:

            # - Carte entre du trèfle et carreau
            carte2 = l10

        # - La carte 11
        elif cartej2 == 10:

            # - Carte entre pique et cœur
            carte2 = p11

        # - La carte 12
        elif cartej2 == 11:

            # - Carte entre du trèfle et carreau
            carte2 = l12

        # - La carte 13
        elif cartej2 == 12:

            # - Carte entre pique et cœur
            carte2 = p13

        # - La carte A
        elif cartej2 == 13:

            # - Carte entre du trèfle et carreau
            carte2 = lA

        # - Afficher nouvelle carte pour Joueur 1
        titrepbt = tk.Label(fenetre)
        titrepbt['image'] = carte1
        titrepbt.place(x=50, y=300)

        # - Afficher nouvelle carte pour Joueur 2
        titrepbt = tk.Label(fenetre)
        titrepbt['image'] = carte2
        titrepbt.place(x=350, y=300)

        # - Détermine le gagnant de la bataille Joueur 2 gagne
        if cartej1 < cartej2:

            # - Prends la carte et donne la carte
            for b in bataillej1:
                joueur1.append(b)

            # - Prends la carte et donne la carte
            for b in bataillej2:
                joueur1.append(b)

            # - message du gagnant
            message = "joueur 2 a gagné"

        # - Détermine le gagnant de la bataille Joueur 1 gagne
        elif cartej1 > cartej2:

            # - Prends la carte et donne la carte
            for b in bataillej1:
                joueur.append(b)

            # - Prends la carte et donne la carte
            for b in bataillej2:
                joueur.append(b)

            # - message du gagnant
            message = "joueur 1 a gagné"

# - Le nombre de partie
touraffiche = tk.Label(fenetre)
touraffiche['text'] = "Parti : 1"
touraffiche['foreground'] = "#ff0000"
touraffiche['bg'] = "#023502"
touraffiche['font'] = "Arial 15"
touraffiche.place(x=5, y=10)

# - Nombre de partie
tour = 1

# - Prochaine partie -----------------------
def clic():

    # - Global joueur 1
    global joueur

    # - Arrière-plan avec beaucoup de cartes
    if len(joueur) > 10:

        # - Arrière-plan
        tablebg = tk.Label(fenetre)
        tablebg['image'] = jeubg
        tablebg.place(x=-2, y=-2)

    # - Arrière-plan avec moins de cartes
    elif len(joueur) <= 10:

        # - Arrière-plan
        tablebg = tk.Label(fenetre)
        tablebg['image'] = jeupeudecartebg
        tablebg.place(x=-2, y=-2)

    # - Titre du joueur 1
    joueurx1 = tk.Label(fenetre)
    joueurx1['text'] = "Joueur 1"
    joueurx1['foreground'] = "#ff0000"
    joueurx1['bg'] = "#023502"
    joueurx1['font'] = "Times 24 "
    joueurx1.place(x=50, y=65)

    # - Titre du joueur 2
    joueurx2 = tk.Label(fenetre)
    joueurx2['text'] = "Joueur 2"
    joueurx2['foreground'] = "#ff0000"
    joueurx2['bg'] = "#023502"
    joueurx2['font'] = "Times 24 "
    joueurx2.place(x=350, y=65)

    # - global tour
    global tour

    # - Compte le nombre de parties
    tour = tour + 1

    # - Affiche le nombre de parties
    touraffiche = tk.Label(fenetre)
    touraffiche['text'] = "Parti : {}". format(tour)
    touraffiche['foreground'] = "#ff0000"
    touraffiche['bg'] = "#023502"
    touraffiche['font'] = "Arial 15"
    touraffiche.place(x=5, y=10)

    # - global bouton
    global btnr

    # - Joueur 2 a gagné le jeu
    if len(joueur) == 0:

        # - Message de fin
        gagneparti = tk.Label(fenetre)
        gagneparti['text'] = "Vous avez perdu la partie contre le joueur 2"
        gagneparti['foreground'] = "#000000"
        gagneparti['bg'] = "#ffffff"
        gagneparti['height'] = 5
        gagneparti['font'] = "Times 20 "
        gagneparti.place(x=10, y=100)

        # - Disparaître le bouton
        btnr.place_forget()

    # - Joueur 1 a gagné le jeu
    elif len(joueur1) == 0:

        # - Message de fin
        gagneparti = tk.Label(fenetre)
        gagneparti['text'] = "Vous avez gagné la partie contre le joueur 2"
        gagneparti['foreground'] = "#000000"
        gagneparti['bg'] = "#ffffff"
        gagneparti['height'] = 5
        gagneparti['font'] = "Times 20 "
        gagneparti.place(x=10, y=100)

        # - Disparaître le bouton
        btnr.place_forget()

    # - Le jeu continue
    else:

        # - Carte de combat
        cartej1 = joueur[0]
        cartej2 = joueur1[0]

        # - Les sortes de cartes pour joueur 1 ----------------------

        # - La carte 2
        if cartej1 == 1:

            # - Carte entre pique et cœur
            carte1 = p2

        # - La carte 3
        elif cartej1 == 2:

            # - Carte entre du trèfle et carreau
            carte1 = l3

        # - La carte 4
        elif cartej1 == 3:

            # - Carte entre pique et cœur
            carte1 = p4

        # - La carte 5
        elif cartej1 == 4:

            # - Carte entre du trèfle et carreau
            carte1 = l5

        # - La carte 6
        elif cartej1 == 5:

            # - Carte entre pique et cœur
            carte1 = p6

        # - La carte 7
        elif cartej1 == 6:

            # - Carte entre du trèfle et carreau
            carte1 = l7

        # - La carte 8
        elif cartej1 == 7:

            # - Carte entre pique et cœur
            carte1 = p8

        # - La carte 9
        elif cartej1 == 8:

            # - Carte entre du trèfle et carreau
            carte1 = l9

        # - La carte 10
        elif cartej1 == 9:

            # - Carte entre pique et cœur
            carte1 = p10

        # - La carte 11
        elif cartej1 == 10:

            # - Carte entre du trèfle et carreau
            carte1 = l11

        # - La carte 12
        elif cartej1 == 11:

            # - Carte entre pique et cœur
            carte1 = p12

        # - La carte 13
        elif cartej1 == 12:

            # - Carte entre du trèfle et carreau
            carte1 = l13

        # - La carte A
        elif cartej1 == 13:

            # - Carte entre pique et cœur
            carte1 = pA

        # - Les sortes de cartes pour joueur 2 ----------------------

        # - La carte 2
        if cartej2 == 1:

            # - Carte entre du trèfle et carreau
            carte2 = l2

        # - La carte 3
        elif cartej2 == 2:

            # - Carte entre pique et cœur
            carte2 = p3

        # - La carte 4
        elif cartej2 == 3:

            # - Carte entre du trèfle et carreau
            carte2 = l4

        # - La carte 5
        elif cartej2 == 4:

            # - Carte entre pique et cœur
            carte2 = p5

        # - La carte 6
        elif cartej2 == 5:

            # - Carte entre du trèfle et carreau
            carte2 = l6

        # - La carte 7
        elif cartej2 == 6:

            # - Carte entre pique et cœur
            carte2 = p7

        # - La carte 8
        elif cartej2 == 7:

            # - Carte entre du trèfle et carreau
            carte2 = l8

        # - La carte 9
        elif cartej2 == 8:

            # - Carte entre pique et cœur
            carte2 = p9

        # - La carte 10
        elif cartej2 == 9:

            # - Carte entre du trèfle et carreau
            carte2 = l10

        # - La carte 11
        elif cartej2 == 10:

            # - Carte entre pique et cœur
            carte2 = p11

        # - La carte 12
        elif cartej2 == 11:

            # - Carte entre du trèfle et carreau
            carte2 = l12

        # - La carte 13
        elif cartej2 == 12:

            # - Carte entre pique et cœur
            carte2 = p13

        # - La carte A
        elif cartej2 == 13:

            # - Carte entre du trèfle et carreau
            carte2 = lA

        # - Affiche la carte du joueur 1
        carte = tk.Label(fenetre)
        carte['image'] = carte1
        carte.place(x=50, y=100)

        # - Affiche la carte du joueur 2
        carte = tk.Label(fenetre)
        carte['image'] = carte2
        carte.place(x=350, y=100)

        # - Apparaître le bouton
        btnr = tk.Button(fenetre)
        btnr['background'] = "#000000"
        btnr['image'] = carf
        btnr['command'] = clic
        btnr.place(x=200, y=370)

        # - Sélectionner le gagnant est le Joueur 1
        if cartej1 > cartej2:

            # - message du gagnant
            message = "joueur 1 a gagné"

            # - Prends la carte et donne la carte
            joueur.append(joueur1[0])
            joueur1.pop(0)
            joueur.append(joueur[0])
            joueur.pop(0)

        # - Sélectionner le gagnant est le Joueur 2
        elif cartej1 < cartej2:

            # - message du gagnant
            message = "joueur 2 a gagné"

            # - Prends la carte et donne la carte
            joueur1.append(joueur[0])
            joueur.pop(0)
            joueur1.append(joueur1[0])
            joueur1.pop(0)

        # - Une bataille
        elif cartej1==cartej2:

            # - Si le joueur 1 n'a pas assez de cartes pour faire une bataille
            if len(joueur) <= 2:

                # - Message pour avertir
                messagebaterr = tk.Label(fenetre)
                messagebaterr['text'] = "    Il a pas assez de carte pour faire une bataille donc le joueur 2 remporté le jeu par défaut    "
                messagebaterr['foreground'] = "#000000"
                messagebaterr['bg'] = "#ffffff"
                messagebaterr['height'] = 15
                messagebaterr['font'] = "Times 10 "
                messagebaterr.place(x=5, y=300)

            # - Si le joueur 2 n'a pas assez de cartes pour faire une bataille
            elif len(joueur1) <= 2:

                # - Message pour avertir
                messagebaterr = tk.Label(fenetre)
                messagebaterr['text'] = "    Il a pas assez de carte pour faire une bataille donc le joueur 1 remporté le jeu par défaut    "
                messagebaterr['foreground'] = "#000000"
                messagebaterr['bg'] = "#ffffff"
                messagebaterr['height'] = 15
                messagebaterr['font'] = "Times 10 "
                messagebaterr.place(x=5, y=300)

            # - Bataille
            else:

                # - Message qui dit qu'il a une bataille
                messagebat = tk.Label(fenetre)
                messagebat['text'] = "Bataille"
                messagebat['foreground'] = "#ff0000"
                messagebat['bg'] = "#023502"
                messagebat['font'] = "Times 24 "
                messagebat.place(x=200, y=100)

                # - Le dos des cartes Joueur 1
                carte0 = tk.Label(fenetre)
                carte0['image'] = carf
                carte0.place(x=50, y=200)

                # - Le dos des cartes Joueur 2
                carte0 = tk.Label(fenetre)
                carte0['image'] = carf
                carte0.place(x=350, y=200)

                # - les cartes qui sont sur la table
                bataillej1 = []
                bataillej2 = []

                # - Prends la carte et donne la carte
                bataillej1.append(cartej1)
                bataillej2.append(cartej2)
                joueur1.pop(0)
                joueur.pop(0)

                # - Une boucle jusqu'à tant qu'il y a un gagnant
                while cartej1 == cartej2:

                    # - Prends la carte et donne la carte
                    bataillej1.append(joueur[0])
                    bataillej2.append(joueur1[0])
                    joueur.pop(0)
                    joueur1.pop(0)

                    # - Prends la carte et donne la carte
                    bataillej1.append(joueur[0])
                    bataillej2.append(joueur1[0])

                    # - Nouvelle carte
                    cartej1 = joueur[0]
                    cartej2 = joueur1[0]
                    joueur.pop(0)
                    joueur1.pop(0)

                    # - Les sortes de cartes pour joueur 1 ----------------------

                    # - La carte 2
                    if cartej1 == 1:

                        # - Carte entre pique et cœur
                        carte1 = p2

                    # - La carte 3
                    elif cartej1 == 2:

                        # - Carte entre du trèfle et carreau
                        carte1 = l3

                    # - La carte 4
                    elif cartej1 == 3:

                        # - Carte entre pique et cœur
                        carte1 = p4

                    # - La carte 5
                    elif cartej1 == 4:

                        # - Carte entre du trèfle et carreau
                        carte1 = l5

                    # - La carte 6
                    elif cartej1 == 5:

                        # - Carte entre pique et cœur
                        carte1 = p6

                    # - La carte 7
                    elif cartej1 == 6:

                        # - Carte entre du trèfle et carreau
                        carte1 = l7

                    # - La carte 8
                    elif cartej1 == 7:

                        # - Carte entre pique et cœur
                        carte1 = p8

                    # - La carte 9
                    elif cartej1 == 8:

                        # - Carte entre du trèfle et carreau
                        carte1 = l9

                    # - La carte 10
                    elif cartej1 == 9:

                        # - Carte entre pique et cœur
                        carte1 = p10

                    # - La carte 11
                    elif cartej1 == 10:

                        # - Carte entre du trèfle et carreau
                        carte1 = l11

                    # - La carte 12
                    elif cartej1 == 11:

                        # - Carte entre pique et cœur
                        carte1 = p12

                    # - La carte 13
                    elif cartej1 == 12:

                        # - Carte entre du trèfle et carreau
                        carte1 = l13

                    # - La carte A
                    elif cartej1 == 13:

                        # - Carte entre pique et cœur
                        carte1 = pA

                    # - Les sortes de cartes pour joueur 2 ----------------------

                    # - La carte 2
                    if cartej2 == 1:

                        # - Carte entre du trèfle et carreau
                        carte2 = l2

                    # - La carte 3
                    elif cartej2 == 2:

                        # - Carte entre pique et cœur
                        carte2 = p3

                    # - La carte 4
                    elif cartej2 == 3:

                        # - Carte entre du trèfle et carreau
                        carte2 = l4

                    # - La carte 5
                    elif cartej2 == 4:

                        # - Carte entre pique et cœur
                        carte2 = p5

                    # - La carte 6
                    elif cartej2 == 5:

                        # - Carte entre du trèfle et carreau
                        carte2 = l6

                    # - La carte 7
                    elif cartej2 == 6:

                        # - Carte entre pique et cœur
                        carte2 = p7

                    # - La carte 8
                    elif cartej2 == 7:

                        # - Carte entre du trèfle et carreau
                        carte2 = l8

                    # - La carte 9
                    elif cartej2 == 8:

                        # - Carte entre pique et cœur
                        carte2 = p9

                    # - La carte 10
                    elif cartej2 == 9:

                        # - Carte entre du trèfle et carreau
                        carte2 = l10

                    # - La carte 11
                    elif cartej2 == 10:

                        # - Carte entre pique et cœur
                        carte2 = p11

                    # - La carte 12
                    elif cartej2 == 11:

                        # - Carte entre du trèfle et carreau
                        carte2 = l12

                    # - La carte 13
                    elif cartej2 == 12:

                        # - Carte entre pique et cœur
                        carte2 = p13

                    # - La carte A
                    elif cartej2 == 13:

                        # - Carte entre du trèfle et carreau
                        carte2 = lA

                    # - Afficher nouvelle carte pour Joueur 1
                    titrepbt = tk.Label(fenetre)
                    titrepbt['image'] = carte1
                    titrepbt.place(x=50, y=300)

                    # - Afficher nouvelle carte pour Joueur 2
                    titrepbt = tk.Label(fenetre)
                    titrepbt['image'] = carte2
                    titrepbt.place(x=350, y=300)

                    # - Détermine le gagnant de la bataille Joueur 2 gagne
                    if cartej1 < cartej2:

                        # - Prends la carte et donne la carte
                        for b in bataillej1:
                            joueur1.append(b)

                        # - Prends la carte et donne la carte
                        for b in bataillej2:
                            joueur1.append(b)

                        # - message du gagnant
                        message = "joueur 2 a gagné"

                    # - Détermine le gagnant de la bataille Joueur 1 gagne
                    elif cartej1 > cartej2:

                        # - Prends la carte et donne la carte
                        for b in bataillej1:
                            joueur.append(b)

                        # - Prends la carte et donne la carte
                        for b in bataillej2:
                            joueur.append(b)

                        # - message du gagnant
                        message = "joueur 1 a gagné"

        # - Affiche les messages du gagnant
        messagegg = tk.Label(fenetre)
        messagegg['text'] = "{}".format(message)
        messagegg['foreground'] = "#FF0000"
        messagegg['bg'] = "#023502"
        messagegg['font'] = "Times 20 "
        messagegg.place(x=160, y=250)

        # - Affiche le nombre de cartes du joueur 1
        nombrecartej1 = tk.Label(fenetre)
        nombrecartej1['text'] = "{}".format(len(joueur))
        nombrecartej1['foreground'] = "#FF0000"
        nombrecartej1['bg'] = "#023502"
        nombrecartej1['font'] = "Times 20 "
        nombrecartej1.place(x=235, y=525)

# - Bouton
btnr = tk.Button(fenetre)
btnr['background'] = "#000000"
btnr['image'] = carf
btnr['command'] = clic
btnr.place(x=200, y=370)

# - Affiche les messages du gagnant
messagegg = tk.Label(fenetre)
messagegg['text'] = "{}".format(message)
messagegg['foreground'] = "#FF0000"
messagegg['bg'] ="#023502"
messagegg['font'] = "Times 20 "
messagegg.place(x=160, y=250)

# - Ferme la fenêtre ------------------------------------------------------------
fenetre.mainloop()
