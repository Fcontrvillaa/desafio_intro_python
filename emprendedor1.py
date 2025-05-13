
print ("Ingrese el precio de la suscripcion : ")
p = input()
p = float(p)

print ("Ingrese número de usuarios normales: ")
u = input()
u = float(u)

print ("Ingrese los gastos Totales: ")
gastos_totales = input()
gastos_totales = float(gastos_totales)

utilidades = p * u - gastos_totales

print(f"Las utilidades son  : {utilidades} ")