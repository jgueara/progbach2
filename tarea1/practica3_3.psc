Algoritmo mayor3Numeros
	Escribir "Introduce un número:"
	Leer num1
	Escribir "Introduce otro número:"
	Leer num2
	Escribir "Introduce el tercer número:"
	Leer num3
	Si num1>num2 Entonces
		Si num1>num3 Entonces
			Escribir "El mayor es ",num1
		SiNo
			Escribir "El mayor es ",num3
		Fin Si
	SiNo
		Si num2>num3 Entonces
			Escribir "El mayor es ",num2
		SiNo
			Escribir "El mayor es ",num3
		Fin Si
	Fin Si
FinAlgoritmo
