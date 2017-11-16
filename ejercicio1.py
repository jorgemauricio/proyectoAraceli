def multiplicarVariables(x, y):
	return x * y

def variableMayor(x,y):
	'''
	Regresa el comparativo de las variables
	mayor, menor o igual
	param: x : valor de x
	param: y : valor de y
	'''
	if x == y:
		print("x y y son iguales")
	elif x > y:
		print("x es mayor a y")
	else:
		print("y es mayor a x")

x = int(input("Dame el valor de x: "))
y = int(input("Dame el valor de y: "))

print("La multiplicación de x = {} y y = {} es: {}".format(x,y, multiplicarVariables(x,y))) 

# imprimir la variable mayor
variableMayor(x,y)
