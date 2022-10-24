#2. Crie de forma recursiva uma função que printe do número recebido até o zero.#

def contador (numero):
    while numero > 0:
        numero -= 1
        print(numero)

contador(10)