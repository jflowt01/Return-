# Saludo con y sin return

def saludar_sin(nombre: str):
    print(f"Hola sin return, {nombre} tipo: {type(nombre)}")

mensaje0=saludar_sin("Ana")
print (f"Mensaje sin return: {mensaje0} tipo: {type(mensaje0)}")

def saludar_con(nombre: str):
    return f"Hola con return, {nombre} tipo: {type(nombre)}"

mensaje = saludar_con("Ana")
print(mensaje)


#Suma de dos numeros con y sin return

def sumar_sin(a: int, b: int):
    print(f"Resultado sin return: {a + b} tipo: {type(a + b)}")

sumar1=sumar_sin(5, 3)
print(f"Resultado sin return: {sumar1} tipo: {type(sumar1)}")

def sumar_con(a: int, b: int):
    return a + b

numeros = sumar_con(5, 3)
print(f"Resultado con return: {numeros} tipo: {type(numeros)}")



# Calcular doble de un numero con y sin return

def doble_sin(numero: int):
    print(f"Resultado sin return: {numero * 2} tipo: {type(numero * 2)}")

doble1=doble_sin(10)
print(f"Resultado sin return: {doble1} tipo: {type(doble1)}")

def doble_con(numero: int):
    return numero * 2

resultado = doble_con(10)
print(f"Resultado con return: {resultado} tipo: {type(resultado)}")


