# Fonctions
def isPalindrome(s: str):
    return s == s[::-1]

def inverse(s: str):
    return [s[i] for i in range(len(s)-1,-1, -1)]

# Assertions
assert isPalindrome('abba')
assert isPalindrome('abcba')
assert isPalindrome('')
assert isPalindrome('a')
assert not isPalindrome('ab')

assert inverse('abc') == ['c','b','a']
assert inverse('') == []

# Code principal
print(isPalindrome("Test"))
print(inverse("Test"))