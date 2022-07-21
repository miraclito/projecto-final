from platform import architecture
from models import Usuario

ruta_archivo = './usuarios.txt'

def ingresarusuario():
    dni = input('DNI: ')
    nombres_apellidos = input('Nombres y Apellidos: ')
    direccion = input('Dirección: ')
    telefono = input('Telefono: ')
    email = input('E-mail: ')

    usuario = Usuario(dni, nombres_apellidos, direccion, telefono, email)

    archivoUsuario = open(ruta_archivo, 'a')
    archivoUsuario.write(str(usuario))
    archivoUsuario.close
    
    
def editarusuario():
    Editar = open('./archivos/usuarios.txt', 'r')
    dni = input('ingrese dni: ')
    for linea in Editar.readline():
        fila = linea
        if dni == linea:
            linea = ('71945296; Luis Quilla; Jr.Lima; 983404586; alberto.quilla@upeu.edu.pe')
            Editar.readline(linea)
            Editar.close()



    '''
    [] = input('ingrese dni')
    ruta_archivo = []
    with open('./usuarios.txt', 'w') as n:
        for dni in n:
            n.chage(dni)
    '''

            
  
    
    
def buscarUsuario(dni):
    vector = []
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        fila = linea.split(";")
        if fila[0] == dni:
            return True
    return False
    
    
def gestionusuario():
    while True:
        print('Gestion de Usuarios')
        print('1. Ingrese usuario')
        print('2. Editar usuario')
        print('3. Buscar usuario')
        print('4. regresar')
        op = input('ingrese una opcion: ')
        
        match(op):
            case '1':
                ingresarusuario()
            case '2':
                editarusuario()
            case '3':
                print('buscar por dni')
                dni = input('Ingrese dni: ')
                if buscarUsuario(dni):
                    print('existe')
                else:
                    print('no existe')
            case '4':
                break
            case _:
                print('esa opcion es incorrecta')
                
