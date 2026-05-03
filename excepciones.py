class ErrorSistema(Exception):
    pass

class ClienteInvalido(ErrorSistema):
    pass

class ServicioNoDisponible(ErrorSistema):
    pass

class ReservaError(ErrorSistema):
    pass