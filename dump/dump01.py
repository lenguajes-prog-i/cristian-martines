import pickle

data = {"mensaje" : "hola"}

serializacion = pickle.dumps(data)

#print(serializacion)

mesaje = pickle.loads(serializacion)

print(mesaje)