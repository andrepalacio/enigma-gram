from machine import Enigma

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

enigma=Enigma(chars)
enigma.createMachine(3)
enigma.listRotors[0].wiring=[1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14]
enigma.listRotors[1].wiring=[0,9,3,10,18,8,17,20,23,1,11,7,22,19,12,2,16,6,25,13,15,24,5,21,14,4]
enigma.listRotors[2].wiring=[4,10,12,5,11,6,3,16,21,25,13,19,14,22,24,7,23,20,18,15,0,8,1,17,2,9]
enigma.reflector.L1connection=[0,1,2,3,4,5,6,8,9,10,12,19,21]
enigma.reflector.L2connection=[24,17,20,7,16,18,11,15,23,13,14,25,22]

print(chars, '\n')
enigma.getData()

msg="HOLAMUNDO"
print("Mensaje original:",msg)
cmsg = enigma.code(msg)

print("\nMensaje encriptado:",cmsg)

enigma.setPositions([0,0,0])
cmsg2 = enigma.code(cmsg)
print("\nMensaje desencriptado:",cmsg2)