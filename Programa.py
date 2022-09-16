import random


class Cuestionador:

    def __init__(self):        
        self.questions=[
            "¿Qué es el ALMICANTARAT?",
            "¿Dónde se encuentra el Zenit?",
            "¿Cuántos órdenes existen en la taxonomía de suelos?"
        ]
        self.answers=[
            "Círculo imaginario en esfera celeste",
            "90 grados respecto al horizonte",
            12
        ]

    def jugar(self):
        # Generar un número aleatorio entre 0 y n-1 siendo n el 
        # tamaño de la lista de preguntas
        n=len(self.questions)
        number= random.randint(0, n-1)
        print(self.questions[number])

        #Solicitar la respuesta al usuario
        respuesta=input("¿Cuál es tu respuesta, mi perrito?")

        #Verificar si la respuesta es correcta

        if respuesta== self.answers[number]:
            print("Eres genial, mi perrito!!!")
        else:
            print("Deje de pensar que sus pap{as siempre lo van a mantener!!!")

















