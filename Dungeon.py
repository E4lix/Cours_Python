import math
from random import *
from collections import Counter

class d:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"{self.n} : {self.roll()}"    
    
    def roll(self):
        return randint(1,self.n)

    def __int__(self):
        return self.roll()

    def __add__(self, other):
        return self.roll() + other
    
    def __radd__(self, other):
        return other + self.roll()
    
    def __mul__(self, other):
        return self.roll() * other

    def __rmul__(self, other):
        """
        resultat = 0
        for i in range(0, other):
            resultat = resultat + self.roll()
        """
        return sum(self.roll() for i in range(0, other))
    
# Programme Général
N = 100000

d6 = d(6)
d20 = d(20)

print(d20)

for v, c in (l := sorted(Counter( 3*d6 for _ in range(N)).items())):
    print(f"{v:2} {'='*(c//500)}")

print("\nAverage : ", sum(c*v for v,c in l)/N,
      "\nExpected Average : ", 3/6*sum(range(1,6+1)), "=", 3*(6+1)/2)

print(3*d6+0, 3*(d6+0))