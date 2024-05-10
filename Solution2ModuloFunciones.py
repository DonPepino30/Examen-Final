import math
import random

def crearListaArchivo(nombre, T):
    lista1 = [random.randint(1, 100) for _ in range(T)]
    with open(nombre, "w") as file:
        for num in lista1:
            file.write(str(num) + "\n")

def numerosRaizCuadradaArchivo(nombre):
    with open(nombre, "r") as file:
        numeros = [float(line.strip()) for line in file.readlines()]
    with open("temp.txt", "w") as aux_file:
        for num in numeros:
            raizCuadrada = math.sqrt(num)
            aux_file.write(str(raizCuadrada) + "\n")
    with open(nombre, "w") as file:
        for num in numeros:
            file.write(str(num) + "\n")
    with open("temp.txt", "r") as aux_file:
        for linea in aux_file:
            file.write(linea)
    aux_file.close()
    file.close()
    with open("aux.txt", "w") as aux_file:
        pass
    with open(nombre, "w") as file:
        pass
    file.close()