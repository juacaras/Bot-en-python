import random

class CartonBingo:
    def __init__(self):
        self.carton = self.generar_carton()

    def generar_carton(self):
        columnas = {
            'B': random.sample(range(1, 16), 5),
            'I': random.sample(range(16, 31), 5),
            'N': random.sample(range(31, 46), 5),
            'G': random.sample(range(46, 61), 5),
            'O': random.sample(range(61, 76), 5),
        }

        # Generar la matriz por filas
        carton = [[columnas[col][row] for col in 'BINGO'] for row in range(5)]

        # Guardar el valor que estaba en el centro y eliminarlo del conjunto N
        numero_central = carton[2][2]
        columnas['N'].remove(numero_central)

        # Reemplazar con espacio libre
        carton[2][2] = 'X'

        return carton

    def marcar(self, numero, jugador_bingo):
        for fila_idx, fila in enumerate(self.carton):
            for col_idx in range(5):
                if fila[col_idx] == numero:
                    fila[col_idx] = 'X'
                    letra_columna = 'BINGO'[col_idx]


    def esta_lleno(self):
        for fila in self.carton:
            for valor in fila:
                if valor != 'X':
                    return False
        return True

    def mostrar(self):
        print(" B   I   N   G   O")
        for fila in self.carton:
            print("".join(f"{str(x):>3} " for x in fila))
        print()