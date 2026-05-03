from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import log

clientes = []
servicios = []
reservas = []


def mostrar_clientes():
    for i, c in enumerate(clientes):
        print(f"{i} - {c.get_nombre()}")


def mostrar_servicios():
    for i, s in enumerate(servicios):
        print(f"{i} - {s.nombre} - ${s.calcular_precio()}")


def menu():
    while True:
        print("\n=== SISTEMA SOFTWARE FJ ===")
        print("1. Crear cliente")
        print("2. Crear servicio")
        print("3. Crear reserva")
        print("4. Ver reservas")
        print("5. Cancelar reserva")
        print("6. Salir")

        opcion = input("Seleccione: ")

        try:

            if opcion == "1":
                nombre = input("Nombre: ")
                identificacion = input("ID: ")

                cliente = Cliente(nombre, identificacion)
                clientes.append(cliente)

                print("Cliente creado")
                log("Cliente creado")

            elif opcion == "2":
                print("1. Sala 2. Equipo 3. Asesoria")
                tipo = input("Seleccione: ")

                if tipo == "1":
                    servicio = ReservaSala("Sala")
                elif tipo == "2":
                    servicio = AlquilerEquipo("Equipo")
                elif tipo == "3":
                    servicio = Asesoria("Asesoria")
                else:
                    print("Opción inválida")
                    continue

                servicios.append(servicio)
                print("Servicio creado")
                log("Servicio creado")

            elif opcion == "3":

                if not clientes or not servicios:
                    print("Debe crear clientes y servicios primero")
                    continue

                print("\nClientes:")
                mostrar_clientes()
                idx_cliente = int(input("Seleccione cliente: "))

                print("\nServicios:")
                mostrar_servicios()
                idx_servicio = int(input("Seleccione servicio: "))

                try:
                    duracion = int(input("Duración: "))
                except ValueError:
                    print("Debe ser número")
                    log("Error tipo dato duración")
                else:
                    print("Dato correcto")
                finally:
                    print("Validación completada")

                cliente = clientes[idx_cliente]
                servicio = servicios[idx_servicio]

                reserva = Reserva(cliente, servicio, duracion)
                reserva.confirmar()

                reservas.append(reserva)

                print("Reserva creada")
                log("Reserva creada")

            elif opcion == "4":
                for i, r in enumerate(reservas):
                    print(f"\nReserva {i}")
                    print(r.mostrar())

            elif opcion == "5":
                for i, r in enumerate(reservas):
                    print(f"{i} - {r.cliente.get_nombre()}")

                idx = int(input("Seleccione reserva: "))
                reservas[idx].cancelar()

                print("Reserva cancelada")
                log("Reserva cancelada")

            elif opcion == "6":
                print("Saliendo...")
                break

            else:
                print("Opción inválida")

        except Exception as e:
            print("Error:", e)
            log("Error: " + str(e))


menu()