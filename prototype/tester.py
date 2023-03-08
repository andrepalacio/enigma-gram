from machine import Enigma

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáéíóúñ ,.0123456789!¡¿?'+-*=/%$#|()<>_\\\"")
#msg = "aislamiento de estructuras para funciones específicas, sin interferencia externa, membrana plasmática, citoplasmática"
msg = "El día de hoy hay permiso académico. Por tanto no se pueden realizar actividades de evaluación ni adelantar temas. Por esto les propongo que trabaje en sus tareas y nos vemos el próximo viernes. Por esta razón hoy no estaré presente en el salón de clases. Sin embargo estaré disponible via correo electrónico para resolver cualquier duda que tengan."

enigma = Enigma(chars)
enigma.createMachine(3)

print(chars, '\n')
enigma.getData()

print("Mensaje original:",msg)
cmsg = enigma.code(msg)
print("\nMensaje encriptado:",cmsg)
enigma.setPositions([1,1,1])
cmsg2 = enigma.decode(cmsg)
print("\nMensaje desencriptado:",cmsg2)

'''
#Leemos el archivo
filename = 'odisea.txt'
with open(filename, 'r',errors='ignore') as f:
    Mensaje = f.read()

#Definimos los caracteres con los que se va a cifrar

#Se puede utilizar los caracteres del libro
CaracteresUnicos = set(Mensaje)
Caracteres = sorted(list(CaracteresUnicos))
#O se definen los caracteres
#Caracteres = ['\n', ' ', '!', '"', '#', '$', '%', "'", '(', ')', '*', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '=', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '\xa0', '¡', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '\xad', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'Â', 'Ã', 'Å', 'Î', 'Ï', 'á', 'â', 'ï', 'Œ', 'œ', 'Š', 'š', 'Ÿ', 'Ž', 'ƒ', 'ˆ', '˜', '–', '‘', '’', '‚', '“', '”', '„', '†', '‡', '•', '…', '‰', '›', '€', '™']

#Creamos la maquina con N rotores
NumRotores=3
maquina=Enigma(Caracteres)
maquina.CrearMaquina(NumRotores)

#Ciframos y desiframos el archivo
MensajeCifrado=maquina.Cifrar(Mensaje)
MensajeDecifrado=maquina.Cifrar(MensajeCifrado)

archivo = open("LibroCifrado.txt","w")
archivo.write(MensajeCifrado)
archivo.close

archivo = open("LibroDecifrado.txt","w")
archivo.write(MensajeDecifrado)
archivo.close

print("Libro completamente Cifrado y Decifrado")
'''
