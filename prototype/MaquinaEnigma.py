from Rotor import Rotor
from Reflector import Reflector

class Enigma:
    def __init__(self,Caracteres):
        self.Caracteres=Caracteres
        self.list_rotores=[]
        self.reflector=[]
        self.contRotores=[]
    
    def GetListRotores(self):
        return self.list_rotores
    def GetReflector(self):
        return self.reflector
    def GetContadores(self):
        return self.contRotores

    def CrearMaquina(self,NumRotores):
        #Convertimos los caracteres a una lista
        LCaracteres=list(self.Caracteres)
        #Creamos los rotores
        i=0
        while i < NumRotores:
            rotor=Rotor()
            self.list_rotores.append(rotor.CrearRotor(LCaracteres))
            self.contRotores.append(1)
            i+=1
        #Creamos el reflector
        reflector=Reflector()
        self.reflector=reflector.CrearReflector(LCaracteres)

    def Cifrar(self,Mensaje):
        MensajeCifrado=""
        #Lista de los rotores
        LRotores=self.list_rotores
        for Letra in Mensaje:
            #n es el total de rotores que tiene la maquina
            n=len(LRotores)-1
            #i=0
            LetraCifrada=Letra
            #Pasamos la letra por los N rotores
            while n >= 0:
                if (n+1)==len(self.list_rotores):
                    LetraCifrada=LRotores[n].Cifrar(LetraCifrada,self.Caracteres)
                else:
                    LetraCifrada=LRotores[n].Cifrar(LetraCifrada,LRotores[n+1].GetConexiones())
                n-=1
            #Pasamos la letra por el reflector
            LetraCifrada=self.reflector.Reflectar(LetraCifrada)
            #Nos devolvemos por los N rotores
            i=0
            n=len(LRotores)-1
            while i <= n:
                if i==n:
                    LetraCifrada=LRotores[i].Cifrar(LetraCifrada,self.Caracteres)
                else:
                    LetraCifrada=LRotores[i].Cifrar(LetraCifrada,LRotores[i+1].GetConexiones())
                i+=1
            MensajeCifrado+=LetraCifrada

            nCaracteres = len(self.Caracteres)
            nCont = len(self.contRotores)-1
            while n >= 0:
                if (n+1)==len(self.contRotores):
                    LRotores[n].Girar(nCaracteres)
                    self.contRotores[nCont]+=1
                else:
                    if (self.contRotores[nCont+1]%26)==0:
                        LRotores[n].Girar(nCaracteres)
                        self.contRotores[nCont]+=1
                n-=1
                nCont-=1

        return MensajeCifrado
    
    def Decifrar(self,Mensaje):
        MensajeCifrado=""
        #Lista de los rotores
        LRotores=self.list_rotores
        for Letra in Mensaje:
            #n es el total de rotores que tiene la maquina
            n=len(LRotores)-1
            #i=0
            LetraCifrada=Letra
            #Pasamos la letra por los N rotores
            while n >= 0:
                if (n+1)==len(self.list_rotores):
                    LetraCifrada=LRotores[n].Decifrar(LetraCifrada,self.Caracteres)
                else:
                    LetraCifrada=LRotores[n].Decifrar(LetraCifrada,LRotores[n+1].GetConexiones())
                n-=1
            #Pasamos la letra por el reflector
            LetraCifrada=self.reflector.Reflectar(LetraCifrada)
            #Nos devolvemos por los N rotores
            i=0
            n=len(LRotores)-1
            while i <= n:
                if i==n:
                    LetraCifrada=LRotores[i].Decifrar(LetraCifrada,self.Caracteres)
                else:
                    LetraCifrada=LRotores[i].Decifrar(LetraCifrada,LRotores[i+1].GetConexiones())
                i+=1
            MensajeCifrado+=LetraCifrada

            nCaracteres = len(self.Caracteres)
            nCont = len(self.contRotores)-1
            while n >= 0:
                if (n+1)==len(self.contRotores):
                    LRotores[n].Girar(nCaracteres)
                    self.contRotores[nCont]+=1
                else:
                    if (self.contRotores[nCont+1]%26)==0:
                        LRotores[n].Girar(nCaracteres)
                        self.contRotores[nCont]+=1
                n-=1
                nCont-=1

        return MensajeCifrado
    
    def resetPosicion(self, posiciones:list):
        n = 0
        for rotor in self.list_rotores:
            rotor.SetPosicion(posiciones[n])
            n+=1

