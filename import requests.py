import json

import requests

headers = {
    'Content-Type': 'text/plain',
}

response = requests.get('http://finis.malba.cl/GetMsg', headers=headers)

def decifrarROT7(texto):
    mensaje = texto
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    aux = ""
    for letra in mensaje:
        aux = aux + diccionario[(diccionario.find(letra) - 7) % 26]
    return aux

def decifrado_vigenere(texto, clave):
    mensaje = texto
    clave_original = clave
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    key = ''
    decifrado = ''

    if len(mensaje) > len(clave_original):
        for i in range(int(len(mensaje) / len(clave_original))):
            key += clave_original
        key += clave_original[:len(mensaje) % len(clave_original)]

    elif len(mensaje) < len(clave_original):
        key += clave_original[:len(mensaje)]

    elif len(mensaje) == len(clave_original):
        key += clave_original

    for i in range(len(mensaje)):
        x = diccionario.find(mensaje[i])
        y = diccionario.find(key[i])
        resta = x - y
        modulo = resta % len(diccionario)
        decifrado += diccionario[modulo]

    return decifrado

def decifrarROT15(texto):
    mensaje = texto
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    aux = ""
    for letra in mensaje:
        aux = aux + diccionario[(diccionario.find(letra) - 15) % 26]
    return aux

msg_import = json.loads(response.text)

mensaje_cifrado = msg_import['msg']

clave_vigenere = 'aobkqolrzsrigpknkufezioer'


decifrar_rot7 = decifrarROT7(mensaje_cifrado)
decifrar_vigenere = decifrado_vigenere(decifrar_rot7, clave_vigenere)
decifrar_rot15 = decifrarROT15(decifrar_vigenere)

print("Mensaje decifrado ROT7:", decifrar_rot7)
print("Mensaje decifrado Vigenère:", decifrar_vigenere)
print("Mensaje decifrado ROT15:", decifrar_rot15)

