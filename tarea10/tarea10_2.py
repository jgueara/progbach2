# Definir lista vacia
nombres=[]
notas=[]
# Agregamos 10 nombre de alumnos y notas
for x in range(10):
	nombre=input("Introduce un nombre:")
	nombres.append(nombre)
	nota=int(input("Introduce un nota:"))
	notas.append(nota)
# Visualizar Suspensos y Aprobados
print("Alumnos aprobados:")
for x in range(10):
	if notas[x]>=5:
		print(nombres[x]," ",notas[x])

print("Alumnos suspensos:")
for x in range(10):
	if notas[x]<5:
		print(nombres[x]," ",notas[x])



