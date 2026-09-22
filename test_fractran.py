from pytest import approx

from fractran import Fraction
from fractran import Facteur
from fractran import Fractran


def test_Fraction_constructeur():
    assert isinstance(Fraction(7, 5), Fraction)


def test_Fraction_init():
    assert Fraction(1, 2).numerateur == 1
    assert Fraction(1, 2).denominateur == 2


def test_Fraction_est_entier():
    assert Fraction(1, 2).est_entier(2)
    assert not Fraction(1, 3).est_entier(2)


def test_Fraction_valeur():
    assert Fraction(3, 2).valeur(4) == 3 * (4 // 2)


def test_Facteur_constructeur():
    assert isinstance(Facteur([2, 3, 7]), Facteur)


def test_Facteur_init():
    assert Facteur([2, 3, 7]).facteurs == [2, 3, 7]


def test_Facteur_nombre():
    assert Facteur([2, 3, 7]).nombre([1, 2]) == (2**1) * (3**2)
    assert Facteur([2, 3, 7]).nombre([1, 2, 3]) == (2**1) * (3**2) * (7**3)


def test_Facteur_décomposition():
    assert Facteur([2, 3, 7]).decomposition(1) == [0, 0, 0]
    assert Facteur([2, 3, 7]).decomposition((2**3) * (3**2) * (7)) == [3, 2, 1]


def test_Fractran_constructeur():
    assert isinstance(Fractran([Fraction(2, 3), Fraction(6, 4)]), Fractran)


def test_Fractran_init():
    assert Fractran([Fraction(2, 3), Fraction(6, 4)]).programme[0].denominateur == 3
    assert Fractran([Fraction(2, 3), Fraction(6, 4)]).programme[0].numerateur == 2
    assert Fractran([Fraction(2, 3), Fraction(6, 4)]).programme[1].denominateur == 4
    assert Fractran([Fraction(2, 3), Fraction(6, 4)]).programme[1].numerateur == 6


def test_Fractran_run_une_fraction():
    assert Fractran([Fraction(3, 11)]).run(13) == 13
    assert Fractran([Fraction(2, 10)]).run(150) == 6


def test_Fractran_run_deux_fractions():
    assert Fractran([Fraction(3, 10), Fraction(4, 3)]).run(14) == 14
    assert Fractran([Fraction(3, 10), Fraction(4, 3)]).run(15) == 8


def test_Fractran_suite():
    assert Fractran([Fraction(3, 10), Fraction(4, 3)]).suite(15, 2) == [15, 20]
    assert Fractran([Fraction(3, 10), Fraction(4, 3)]).suite(15, 7) == [15, 20, 6, 8]
