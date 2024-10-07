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


def roots(a, b, c):
    # Calcul de delta
    delta = b**2 - 4 * a * c

    # Calcul des racines
    if delta > 0:
        racine1 = (-b - math.sqrt(delta))/(2*a)
        racine2 = (-b + math.sqrt(delta))/(2*a)

        return (racine1, racine2)
                   
    elif delta == 0:
        racine = -b/(2*a)
        
        return (racine,)
    
    else:
        return ()
    

assert roots(1,1,1) == ()
assert roots(1,-2,1) in [(1,1), (1,)]
assert set(roots(4,-4,-24)) == {-2, 3}

for a in (-5, 6):
    if a != 0:
        for b in (-5, 6):
            for c in (-5, 6):
                if greatest_root(a, b, c) != None:
                    assert greatest_root(a, b, c) == max(roots(a, b, c), default = None)
                if greatest_root(a, b, c) == None:
                    assert roots(a, b, c) == ()
                    
# Version optimisée
assert all(max(roots(a,b,c)) == greatest_root(a,b,c)
           if roots(a,b,c) != ()
           else greatest_root(a,b,c) is None
           for r in [range(-5,6)]
           for a in r if a != 0 for b in r for c in r)
