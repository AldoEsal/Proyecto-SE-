import json

def buscar_progresiones(acordes_ingresados, base_de_datos):
    progresiones_encontradas = []

    for progresion in base_de_datos["progresiones"]:
        acordes_progresion = progresion["acordes"]
        
        if all(acorde in acordes_progresion for acorde in acordes_ingresados):
            progresion_encontrada = {
                "progresion": progresion["progresion"],
                "acordes_completos": acordes_progresion
            }
            progresiones_encontradas.append(progresion_encontrada)

    return progresiones_encontradas

def mostrar_progresiones(resultado):
    if resultado:
        for progresion in resultado:
            print(f'Progresión: {progresion["progresion"]}')
            print(f'Acordes completos: {", ".join(progresion["acordes_completos"])}')
            print('-' * 30)
    else:
        print('No se encontraron progresiones para los acordes ingresados.')

def main():
    with open('bd.json', 'r') as file:
        base_de_datos = json.load(file)

    while True:
        acordes_usuario = input('Ingresa los acordes separados por coma (o "salir" para salir): ')

        if acordes_usuario.lower() == 'salir':
            break

        resultado = buscar_progresiones(acordes_usuario.split(','), base_de_datos)

        mostrar_progresiones(resultado)

if __name__ == "__main__":
    main()
