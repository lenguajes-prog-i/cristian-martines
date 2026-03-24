import threading 
import time

print(threading.active_count)
print(threading.enumerate)


def programar ():
    print("inicio 1")
    time.sleep(4)
    print("finaliza 1")

def beber_agua():
    print("inicio 2")
    time.sleep(6)
    print("finalizo 2")

def estudiar ():
    print("inicio 3")
    time.sleep(8)
    print("finalizo 3")

inicio = time.perf_counter()

programar()
beber_agua()
estudiar()
hilo_programar = threading.thread (terger=programar, args =())
hilo_programar.start()
hilo_beber_agua = threading.thread(terger=beber_agua, args =())
hilo_beber_agua.start()
hilo_estudiar = threading.thread(terger=estudiar, args =())
hilo_estudiar.start()


hilo_programar.join()
hilo_beber_agua.join()
hilo_estudiar.join()


fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)