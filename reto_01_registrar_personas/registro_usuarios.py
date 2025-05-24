import os

# Variables
continuar = True

# Funciones
def crear_archivo(name, age):
    with open('usuarios.txt', 'w') as usuarios:
        usuarios.write(f'{name}\n{age}\n')

def actualizar_archivo(name, age):
    with open('usuarios.txt', 'a') as usuarios:
        usuarios.write(f'{name}\n{age}\n')

def leer_archivo():
    contenido = []
    with open("usuarios.txt", "r") as f:
        for linea in f:
            contenido.append(linea.strip())
    return contenido

try:
    nombre = input('Cual es tu nombre:')
    edad = int(input('Ingresa tu edad:'))
    if edad <= 0:
        raise Exception
except ValueError:
    print('Error en el valor ingresado')
except Exception:
    print(f'Edad no puede ser menor o igual a 0')
else:
    if os.path.exists('usuarios.txt'):
        actualizar_archivo(nombre, edad)
    else:
        crear_archivo(nombre, edad)
    datos = leer_archivo()
    for i in range(0, len(datos), 2):
        try:
            nombre = datos[i]
            edad = int(datos[i + 1])
            if edad >= 18:
                print(f'{nombre} ({edad}) es mayor de edad')
            else:
                print(f'{nombre} ({edad}) es menor de edad')
        except ValueError:
            print("Error al procesar datos del archivo")
