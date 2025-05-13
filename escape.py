import math

velocidad_escape = float(0)


print ("Ingrese el radio en Kilometros : ")
r = input()
r = float(r)*1000

print ("Ingrese la constante g (m/s2): ")
g = input()
g = float(g)


velocidad_escape = math.sqrt(2*g*r)
velocidad_escape = round(velocidad_escape, 1)
print(f"La Velocidad de Escape es : {velocidad_escape} [m/s\u00b2]")
