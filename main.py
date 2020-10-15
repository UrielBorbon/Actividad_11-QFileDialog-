from particula import Particula

class Particle:
    def __init__(self):
        self.__particles = []

    def agregar_final(self, particula:Particula):
        self.__particles.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particles.insert(0, particula)

    def mostrar(self):
        for particula in self.__particles:
            print(particula)

#part = Particle()
#pa1 = Particula(1,1,1,1,1,1,1,1,1,0)
#pa2 = Particula(1,100,200,200,1,4,2,2,2,0)
#part.agregar_inicio(pa2)
#part.agregar_final(pa1)
#part.mostrar()
