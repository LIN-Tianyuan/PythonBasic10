a = int(input("Veuillez entrer un nombre a: "))
# == signifie: est égal à
# = sert à affectuer une valeur
# Si un nombre est pair, it est divisible par 2.
# Donc a % 2, si le résultat vaut 0, le nombre est pair.
if a % 2 == 0:
    print("a est pair.")
# Sinon, it est impair.
else:
    print("a est impair.")