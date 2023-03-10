from machine import Enigma

#Leemos el archivo
filename = 'Odisea.txt'
with open(filename, 'r',errors='ignore') as f:
    msg = f.read()

#Definimos los caracteres con los que se va a cifrar

#Se puede utilizar los caracteres del libro
CaracteresUnicos = set(msg)
chars = sorted(list(CaracteresUnicos))

#O se definen los caracteres
#chars = ['\n',' ', '!', '"', '#', '$', '%', "'", '(', ')', '*', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '=', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '\xa0', '¡', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '\xad', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'Â', 'Ã', 'Å', 'Î', 'Ï', 'á', 'â', 'ï', 'Œ', 'œ', 'Š', 'š', 'Ÿ', 'Ž', 'ƒ', 'ˆ', '˜', '–', '‘', '’', '‚', '“', '”', '„', '†', '‡', '•', '…', '‰', '›', '€', '™']
print(len(chars))
#Creamos la maquina con 5 rotores
enigma = Enigma(chars)
enigma.createMachine(5)

print(chars, '\n')
enigma.getData()

#print("Mensaje original:",msg)
cmsg = enigma.code(msg)
#print("\nMensaje encriptado:",cmsg)
enigma.setPositions([0,0,0,0,0])
cmsg2 = enigma.code(cmsg)
#print("\nMensaje desencriptado:",cmsg2)

#Ciframos y desiframos el archivo
archivo = open("LibroCifrado.txt","w")
archivo.write(cmsg)
archivo.close

archivo = open("LibroDecifrado.txt","w")
archivo.write(cmsg2)
archivo.close

print("Libro completamente Cifrado y Decifrado")