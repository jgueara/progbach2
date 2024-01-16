# Definir lista vacia
nombres=[]
sueldos=[]
# Agregamos 5 nombre y sueldos
for x in range(5):
	nombre=input("Introduce un nombre:")
	nombres.append(nombre)
	valor=int(input("Introduce un sueldo:"))
	sueldos.append(valor)
# Visualizar la persona con mayor sueldo y con menor sueldo
mayor=0
menor=9999999
posMayor=0
posMenor=0
for x in range(5):
	if sueldos[x]>mayor:
		mayor=sueldos[x]
		posMayor=x
	if sueldos[x]<menor:
		menor=sueldos[x]
		posMenor=x
print("El sueldo mayor es ",mayor," y pertenece a ",nombres[posMayor])
print("El sueldo menor es ",menor," y pertenece a ",nombres[posMenor])


