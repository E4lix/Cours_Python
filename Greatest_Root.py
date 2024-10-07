import math

def greatest_root(a, b, c):
    assert a != 0
    
    # Calcul de Delta
    delta = b**2 - 4 * a * c

    # Calcul des racines
    if delta > 0:
        racine1 = (-b - math.sqrt(delta))/(2*a)
        racine2 = (-b + math.sqrt(delta))/(2*a)
        
        # Renvoie de la plus grande racine
        return max(racine1, racine2)
                   
    elif delta == 0:
        racine = -b/(2*a)
        return racine
    else:
        return None

    
assert greatest_root(1, 1, 1) == None
assert greatest_root(1, -2, 1) == 1
assert greatest_root(4, -4, -24) == 3

