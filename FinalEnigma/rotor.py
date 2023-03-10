from random import sample

class Rotor():
    def __init__(self, characters, position):
        n = len(characters)
        self.wiring = sample(range(0,n),n)
        self.position = position

    def setPosition(self, n):
        self.position=n

    #Letter = Index de la letra
    #Position_BR = Position Backward Rotor = Posicion del rotor anterior
    def forward_code(self, letter:int,position_BR):
        position=letter+self.position-position_BR
        if position>(len(self.wiring)-1):
            position=position-(len(self.wiring))
            return self.wiring[position]
        else:
            return self.wiring[position]
    
    #Letter = Index de la letra
    #PositionRotor = Posicion del rotor siguiente  R3 -> R2 -> R1 
    def backward_code(self, letter,positionRotor):
        position=self.wiring.index(letter)-self.position+positionRotor
        if position<0:
            position=position+len(self.wiring)
        elif position>(len(self.wiring)-1):
            position=position-(len(self.wiring)) 
        return (position)
