def log(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(mensaje + "\n")