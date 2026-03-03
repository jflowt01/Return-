# Saludo con y sin return

def saludar_sin(nombre: str):
    print(f"Hola, {nombre}")

saludar_sin("Ana")

def saludar_con(nombre: str):
    return f"Hola, {nombre}"

mensaje = saludar_con("Ana")
print(mensaje)


#Suma de dos numeros con y sin return

def sumar_sin(a: int, b: int):
    print(f"Resultado: {a + b}")

sumar_sin(5, 3)

def sumar_con(a: int, b: int):
    return a + b

resultado = sumar_con(5, 3)
print(resultado * 2) 



# Calcular doble de un numero con y sin return

def doble_sin(numero: int):
    print(numero * 2)

doble_sin(10)

def doble_con(numero: int):
    return numero * 2

resultado = doble_con(10)
print(resultado)


