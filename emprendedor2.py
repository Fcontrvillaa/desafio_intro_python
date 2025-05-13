print ("Ingrese el precio de la suscripcion : ")
p = input()
p = float(p)

print ("Ingrese número de usuarios normales: ")
u_norm = input()
u_norm = float(u_norm)

print ("Ingrese número de usuarios premium: ")
u_prem = input()
u_prem = float(u_prem)

print ("Ingrese los gastos Totales: ")
gastos_totales = input()
gastos_totales = float(gastos_totales)

utilidades = p * (u_norm +  u_prem * 1.5) - gastos_totales

print(f"Las utilidades son  : {utilidades} ")