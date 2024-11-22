from collections import defaultdict

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

class sMatrix:
    # Initialisation d'une variable de type sMatrix (Sparse Matrix)
    def __init__(self, dimension=100):
        self.N = dimension
        self.m = defaultdict(lambda: 0, {(i, i):i for i in range(1, self.N)})

    # Fonction qui renvoie la somme des élements d'une smatrice
    def sum(self):
        return sum(self.m[(i,i)] for i in range(1, self.N))

    # Renvoie la liste des listes de la smatrice
    def full_matrix(self):
        return [[self.m[(i,j)] for i in range(self.N)] for j in range(self.N)]

    # Représentation de la matrice en sortie
    def __repr__(self):
        return f"sMatrix({repr(self.full_matrix())})"

# Assertions
assert Matrix(3).m == [[0, 0, 0], [0, 1, 0], [0, 0, 2]]
assert all(Matrix(N).sum() == N*(N-1)//2 for N in range(10))

assert type(sMatrix(3).m) is defaultdict
assert sMatrix(3).m == {(1, 1): 1, (2, 2): 2}
assert sMatrix(3).m[(999, 999)] == 0
assert all(sMatrix(N).full_matrix() == Matrix(N).m for N in range(10))
#assert all(repr(sMatrix(N)) == "s"+repr(Matrix(N)) for N in range(10))

# Code Principal
Matrice = Matrix(3)
somme = Matrice.sum()
print(Matrice)
print(somme)

sMatrice = sMatrix(3)
somme = sMatrice.sum()
print(sMatrice)
print(somme)
print(sMatrice.full_matrix())