from models import Cliente
from utils import limpiarPantalla

ruta_archivo = "./archivos/clientes.txt"


def crearCliente():

    dni = input("DNI: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("E-mail: ")

    cliente = Cliente(dni, nombres_apellidos, direccion, telefono, email)

    archivoCliente = open(ruta_archivo, "a")
    archivoCliente.write(str(cliente))
    archivoCliente.close


def gestionClientes():
    while True:
        print("Sub Menu: GESTION DE CLIENTES")
        print("1. Ingresar cliente")
        print("2. Mostrar clientes")
        print("3. regresar al menu principal")
        op = input("Ingrese una opcion: ")

        match (op):
            case "1":
                limpiarPantalla()
                crearCliente()
            case "2":
                print("aqui se mostraran los clientes")
            case "3":
                break
            case _:
                print("opcion no disponible")
