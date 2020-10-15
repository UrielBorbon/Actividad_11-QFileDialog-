import math

def distancetwopoints(origen_X, origen_Y, destino_X, destino_Y):
    x_1 = origen_X
    y_1 = origen_Y
    x_2 = destino_X
    y_2 = destino_Y

    d = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

    return d