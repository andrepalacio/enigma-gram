from reflector import Reflector
from rotor import Rotor

class Enigma:
    def __init__(self, characters:list):
        self.characters = characters
        self.listRotors = []
        self.reflector = Reflector()

    def createMachine(self, nRotors:int):
        n = 0
        while n < nRotors:
            self.listRotors.append(Rotor(self.characters, 0))
            n+=1
        self.reflector.createReflector(self.characters)
        
    def getData(self):
        n=0
        while n < len(self.listRotors):
            print("Rotor ",n,": ",self.listRotors[n].wiring,'\n')
            n+=1
        print(self.reflector.GetL1connection())
        print(self.reflector.GetL2connection(),'\n')

    def setPositions(self, lPositions:list):
        i = 0
        for n in lPositions:
            self.listRotors[i].setPosition(n)
            i+=1

    def code(self, message:str):
        codeMessage = ""
        for letter in message:
            codeLetter = self.characters.index(letter)
            n = 0
            while n < len(self.listRotors):
                if n == 0:
                    codeLetter = self.listRotors[n].forward_code(codeLetter,0)
                else:
                    codeLetter = self.listRotors[n].forward_code(codeLetter,self.listRotors[n-1].position)
                n+=1
            n = len(self.listRotors)-1
            codeLetter = self.reflector.reflect(codeLetter,self.listRotors[n])
            while n >= 0:
                if n == 0:
                    codeLetter = self.listRotors[n].backward_code(codeLetter,0)
                else:
                    codeLetter = self.listRotors[n].backward_code(codeLetter,self.listRotors[n-1].position)
                n-=1
            #Giros
            i=0
            while i<=len(self.listRotors)-1:
                if self.listRotors[i].position==len(self.characters)-1:
                    self.listRotors[i].position=0
                    self.listRotors[i+1].position+=1
                if i==0:
                    self.listRotors[i].position+=1
                i=i+1
            codeMessage+=self.characters[codeLetter]
        return codeMessage