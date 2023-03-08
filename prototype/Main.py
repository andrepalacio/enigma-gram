from MaquinaEnigma import Enigma
from string import ascii_letters, digits, punctuation

# Creamos las listas aleatorias para los rotores
#t_caract = list(ascii_letters + digits + punctuation + "ñáéíóú ")
t_caract = list("abcdefghijklmnopqrstuvwxyzáéíóú ,.")

#testing
encryptor = Enigma(t_caract)
encryptor.CrearMaquina(3)
rotor1, rotor2, rotor3 = encryptor.GetListRotores()
reflector = encryptor.GetReflector()
print(rotor1.GetConexiones(),'\n')
print(rotor2.GetConexiones(), '\n')
print(rotor3.GetConexiones(), '\n')
print(reflector.GetL1Conexiones(), '\n')
print(reflector.GetL2Conexiones(), '\n')
#msg='el sistema tegumentario contribuye a la homeostasis, a través de la protección del cuerpo y la regulación de la temperatura corporal'
msg = 'hola mundo, d'
print('Mensaje original',msg)
text = encryptor.Cifrar(msg)
print('Encriptado',text)
#print('Desencriptado sin reset',encryptor.Decifrar(text))
#encryptor.resetPosicion([1,1,1])
#text2 = encryptor.Cifrar(text)
#print('Desencriptado con cifrar',text2)
encryptor.resetPosicion([1,1,1])
print('Desencriptado con decifrar y reset',encryptor.Decifrar(text))


'''
#Leemos el archivo
filename = input("Ingrese el nombre del archivo: ")
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