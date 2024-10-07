def F_to_C(Fahrenheit):
    assert -459.67 <= Fahrenheit, "Valeur en dessous du Zéro absolu en Fahrenheit"
    Celsius = (5 * (Fahrenheit - 32))/9
    return Celsius

def C_to_F(Celsius):
    assert -273.15 <= Celsius, "Valeur en dessous du Zéro absolu en Celsius"
    Fahrenheit = (9/5)*Celsius + 32
    return Fahrenheit

def isalmost(n, m):
    d = 1e-13
    if abs(n - m) > d:
        return False
    else:
        return True


assert isalmost(F_to_C(-459.67), -273.15)
assert isalmost(C_to_F(-273.15), -459.67)
assert all(isalmost(efc:= F_to_C(C_to_F(c)), ec := c)
            and isalmost( efc := C_to_F(F_to_C(c)), c)
            for c in range(-273, 200) ), (ec, efc)
            
