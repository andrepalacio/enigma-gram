from random import sample

class Reflector:
    def __init__(self):
        self.L1connection=[]
        self.L2connection=[]

    def GetL1connection(self):
        return self.L1connection
    def GetL2connection(self):
        return self.L2connection
    #n es la cantidad de caracteres
    def createReflector(self,characters):
        n=len(characters)
        connections=sample(range(0,n),n)
        self.L1connection=sample(connections,int(n/2))
        for i in connections:
            if i not in self.L1connection:
                self.L2connection.append(i)
                j=i
        if type(n/2)==float:
            self.L1connection.append(i)
    
    def reflect(self,Letra,RFinal):
        if Letra-RFinal.position<0:
            if (Letra-RFinal.position+len(RFinal.wiring)) in self.L1connection:
                return self.L2connection[self.L1connection.index(Letra-RFinal.position+len(RFinal.wiring))]+RFinal.position
            else:
                return self.L1connection[self.L2connection.index(Letra-RFinal.position+len(RFinal.wiring))]+RFinal.position
        elif Letra-RFinal.position in self.L1connection:
            Letter=self.L2connection[self.L1connection.index(Letra-RFinal.position)]+RFinal.position
            if Letter<0:
                Letter=Letter+len(RFinal.wiring)
            elif Letter>(len(RFinal.wiring)-1):
                Letter=Letter-(len(RFinal.wiring)) 
            return Letter
        else:
            Letter=self.L1connection[self.L2connection.index(Letra-RFinal.position)]+RFinal.position
            if Letter<0:
                Letter=Letter+len(RFinal.wiring)
            elif Letter>(len(RFinal.wiring)-1):
                Letter=Letter-(len(RFinal.wiring)) 
            return Letter