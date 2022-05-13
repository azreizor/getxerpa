# Enunciado:
# Para este ejercicio es necesario construir un conjunto de funciones que ejecuten operaciones aritméticas básicas.
# Por ejemplo:

# four(times(five())) # regresa 20
# one(plus(one())) # regresa 2
# seven(minus(three())) # regresa 4
# nine(divided_by(three())) # regresa 3

# Requisitos:
# Deben existir funciones para cada número de cero (0) a nueve (9).
# Debe existir una función para cada operación aritmética: sumar, restar, multiplicar y dividir.- Cada cálculo se
# compone exactamente de una operación y dos números.
# La función más externa representa el número de la izquierda y la función más interna al número de  la derecha.
# La división deberá entregar un número entero

# Entrega:
# El código será un archivo python público en github o cualquiera otra plataforma con acceso público y que mantenga
# la siguiente estructura:

def zero(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(0)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 0

def one(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(1)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 1

def two(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(2)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 2

def three(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(3)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 3

def four(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(4)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 4


def five(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(5)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 5


def six(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(6)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 6


def seven(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(7)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 7


def eight(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(8)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 8


def nine(*opcionales):
    aux = []
    if len(opcionales)>0:
        aux.append(9)
        for opcion in opcionales:
            aux.append(opcion[0])
            aux.append(opcion[1])
        print(int(eval(f"{aux[0]}{aux[1]}{aux[2]}")))
    else:
        return 9

def plus(numero):
    return "+",numero
def minus(numero):
    return "-",numero
def times(numero):
    return "*",numero
def divided_by(numero):
    return "/",numero


four(times(five())) # imprime 20
one(plus(eight())) # imprime 9
seven(minus(three())) # imprime 4
nine(divided_by(three())) # imprime 3
