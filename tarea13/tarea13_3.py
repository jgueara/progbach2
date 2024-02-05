#Leer una lista de 5 empleados nombre y tres sueldos
#empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
def cargar_empleados():
	empleados=[]
	for x in range(3):
		nombre=input("Introduce un nombre:")
		sueldo1=int(input("Introduce el primer sueldo:"))
		sueldo2=int(input("Introduce el segundo sueldo:"))
		sueldo3=int(input("Introduce el tercer sueldo:"))
		empleado=[]
		empleado.append(nombre)
		empleado.append((sueldo1,sueldo2,sueldo3))
		empleados.append(empleado)
	return empleados

#Visualizar el mayor sueldo de dos empleados
#Juan tiene un sueldo trimestral de 9233
def visualizar(empleados):
	for empleado in empleados:
		total=0
		for sueldo in empleado[1]:
			total=total+sueldo
		print(empleado[0]," tiene un sueldo trimestral de ",total)

#Visualizar empleados con un monto trimestral mayor a 10000
def visualizarSuperior(empleados):
	print("Los empleados con un monto trimestral superior a 10000 son:")
	for empleado in empleados:
		total=0
		for sueldo in empleado[1]:
			total=total+sueldo
		if total>10000:
			print(empleado[0]," tiene un sueldo trimestral de ",total)

#Programa principal
empleados=cargar_empleados()
visualizar(empleados)
visualizarSuperior(empleados)



