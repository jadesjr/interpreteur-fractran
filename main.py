from fractran import Fraction
from fractran import Facteur
from fractran import Fractran

facteurs = Facteur([2, 3, 5])

## somme
somme = [Fraction(3, 2)]
# essaie sur le cas 3+4
resultat = Fractran(somme).run(facteurs.nombre([3, 4]))
somme_3_4 = facteurs.decomposition(resultat)[1]
print(somme_3_4)


# sommes i+j pour tout les entiers i,j tel que 1<=i,j<=10
def fct_somme(i, j):
    resultat = Fractran(somme).run(facteurs.nombre([i, j]))
    somme_ij = facteurs.decomposition(resultat)[1]
    return somme_ij


for i in range(1, 11):
    for j in range(1, 11):
        print(str(i) + "+" + str(j) + "=" + str(fct_somme(i, j)))


## produits i*j pour les entiers i,j tel que 1<=i,j<=10 - option1
for i in range(1, 11):
    for j in range(1, 11):
        produit = 0
        for _ in range(i):
            produit = fct_somme(produit, j)
        print(str(i) + "*" + str(j) + "=" + str(produit))

## produits i*j pour les entiers i,j tel que 1<=i,j<=10 - option2
# essaie sur le cas 2*3
produit = [
    Fraction(455, 33),
    Fraction(11, 13),
    Fraction(1, 11),
    Fraction(3, 7),
    Fraction(11, 2),
    Fraction(1, 3),
]
resultat = Fractran(produit).run(facteurs.nombre([2, 3]))
produit_2_3 = facteurs.decomposition(resultat)[2]
print(produit_2_3)

# code pour tout les i,j
for i in range(1, 11):
    for j in range(1, 11):
        resultat = Fractran(produit).run(facteurs.nombre([i, j]))
        produit_ij = facteurs.decomposition(resultat)[2]
        print(str(i) + "*" + str(j) + "=" + str(produit_ij))


##suite Fibonacci
print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [
    Fraction(23, 95),
    Fraction(57, 23),
    Fraction(17, 39),
    Fraction(130, 17),
    Fraction(11, 14),
    Fraction(35, 11),
    Fraction(19, 13),
    Fraction(1, 19),
    Fraction(35, 2),
    Fraction(13, 7),
    Fraction(7, 1),
]
sortie_brute = Fractran(fibonacci).suite(3, 1000)
sortie = []
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).decomposition(n)):
        sortie.append(Facteur([2, 3]).decomposition(n))
print(sortie)


##Nombres premiers avec l'algorithme de Conway
fractions_conway = [
    Fraction(17, 91),
    Fraction(78, 85),
    Fraction(19, 51),
    Fraction(23, 38),
    Fraction(29, 33),
    Fraction(77, 29),
    Fraction(95, 23),
    Fraction(77, 19),
    Fraction(1, 17),
    Fraction(11, 13),
    Fraction(13, 11),
    Fraction(15, 2),
    Fraction(1, 7),
    Fraction(55, 1),
]
sortie_brute = Fractran(fractions_conway).suite(2, 100000)
nombres_premiers = []
for n in sortie_brute:
    if n == Facteur([2]).nombre(Facteur([2]).decomposition(n)):
        nombre_premier = Facteur([2]).decomposition(n)[0]
        if nombre_premier != 1 and nombre_premier not in nombres_premiers:
            nombres_premiers.append(nombre_premier)

print("les nombres premiers trouvés pour 100000 nombres rendu par le programme :")
print(nombres_premiers)
