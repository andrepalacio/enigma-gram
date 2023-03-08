from random import shuffle

class Rotor:
    def __init__(self) -> None:
        self.posicion=1
        self.conexiones=[]
    
    def SetPosicion(self,posicion:int):
        self.posicion=posicion
    def GetPosicion(self):
        return self.posicion
    def GetConexiones(self):
        return self.conexiones

    def CrearRotor(self,Caracteres:list):
        Lista=list(Caracteres)
        shuffle(Lista)
        self.conexiones=Lista
        return self
    
    def Girar(self, nCaracteres):
        if self.posicion < nCaracteres:
            self.posicion += 1
        else:
            self.posicion = 1

    def Cifrar(self,Letra,Caracteres):
        lPosicion=Caracteres.index(Letra)
        Letra = (lPosicion+self.posicion)%len(Caracteres)
        return self.conexiones[Letra]
    
    def Decifrar(self,Letra,Caracteres):
        lPosicion=self.conexiones.index(Letra)
        Letra = (lPosicion-self.posicion)%len(Caracteres)
        return Caracteres[Letra]
