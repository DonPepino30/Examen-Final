import random

def crearLista():
    Lista1 = [random.randint(1, 100) for _ in range(10)]
    print("Lista:", Lista1)
    return Lista1

def almacenarNoRepetidos(Lista1):
    Lista2 = list(set(Lista1))
    print("Numeros unicos de Lista 1:", Lista2)
    return Lista2

def ordenarListaUnica(Lista2):
    ListasOrdenadas = {"Ascendente": sorted(Lista2), "Descendente": sorted(Lista2, reverse=True)}
    print("Ascendente:", ListasOrdenadas["Ascendente"])
    print("Descendente:", ListasOrdenadas["Descendente"])

def numeroMayor(Lista2):
    numerosPares = [num for num in Lista2 if num % 2 == 0]
    if numerosPares:
        maximoPar = max(numerosPares)
        print("El maximo numero par es:", maximoPar)
    else:
        print("No hay pares (lo cual es muy raro)")