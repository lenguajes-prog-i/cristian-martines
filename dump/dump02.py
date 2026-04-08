import pickle

datos = {
    "nombre" : "cristian martinez",
    "materia" : "lenguaje de programacion",
    "notas" : [4.5, 3.0, 5.0],
}

with open("data.txt", "wb") as file:
    pickle.dump(datos,file)

with open("data.txt", "rb") as file2:
    datos_estudiante = pickle.load(file2)

print(datos_estudiante)
