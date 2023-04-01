'''
Date: 31/03/2023 - 22:30
Authors: Juan Jose Espinoza Mendez and Andres Palacio Sanchez
Repository of the project: https://github.com/andrepalacio/enigma-gram.git
'''

from random import sample

class Reflector:
    def __init__(self):
        self.L1conexiones=[]
        self.L2conexiones=[]

    def GetL1Conexiones(self):
        return self.L1conexiones
    def GetL2Conexiones(self):
        return self.L2conexiones
    
    def SetL1Conexiones(self, w):
        self.L1conexiones = w
    def SetL2Conexiones(self, w):
        self.L2conexiones = w

    #n es la cantidad de caracteres
    def createReflector(self,Caracteres):
        n=len(Caracteres)
        removed = 0
        if n%2!=0: #si n es impar
            n-=1
            removed = Caracteres.pop(n)
        conexiones=sample(Caracteres,int(n/2))
        self.L1conexiones=conexiones
        for i in Caracteres:
            if i not in self.L1conexiones:
                self.L2conexiones.append(i)
        if removed != 0: #si n es impar
            self.L1conexiones.append(removed)
            self.L2conexiones.append(removed)
            Caracteres.append(removed)

        return self
    
    def reflect(self,Letra):
        if Letra in self.L1conexiones:
            return self.L2conexiones[self.L1conexiones.index(Letra)]
        else:
            return self.L1conexiones[self.L2conexiones.index(Letra)]