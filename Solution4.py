"""Usando la siguiente API:
https://jsonplaceholder.typicode.com/users
Agregar los nombres y edades (en el código) para los usuarios que tengan id 6
y 8.
Terminar comparando sus edades e indicar y mostrar en consola quien es el
mayor de los 2 usuarios."""

import datetime
import requests

def obtenerData(IdUsuarios):
    url = "https://jsonplaceholder.typicode.com/users"
    resp = requests.get(url)
    usuarios = resp.json()
    data = {}
    for user in usuarios:
        if str(user["id"]) in IdUsuarios:
            data[user["id"]] = {
                "name": user["name"],
                "age": calcularEdad(user["birthday"])
            }
    return data

def calcularEdad(cumple):
    actual = datetime.date.today()
    edad = actual.year - cumple.year - ((actual.month, actual.day) < (cumple.month, cumple.day))
    return edad

if __name__ == "__main__":
    IdUsuarios = [6, 8]
    data = obtenerData(IdUsuarios)
    usuario6 = data[6]
    usuario8 = data[8]
    if usuario6["age"] > usuario8["age"]:
        print(f"{usuario6['name']} es mas viejo que {usuario8['name']}")
    elif usuario6["age"] < usuario8["age"]:
        print(f"{usuario8['name']} es mas viejo que {usuario6['name']}")
    else:
        print(f"{usuario6['name']} y {usuario8['name']} son de la misma edad")