# Fonctions
def crange(a: str, b: str):
    return (chr(i) for i in range(ord(a), ord(b)+1))

def charrange(*args: list):
    for i in range(0, len(args), 2):
        yield from crange(args[i], args[i+1])

# Assertions
assert "".join(crange('A', 'Z')) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert next(crange("a","b")) == "a"

assert "".join(charrange('A','Z','a','z','0','9')) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
assert next(charrange("a","b")) == "a"
assert "".join(charrange()) == ''

# Code principal
print("".join(crange('A', 'Z')))
print("".join(charrange('A','Z','a','z','0','9')))