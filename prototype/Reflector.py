from random import sample

class Reflector:
    def __init__(self) -> None:
        self.L1conexiones=[]
        self.L2conexiones=[]

    def GetL1Conexiones(self):
        return self.L1conexiones
    def GetL2Conexiones(self):
        return self.L2conexiones

    #n es la cantidad de caracteres
    def CrearReflector(self,Caracteres):
        n=len(Caracteres)
        conexiones=sample(Caracteres,int(n/2))
        self.L1conexiones=conexiones
        for i in Caracteres:
            if i not in self.L1conexiones:
                self.L2conexiones.append(i)

        return self
    
    def Reflectar(self,Letra):
        if Letra in self.L1conexiones:
            return self.L2conexiones[self.L1conexiones.index(Letra)]
        else:
            return self.L1conexiones[self.L2conexiones.index(Letra)]