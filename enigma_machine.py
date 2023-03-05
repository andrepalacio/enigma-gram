from random import sample

# definimos los caracteres a utilizar
#caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzñáéíóú,.;:-¿?!¡"

# creamos 5 listas vacías
#listas_random = [[] for i in range(5)]

# generamos listas aleatorias sin repetir caracteres
#for lista in listas_random:
#    lista.extend(sample(caracteres, len(caracteres)))

class Reflector:
    def __init__(self, caracteres):
        self.caracteres = caracteres
        
    def reflect(self, n):
        caracter=self.caracteres[n]
        return caracteres.index(caracter)

# creamos una instancia del reflector


class Rotor:
    def __init__(self, wiring):
        self.wiring = wiring
        self.posicion_inicio = 0

    def setPosicion_inicio(self,posicion):
        self.posicion_inicio = posicion

    def avanzar(self):
        self.posicion_inicio = (self.posicion_inicio + 1) % len(caracteres)
        
    def cifrar(self, indice):
        indice_desplazado = (indice + self.posicion_inicio) % len(caracteres)
        wiring = self.wiring
        letra_cifrada = wiring[indice_desplazado]
        indice_cifrado = (caracteres.index(letra_cifrada) - self.posicion_inicio) % len(caracteres)
        return indice_cifrado
    
    def cifrar_inverso(self, indice):
        letra_cifrada = caracteres[(indice + self.posicion_inicio) % len(caracteres)]
        indice_cifrado = self.wiring.index(letra_cifrada) - self.posicion_inicio
        if indice_cifrado < 0:
            indice_cifrado += len(caracteres)
        return indice_cifrado

class Enigma:
    def __init__(self, listas_random, lista_reflector):
        self.rotor1 = Rotor(listas_random[0])
        self.rotor2 = Rotor(listas_random[1])
        self.rotor3 = Rotor(listas_random[2])
        self.reflector = Reflector(lista_reflector)
        
    def cifrar(self, mensaje):
        mensaje_cifrado = ""
        for letra in mensaje:
            indice = caracteres.index(letra)
            indice_cifrado = self.rotor1.cifrar(indice)
            indice_cifrado = self.rotor2.cifrar(indice_cifrado)
            indice_cifrado = self.rotor3.cifrar(indice_cifrado)
            #indice_cifrado = self.reflector.reflect(indice_cifrado)
            #indice_cifrado = self.rotor3.cifrar_inverso(indice_cifrado)
            #indice_cifrado = self.rotor2.cifrar_inverso(indice_cifrado)
            #indice_cifrado = self.rotor1.cifrar_inverso(indice_cifrado)
            mensaje_cifrado += caracteres[indice_cifrado]
            self.rotor1.avanzar()
            if self.rotor1.posicion_inicio == 0:
                self.rotor2.avanzar()
                if self.rotor2.posicion_inicio == 0:
                    self.rotor3.avanzar()
                    
        return mensaje_cifrado

    def descifrar(self,mensaje):
        mensaje_cifrado = ""
        for letra in mensaje:
            indice = caracteres.index(letra)
            indice_cifrado = self.rotor3.cifrar_inverso(indice)
            indice_cifrado = self.rotor2.cifrar_inverso(indice_cifrado)
            indice_cifrado = self.rotor1.cifrar_inverso(indice_cifrado)
            mensaje_cifrado += caracteres[indice_cifrado]
            self.rotor1.avanzar()
            if self.rotor1.posicion_inicio == 0:
                self.rotor2.avanzar()
                if self.rotor2.posicion_inicio == 0:
                    self.rotor3.avanzar()
                    
        return mensaje_cifrado

# Importamos las clases que necesitamos
from string import ascii_letters, digits, punctuation

# Creamos las listas aleatorias para los rotores
caracteres = list(ascii_letters + digits + punctuation + "ñáéíóú")
listas_random = [[] for i in range(5)]
for lista in listas_random:
    lista.extend(sample(caracteres, len(caracteres)))
rotor1_wiring = listas_random[0]
rotor2_wiring = listas_random[1]
rotor3_wiring = listas_random[2]
reflector_wiring = sample(caracteres, len(caracteres))

'''
-------------ERROR PRINCIPAL-----------------
Se estaban creando instancias de las clases 
rotores y reflector pero esto ya lo hacia la clase
maquina, entonces se estaban creando dos veces las 
instanciasentonces para que funcionara solo tocaba 
enviarlela lista de caracteres
'''
# Creamos el reflector y los rotores
#reflector = Reflector(reflector_wiring)
#rotor1 = Rotor(rotor1_wiring)
#rotor2 = Rotor(rotor2_wiring)
#rotor3 = Rotor(rotor3_wiring)
#print(rotor1.wiring,'\n',len(rotor1_wiring), rotor1.wiring[0])

# Creamos una instancia de la máquina Enigma con los rotores y el reflector
maquina = Enigma([rotor1_wiring, rotor2_wiring, rotor3_wiring], reflector_wiring)

maquina.rotor1.setPosicion_inicio(0)
maquina.rotor2.setPosicion_inicio(0)
maquina.rotor3.setPosicion_inicio(0)
# Ciframos un mensaje de prueba
mensaje = "HOLA"
mensaje_cifrado = maquina.cifrar(mensaje)
print("Mensaje cifrado:", mensaje_cifrado)

maquina.rotor1.setPosicion_inicio(0)
maquina.rotor2.setPosicion_inicio(0)
maquina.rotor3.setPosicion_inicio(0)

# Desciframos el mensaje cifrado
mensaje_descifrado = maquina.descifrar(mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)
