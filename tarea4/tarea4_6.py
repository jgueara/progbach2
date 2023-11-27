x=1
sumaLista1=0
sumaLista2=0
while x<=5:
	valor=int(input("Introduce un valor de la lista 1:"))
	x=x+1
	sumaLista1=sumaLista1+valor

x=1
while x<=5:
	valor=int(input("Introduce un valor de la lista 2:"))
	x=x+1
	sumaLista2=sumaLista2+valor
if sumaLista1>sumaLista2:
	print("La lista 1 es mayor con un valor acumulado:",sumaLista1)
else:
	if sumaLista1<sumaLista2:
		print("La lista 2 es mayor con un valor acumulado:",sumaLista2)
	else:
		print("Ambas listas son iguales con un valor acumulado:",sumaLista1)
