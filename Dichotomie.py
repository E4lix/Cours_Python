from math import nextafter as na, inf

# Définitions des fonctions
def di_recursif(f, a, b, d=1e-16):
    # Moitié de l'intervalle
    m = (a+b)/2

    if abs(a - b) <= d or m in (a,b): 
        return m

    if f(m) == 0: # m est la racine que l'on recherche
        return m
    elif f(m) * f(a) < 0:  # La racine est dans [a, m]
        return di_recursif(f, a, m)
    else:  # La racine est dans [m, b]
        return di_recursif(f, m, b)

def di_while(f, a, b, d=1e-16):
    m = (a+b)/2
    while abs(b-a) > d and not(m in (a,b)):    
        if f(m) == 0:
            return m
        elif f(m) * f(a) <= 0:
            b = m
        elif f(m) * f(b) <= 0:
            a = m   
        m = (a+b)/2
    return m

def f(x):
    return x**2 - 2

def neigh(f): 
    return na(f,inf), na(f,-inf)

assert all(abs(n**.5 - (r := di_recursif(lambda x : x**2-n, 0, 99, d))) <= d
    or r in neigh(n**.5) # result is closest float
    for di in [di_recursif , di_while]
    for n in range(1, 20) for d in [1e-7, 1e-16, 1e-32] ), r

def find(x, l):
    debut = 0
    fin = len(l) - 1

    milieu = (debut + fin)//2
    print(milieu)

    if debut == fin:
        return milieu

    if l[milieu] == x:
        return milieu
    elif l[milieu] > x:
        return find(x, l[milieu+1:fin])
    else:
        return find(x, l[debut:milieu-1])
        
# assert find(3,[3]) == 0

# assert all( (fe:=find(ie:=i,ir:=r)) == (i if 0<=i<N else None)
#     for N in range(9) for r in [range(N)]
#     for i in list(r)+[-1,N] ), (ir, ie, fe)

# assert all( l[fe:=find(ie:=i,il:=l)] == i
#     for N in range(5) for R in [2,3]
#     for l in [[ e for e in range(N) for _ in range(R) ]]
#     for i in range(N)), (il, ie, fe)


# Programme principal

# Racine1 = di_recursif(f, 0, 12)
# Racine2 = di_while(f, 0, 12)
# print(Racine1, Racine2)

print(len([1, 3, 4, 5, 7, 8, 9, 10, 23, 34, 45, 54]))
print(find(5, [1, 3, 4, 5, 7, 8, 9, 10, 23, 34, 45, 54]))