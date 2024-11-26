# Fonctions
def isPalindrome_sliced(s: str) -> bool:
    return s == s[::-1]

def isPalindrome(s: str) -> bool:
    return [s[i] for i in range(len(s)-1, -1, -1)] == [s[i] for i in range(0, len(s))]

def inverse(s: str) -> list[str]:
    return [s[i] for i in range(len(s)-1, -1, -1)]

def palinv(s: str|list[str]) -> bool:
    return list(s) == inverse(s)

def rmfrom(s: str, bad: str) -> list[str]:
    # return [s[i] for i in range(len(s)) if s[i] not in bad]
    # Ci-dessus, fonctionnel, mais génère une erreur sur un ensemble, car ceux-ci ne sont pas indexables
    return [character for character in s if character not in bad]

def rmspaces(s: list[str]|str) -> list[str]:
    return rmfrom(s, ' ')

def isPalindrome_sentence(s: str):
    return palinv(rmspaces(s))

def fsum(f, start: int, end: int) -> int:
    return sum(f(k) for k in range(start, end+1))


# Assertions
assert isPalindrome('abba')
assert isPalindrome('abcba')
assert isPalindrome('')
assert isPalindrome('a')
assert not isPalindrome('ab')

assert inverse('abc') == ['c','b','a']
assert inverse('') == []

assert palinv('abba')
assert palinv('abcba')
assert palinv('')
assert palinv('a')
assert not palinv('ab')

assert rmfrom('esope reste ici et se repose', 'aeiouy ') == ['s','p','r','s','t','c','t','s','r','p','s']

assert rmspaces('esope reste ici et se repose') == [ 'e', 's', 'o', 'p', 'e', 'r', 'e', 's', 't', 'e', 'i', 'c', 'i', 'e', 't', 's', 'e', 'r', 'e', 'p', 'o', 's', 'e']

assert isPalindrome_sentence('esope reste ici et se repose')
assert not isPalindrome_sentence('esope reste ici et se reposes')

assert fsum(lambda i:i, 0, 10) == 55
assert fsum (lambda i:i**2, 0, 10) == 385

# Code principal
print(isPalindrome("Test"))
print(inverse("Test"))
print(rmfrom('esope reste ici et se repose', 'aeiouy '))
print(rmspaces('esope reste ici et se repose'))
print(isPalindrome_sentence('esope reste ici et se repose'))
print(fsum(lambda i:i, 0, 10))