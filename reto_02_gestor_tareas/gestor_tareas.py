import os
import msvcrt

# Variables
continuar = True
lista = []

# Funciones
def crear_archivo(datos):
    with open('tareas.txt', 'w') as tareas:
        tareas.write(f'{datos}\n')

def agregar_tarea(datos):
    with open('tareas.txt', 'a') as tareas:
        tareas.write(f'{datos}\n')

def leer_archivo():
    contenido = []
    with open("tareas.txt", "r") as tareas:
        for linea in tareas:
            contenido.append(linea.strip())
    for i, linea in enumerate(contenido, start=1):
        print(f"{i}. {linea}")

def llenar_lista():
    temporal = []
    with open("tareas.txt", "r") as f:
        temporal = f.readlines()
    return temporal

def completar_tarea():
    leer_archivo()
    lista = llenar_lista()
    try:
        ntarea = int(input('Ingresa el numero de tarea a completar: ')) - 1
        lista[ntarea] = "[X] " + lista[ntarea][4:]
        print("Tarea completada con exito!")
    except IndexError:
        print("Regresando al menu principal para evitar errores")
        return
    with open('tareas.txt', 'w') as tareas:
        tareas.writelines(lista)

# Main
while continuar:
    os.system('cls')
    opt = input("=== GESTOR DE TAREAS ===\n   1. Agregar tarea\n   2. Ver tareas\n   3. Marcar tarea como completada\n   4. Salir\n   Opción:")
    match opt:
        case '1':
            tarea = input("\nDescripcion de la tarea: ")
            tarea = (f"[ ] {tarea}")
            if os.path.exists('tareas.txt'):
                agregar_tarea(tarea)
                print("\n!Tarea agregada!")
            else:
                crear_archivo(tarea)
                print("\n!Tarea agregada!")
            print("Presiona cualquier tecla para continuar...")
            msvcrt.getch()
        case '2':
            os.system('cls')
            if os.path.exists('tareas.txt') and os.path.getsize('tareas.txt') > 0:
                leer_archivo()
            else:
                print("\nEl gestor de tareas no ha sido creado aun, favor de usar opcion (1)")
            print("\nPresiona cualquier tecla para continuar...")
            msvcrt.getch()
        case '3':
            os.system('cls')
            if os.path.exists('tareas.txt') and os.path.getsize('tareas.txt') > 0:
                completar_tarea()
            else:
                print("\nEl gestor de tareas no ha sido creado aun, favor de usar opcion (1)")
            print("Presiona cualquier tecla para continuar...")
            msvcrt.getch()
        case '4':
            continuar = False
        case _:
            os.system('cls')
            print("\nERROR: Lo ingresado no es una opcion valida!")
            print("Presiona cualquier tecla para continuar...")
            msvcrt.getch()