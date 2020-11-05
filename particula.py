from algoritmos import distancetwopoints


class Particula:
    def __init__(self, Id = 0, origen_X = 0, origen_Y = 0, destino_X = 0, destino_Y = 0, velocidad = 0, red = 0, green = 0, blue = 0, distancia = 0):
        self.__Id = Id
        self.__origen_X = origen_X
        self.__origen_Y = origen_Y
        self.__destino_X = destino_X
        self.__destino_Y = destino_Y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancetwopoints(origen_X, origen_Y, destino_X, destino_Y)

    def __str__(self):
        return(
            'ID: ' + str(self.__Id) + '\n' +
            'Origen en X: ' + str(self.__origen_X) + '\n' +
            'Origen en Y: ' + str(self.__origen_Y) + '\n' +
            'Destino en X: ' + str(self.__destino_X) + '\n' +
            'Destino en Y: ' + str(self.__destino_Y) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n' 
        )

    @property
    def Id(self):
        return self.__Id

    @property
    def origen_X(self):
        return self.__origen_X

    @property
    def origen_Y(self):
        return self.__origen_Y

    @property
    def destino_X(self):
        return self.__destino_X

    @property
    def destino_Y(self):
        return self.__destino_Y

    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def red(self):
        return self.__red
    
    @property
    def green(self):
        return self.__green
    
    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia


    def to_json(self):
        return {
            "Id": self.__Id,
            "origen_X": self.__origen_X,
            "origen_Y": self.__origen_Y,
            "destino_X": self.__destino_X,
            "destino_Y": self.__destino_Y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue,
        }
