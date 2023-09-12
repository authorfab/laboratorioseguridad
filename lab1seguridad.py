def cifrarROT15(texto):
    
    mensaje = texto
    
    diccionario = "abcdefghijklmnopqrstuvwxyz"

    aux = ""
    
    for letra in mensaje:

        aux = aux + diccionario[(diccionario.find(letra)+15)% 26]

    return aux


def cifrado_vigenere(texto, clave):
    
    mensaje = texto

    clave_original = clave

    diccionario = "abcdefghyjklmnopqrstuvwxyz"

    key = ''
    cifrado = ''

    if len(mensaje)>len(clave_original):
        for i in range (int(len(mensaje)/len(clave_original))):
            key += clave_original
        key += clave_original [:len(mensaje)%len(clave_original)]

    elif len(mensaje)<len(clave_original):
        key += clave_original [:len(mensaje)]
        
    elif len(mensaje)==len(clave_original):
        key += clave_original

    for i in range (len(mensaje)):
        x = diccionario.find(mensaje[i])
        y = diccionario.find(key[i])
        suma = (x + y)%len(diccionario)
        cifrado += diccionario[suma]
    
    return cifrado

def cifrarROT7(texto):
    
    mensaje = texto
    
    diccionario = "abcdefghyjklmnopqrstuvwxyz"

    aux = ""
    
    for letra in mensaje:

        aux = aux + diccionario[(diccionario.find(letra) + 7 ) % 26]

    return aux


mensaje_original = "correrapido"
clave_vigenere = "cvqnoteshrwnszhhksorbqcoas"

cifrar_rot15 = cifrarROT15(mensaje_original)
cifrar_vigenere = cifrado_vigenere(cifrar_rot15, clave_vigenere)
cifrar_rot7 = cifrarROT7(cifrar_vigenere)

print("Mensaje cifrado ROT15 ", cifrar_rot15)
print("Mensaje cifrado Vigenère:", cifrar_vigenere)
print("Mensaje cifrado ROT7 ", cifrar_rot7)

print("Mensaje cifrado final ", cifrar_rot7)
