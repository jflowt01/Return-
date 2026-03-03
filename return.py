# Saludo con y sin return

def saludar_sin(nombre: str):
    print(f"Hola sin return, {nombre} tipo: {type(nombre)}")

saludar_sin("Ana")

def saludar_con(nombre: str):
    return f"Hola con return, {nombre} tipo: {type(nombre)}"

mensaje = saludar_con("Ana")
print(mensaje)


#Suma de dos numeros con y sin return

def sumar_sin(a: int, b: int):
    print(f"Resultado sin return: {a + b} tipo: {type(a + b)}")

sumar_sin(5, 3)

def sumar_con(a: int, b: int):
    return a + b

numeros = sumar_con(5, 3)
print(f"Resultado con return: {numeros} tipo: {type(numeros)}")



# Calcular doble de un numero con y sin return

def doble_sin(numero: int):
    print(f"Resultado sin return: {numero * 2} tipo: {type(numero * 2)}")

doble_sin(10)

def doble_con(numero: int):
    return numero * 2

resultado = doble_con(10)
print(f"Resultado con return: {resultado} tipo: {type(resultado)}")


