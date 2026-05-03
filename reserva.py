from excepciones import ReservaError

class Reserva:
    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def calcular_total(self):
        return self.servicio.calcular_precio() * self.duracion

    def mostrar(self):
        return f"""
Cliente: {self.cliente.get_nombre()}
Servicio: {self.servicio.nombre}
Duración: {self.duracion}
Estado: {self.estado}
Total: {self.calcular_total()}
"""