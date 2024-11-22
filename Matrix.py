class Matrix:
    # Initialisation d'une variable de type Matrix
    def __init__(self, dimension=100):
        self.N = dimension
        self.m = [[i if i==j else 0 for i in range(dimension)] for j in  range(dimension)]

    # Fonction qui renvoie la somme des élements d'une matrice
    def sum(self):
        return sum(sum(i) for i in self.m)

    # Représentation de la matrice en sortie
    def __str__(self):
        return f"Matrix({repr(self.m)})"

# Assertions
assert Matrix(3).m == [[0, 0, 0], [0, 1, 0], [0, 0, 2]]
assert all(Matrix(N).sum() == N*(N-1)//2 for N in range(10))

# Code Principal
Matrice = Matrix(3)
somme = Matrice.sum()

print(Matrice)
print(somme)
