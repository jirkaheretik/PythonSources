"""
Vypocita koreny kvadraticke rovnice
"""
import math

# Zadani koeficientu:
print("Zadej koeficient a:")
a = int(input())
print("Zadej koeficient b:")
b = int(input())
print("Zadej koeficient c:")
c = int(input())
if a == 0:
    print("Není kvadratická rovnice")
else:
    d = b * b - 4 * a * c
    if d == 0:
        print("Rovnice má jeden kořen")
        print (-b / (2 * a))
    elif d < 0:
        print("Rovnice nemá řešení v oboru reálných čísel")
    else:
        print("Rovnice má dva kořeny:")
        odm = math.sqrt(d)
        print((-b + odm)/(2 * a))
        print((-b - odm)/(2 * a))
