from models import Usuario
from utils import limpiarPantalla

ruta_archivo = "./archivos/usuarios.txt"

def editarusuario():
    Editar = open('usuarios.txt', 'r')
    dni = input('ingrese dni: ')
    for linea in Editar.readline():
        fila = linea
        if dni == linea:
            linea = ('71945296; Luis Quilla; Jr.Lima; 983404586; alberto.quilla@upeu.edu.pe')
            Editar.readline(linea)
            Editar.close()

def crearUsuario():

    dni = input("DNI: ")
    password = input("Password: ")
    tipo = input("Tipo: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("E-mail: ")

    usuario = Usuario(
        dni, password, tipo, nombres_apellidos, direccion, telefono, email
    )

    archivoUsuario = open(ruta_archivo, "a")
    archivoUsuario.write(str(usuario))
    archivoUsuario.close


def buscarUsuario(dni):
    vector = []
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        fila = linea.split(";")
        # print(atributo)
        if fila[0] == dni:
            return True
    return False


def buscarPassword(dni,password):
    pass
    

def gestionUsuarios():
    while True:
        print("Sub Menu: GESTION DE USUARIOS")
        print("1. Ingresar usuario")
        print("2. editar usuario")
        print("3. Buscar usuario por DNI")
        print("4. regresar al menu principal")
        op = input("Ingrese una opcion: ")

        match (op):
            case "1":
                limpiarPantalla()
                crearUsuario()
            case "2":
                limpiarPantalla()
                editarusuario()
            case "3":
                limpiarPantalla()
                print("buscar por DNI")
                dni = input("Ingrese DNI: ")
                if buscarUsuario(dni):
                    print("Existe")
                else:
                    print("No existe")

            case "4":
                break
            case _:
                print("opcion no disponible")
