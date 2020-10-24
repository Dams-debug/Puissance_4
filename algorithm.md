# Algorithme du jeu puissance 4
-----------------

## Descriptif

- 1 plateau de jeu composé de 6 lignes et 7 colonnes ;
- 2 joueurs s'affrontent (l'un a des jetons jaune et l'autre des jetons rouge) ;
- Les joueurs qui s'affrontent jouent à tour de rôle ;
- Le premier qui réussi à aligner 4 jetons de sa couleur remporte la partie.

## Décomposition du projet


## 1 | Création et affichage du plateau de jeu et premières variables.


* 1 variable qui représente le plateau de jeu sous forme de liste :
[
    [_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_],
].
* 1 variable qui représente le joueur ayant des jetons jaune.
* 1 variable qui représente le joueur ayant des jetons rouge.

* Pour afficher le plateau de jeu il faut faire une boucle qui permet l'affichage des lignes du tableau.

## 2 | Savoir si un emplacement est libre ou non.
-----------------
Cette partie va permettre au programme de savoir à quelle position le jeton doit se retrouver lorsque le joueur décide de le lâcher dans une colonne (la gravité ;-)). En effet, si un ou plusieurs jetons sont déjà présents dans la colonne choisie par le joueur, ce dernier se retrouvera au-dessus des autres.

* Créer une seconde liste qui permet, par itération, de savoir combien d'emplacements sont vides dans chaque colonne. Chaque occurrence dans les sous-listes de la seconde liste, représentera un emplacement vide dans le tableau de jeu.
* Si dans une colonne, le nombre d'occurences est inférieur à 6, un ou plusieurs jetons sont déjà présents dans la colonne choisie par le joueur.

## 3 | Permettre aux joueurs de jouer l'un après l'autre.

Une simple boucle while permet aux utilisateurs de jouer tour après tour.

## 4 | Savoir si un joueur a gagné et arrêter la partie.

Un joueur remporte la partie si il aligne 4 jetons. Ils peuvent être aligné horizontalement, verticalement ou sur les diagonales (gauche, droite). 

* 4 jetons sont alignés à l'horizontale ;
* 4 jetons sont alignés à la verticale ;
* 4 jetons sont alignés sur l'une des diagonales.
