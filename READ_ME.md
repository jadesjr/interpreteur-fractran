# Projet "Interpréteur FRACTRAN"

## À propos

Ce projet contient un interpréteur FRACTRAN. Il permet d'exécuter des programmes de fractions  pour faire des calculs comme des sommes, et des produits. Il permet aussi de générer des suites comme la suite de fibonacci et des nombres premiers.

## Utilisation

Exécutez le fichier `main.py`.

## Explication fibonacci
fibonacci est entre guillemets le programme en FRACTRAN pour calculer la suite de Fibonacci.
Pour commencer, on exécute le FRACTRAN avec les fractions contenues dans la liste du programme fibonacci et avec comme n initial 3. On utilise la fonction suite pour avoir tous les résultats intermédiaires générés par la méthode.
On se retrouve donc avec une suite de longueur égale à 1 000.Certains contiennent de manière indirecte les termes de la suite de Fibonacci et d'autres non. 
On va donc filtrer la liste pour n'avoir que les termes de la suite de Fibonacci. On cherche à décomposer chaque nombre en produit de facteurs premiers 2 et 3 (fonction decomposition()), puis on le reconstruit avec ce produit de facteurs premiers (fonction nombre()).
Si le nombre reste le même, c'est qu'on peut l'écrire sous la forme 2^a * 3^b et donc il contient des informations sur des termes de la suite de Fibonacci. On récupère donc les exposants a et b qui représentent deux termes consécutifs dans la suite de Fibonacci.