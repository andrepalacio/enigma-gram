'''
Date: 31/03/2023 - 22:30
Authors: Juan Jose Espinoza Mendez and Andres Palacio Sanchez
Repository of the project: https://github.com/andrepalacio/enigma-gram.git
'''

from random import sample

class Rotor():
    def __init__(self, characters, position):
        n = len(characters)
        self.wiring = sample(characters,n)
        self.position = position

    def getWiring(self):
        return self.wiring
    
    def setWiring(self, w):
        self.wiring=w

    def setPosition(self, n):
        self.position=n

    def rotate(self):
        self.position=(self.position+1)%len(self.wiring)

    #method used to encrypt
    def code(self, letter):
        index=(letter+self.position)%len(self.wiring)
        return index
    
    #method used to decrypt
    def decode(self, letter):
        index=((letter-self.position)+len(self.wiring))%len(self.wiring)
        return index