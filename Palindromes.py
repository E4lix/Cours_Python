# Fonctions
def isPalindrome_sliced(s: str):
    return s == s[::-1]

def isPalindrome(s: str):
    return [s[i] for i in range(len(s)-1, -1, -1)] == [s[i] for i in range(0, len(s))]

def inverse(s: str):
    return [s[i] for i in range(len(s)-1, -1, -1)]

def palinv(s: str):
    return list(s) == inverse(s)

def rmfrom(s: str, bad: str):
    # return [s[i] for i in range(len(s)) for j in range(len(bad)) if bad[j] != s[i]]
    return [character for character in s if character not in bad]

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

# Code principal
print(isPalindrome("Test"))
print(inverse("Test"))
print(rmfrom('esope reste ici et se repose', 'aeiouy '))