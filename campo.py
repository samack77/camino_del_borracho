
class Campo:

    def __init__(self):
        self.coodenadas_de_borrachos = {}

    def agregar_borracho(self, borracho, coordenada):
        self.coodenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.caminar()
        coordenada_actual = self.coodenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coodenadas_de_borrachos[borracho] = nueva_coordenada
    
    def obtener_coordenada(self, borracho):
        return self.coodenadas_de_borrachos[borracho]
