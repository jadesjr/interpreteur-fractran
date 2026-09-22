class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def est_entier(self, n):
        return n % self.denominateur == 0

    def valeur(self, n):
        return self.numerateur * (n // self.denominateur)


class Facteur:
    def __init__(self, facteurs):
        self.facteurs = facteurs

    def nombre(self, L):
        produit = 1
        for i in range(0, len(L)):
            produit = produit * (self.facteurs[i] ** L[i])
        return produit

    def decomposition(self, n):
        L = []
        for facteur in self.facteurs:
            d = 0
            while n % facteur == 0:
                d += 1
                n = n // facteur
            L.append(d)
        return L


class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):

            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n, N):
        L = []
        if N == 0:
            return L
        L.append(n)
        i = 0
        while len(L) < N and i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
                L.append(n)
            else:
                i += 1
        return L
