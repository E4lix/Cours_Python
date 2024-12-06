"""
2+2 # Ne renvoie rien
print(2+2) # Résultat puis retour à la ligne
print(print(2+2), print(2+2)) # Evalue d'abord les paramètres des prints de gauche à droite
l = [1+i for i in range(3)] # Ne renvoie rien (pas d'effet de bord)
pl = [print(1+i) for i in range(3)] # Renvoie les prints des chiffres de 1 à 3
print(l, pl) # l renvoie une liste de 1 à 3, pl renvoie une liste vide (None)

Fonction avec effet de bord
Procédure pas d'effet de bord
"""

"""
print(set('totto')) # Renvoie les élements en paramètres du set (ensemble) de manière unique
print({'totto'}) # Renvoie le contenu des parenthèses
# print({{'toto'}, {'tata'}}) # Renvoie une erreur
print('abcde'[-1]) # Renvoie le dernier élement du print
# print({'abcde'}[0][1]) # Renvoie une erreur (ensemble non indexable)
print('abcdefg'[2:5]) # Renvoie uniquement les éléments d'indice 2 à 5
print((list('abcdefg')*3)[2:5]) # Renvoie une liste des éléments d'indice 2 à 5
print((list('abcdefg')*3)[19:22]) # Renvoie une liste des éléments d'indice 19 à 21 car pas d'éléments 22
print('abcdefg'[-5:-2]) # Renvoie uniquement les éléments d'indice -5 à -2
print(list(range(12))[13:5:-2]) # Renvoie une liste des éléments d'indice 13 à 5 avec un pas de -2
print({0:1, None:2, False:5}) # What the fuck, False peut être une clé de dictionnaire, par contre,
# et 0 ont le même hash, donc le dico à deux éléments avec 2 fois la même clé
"""

"""
s = { print(i) for i in range(1,3) }
ss = { (i,print(i)) for i in range(1,3) }
sss = { (i,i,print(i)) for i in range(1,3) }
print(s,ss,sss,sep='\n')
"""

p = "oyoyoyoyo"
Test = True if len(p) == 0 else not False in {True if p[j] == p[len(p)-j-1] else False for j in range(len(p)//2)}

print(Test)