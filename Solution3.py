"""Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: multiplicación de 4 números (o x números)
para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos."""

import time

def medirTiempo(func):
    def funcA(*args, **kwargs):
        tiempoInicio = time.time()
        resultado = func(*args, **kwargs)
        tiempoFinal = time.time()
        print(f"Timepo de ejecucion:  {func.__name__}: {tiempoFinal - tiempoInicio:.6f} segundos")
        return resultado
    return funcA

@medirTiempo
def multiplicar(a, b, c, d):
    return a * b * c * d

if __name__ == "__main__":
    multiplicar(2, 3, 4, 5)

    numeros = {
        "a": 10,
        "b": 20,
        "c": 30,
        "d": 40
    }
    multiplicar(**numeros)

    numeros = [1, 2, 3, 4]
    multiplicar(*numeros)