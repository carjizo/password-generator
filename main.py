import random
import json


def generar_id():
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    id = []

    for i in range(5):
        caracter_random_id = random.choice(NUMS)
        id.append(caracter_random_id)
    id = ''.join(id)
    return id


def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres =  MAYUS + MINUS + NUMS +CHARS

    contrasena = []
    
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena)
    return contrasena


def crear_data(id, contrasena):
    my_data = {}
    my_data['clientes'] = []

    my_data['clientes'].append({
        id : contrasena
    })

    with open("./archivos/data.json", "w", encoding="utf-8") as f:
        json.dump(my_data, f, indent=4)
    return my_data



def run():
    usuario = input('Escribe tu nombre: ')
    contrasena = generar_contrasena()
    id = generar_id()
    dat = crear_data(id, contrasena)
    # dat_actualizada = alctualizar_data(id, contrasena)
    
    
    print(f'Hola {usuario.upper()} tu id es: {id} y tu contraseña es: {contrasena}')
    print(dat)
    # print(dat_actualizada)
    


if __name__ == '__main__':
    # while True:
    run()