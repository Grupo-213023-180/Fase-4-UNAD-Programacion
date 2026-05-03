from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_precio(self):
        pass

    def calcular_precio_con_descuento(self, descuento=0):
        return self.calcular_precio() - descuento


class ReservaSala(Servicio):
    def calcular_precio(self):
        return 50000


class AlquilerEquipo(Servicio):
    def calcular_precio(self):
        return 80000


class Asesoria(Servicio):
    def calcular_precio(self):
        return 100000