
print ("Ingrese el precio de la suscripcion : ")
p = input()
p = float(p)

print ("Ingrese número de usuarios normales: ")
u = input()
u = float(u)

print ("Ingrese los gastos Totales: ")
gastos_totales = input()
gastos_totales = float(gastos_totales)

print ("Ingrese las utilidades del año anterior (debe ser distinto de 0): ")
u_anterior = input()
u_anterior = float(u_anterior)

utilidades = p * u - gastos_totales

razon = utilidades/u_anterior

print(f"Razón  : {razon:.2} ")