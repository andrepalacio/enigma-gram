from random import sample

class Rotor():
    def __init__(self, characters, position):
        n = len(characters)
        self.wiring = sample(characters,n)
        self.position = position

    def setPosition(self, n):
        self.position=n

    def rotate(self):
        self.position=(self.position+1)%len(self.wiring)

    def code(self, letter):
        index=(letter+self.position)%len(self.wiring)
        return index
    
    def decode(self, letter):
        index=((letter-self.position)+len(self.wiring))%len(self.wiring)
        return index