import random

class Bombo:
    def __init__(self):
        self.numeros = list(range(1, 76))
        random.shuffle(self.numeros)

    def sortear_numero(self):
        if self.numeros:
            return self.numeros.pop()
        else:
            return None