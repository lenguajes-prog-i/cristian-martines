import threading
import time

def tarea(letra):
    print(f'Hilo trabajando con: {letra * 5}')

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
hilos = []

inicio = time.perf_counter() 

for i in letras:
    hilo = threading.Thread(target=tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

fin = time.perf_counter()

print(f"Tiempo total de ejecución: {fin - inicio:} segundos")