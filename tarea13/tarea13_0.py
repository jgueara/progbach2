#Leer una lista con 5 empleados
def cargarLista():
	empleados=[]
	empleado=[]
	for x in range(5):
		nombre=input("Introduce nombre:")
		sueldo1=int(input("Introduce sueldo 1:"))
		sueldo2=int(input("Introduce sueldo 2:"))
		sueldo3=int(input("Introduce sueldo 3:"))
		empleado.append(nombre);
		empleado.append((sueldo1,sueldo2,sueldo3))
		empleados.append(empleado)
	return empleados
#Imprimir elementos de la lista
def imprimir(empleados):
	for emp in empleados:
		print(emp[0]," tiene los siguientes sueldos:")
		for x in emp[1]:
			print(x)

empleados=cargarLista()
imprimir(empleados)
