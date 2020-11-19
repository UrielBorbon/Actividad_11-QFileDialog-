from particula import Particula
import json

class ListaPar:
    def __init__(self):
        self.particles = [] #antes era un arreglo privado pero lo tuve que cambiar a metodo publico para que pudiera acceder a la lista de mis particulas

    def agregar_final(self, particula:Particula):
        self.particles.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.particles.insert(0, particula)

    def mostrar(self):
        for particula in self.particles:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.particles
        ) 

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo: #se va a crear en modo escritura "write"
                listaparti = [particula.to_json() for particula in self.particles]
                print (listaparti)
                json.dump(listaparti, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                listaparti = json.load(archivo)
                self.particles = [Particula(**particula) for particula in listaparti]     
            return 1
        except:
            return 0    

    def __len__(self):
        return len(self.particles)

    
    def __iter__(self):
        self.cont = 0

        return self
    
    def __next__(self):
        if self.cont < len(self.particles):
            particula = self.particles[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration


#part = Particle()
#pa1 = Particula(1,1,1,1,1,1,1,1,1,0)
#pa2 = Particula(1,100,200,200,1,4,2,2,2,0)
#part.agregar_inicio(pa2)
#part.agregar_final(pa1)
#part.mostrar()
