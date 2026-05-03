from excepciones import ClienteInvalido
from base import Entidad

class Cliente(Entidad):
    def __init__(self, nombre, identificacion):

        if not nombre:
            raise ClienteInvalido("Nombre inválido")

        if len(identificacion) < 3:
            raise ClienteInvalido("ID inválido")

        self.__nombre = nombre
        self.__identificacion = identificacion

    def get_nombre(self):
        return self.__nombre

    def mostrar(self):
        return f"Cliente: {self.__nombre}"