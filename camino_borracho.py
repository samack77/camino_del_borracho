from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo_caminata, borracho, pasos):
    inicio = campo_caminata.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo_caminata.mover_borracho(borracho)
    
    return inicio.distancia(campo_caminata.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo_caminata = Campo()
        campo_caminata.agregar_borracho(borracho, origen)
        simulacion_caminata = caminata(campo_caminata, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    return distancias

def graficar_linea(x, y):
    grafica = figure(title='Camino borracho', x_axis_label="Pasos", y_axis_label="Distancia")
    grafica.line(x, y, legend_label="Distancia Media")
    show(grafica)

def main(distancias_caminata, numero_intentos, tipo_borracho):
    
    distancias_media_caminata = []
    for pasos in distancias_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)
        distancias_media_caminata.append(distancia_media)
        print(f'{tipo_borracho.__name__} camino {pasos}')
        print(f'Media= {distancia_media}')
        print(f'Max= {distancia_max}')
        print(f'Min= {distancia_min}')
    graficar_linea(distancias_caminata, distancias_media_caminata)

if __name__ == '__main__':
    distancias_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100

    main(distancias_caminata, numero_intentos, BorrachoTradicional)
