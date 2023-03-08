from reflector import Reflector
from rotor import Rotor

class Enigma:
    def __init__(self, characters:list):
        self.characters = characters
        self.listRotors = []
        self.listConts = []
        self.reflector = Reflector()

    def createMachine(self, nRotors:list):
        n = 0
        while n < nRotors:
            self.listRotors.append(Rotor(self.characters, 1))
            self.listConts.append(1)
            n+=1
        self.reflector.createReflector(self.characters)
        
    def getData(self):
        n=0
        while n < 3:
            print(self.listRotors[n].wiring,'\n')
            n+=1
        print(self.reflector.GetL1Conexiones())
        print(self.reflector.GetL2Conexiones(),'\n')

    def setPositions(self, lPositions:list):
        i = 0
        for n in range(len(lPositions)):
            self.listRotors[i].setPosition(lPositions[n])
            self.listConts[i]=1
            i+=1

    def code(self, message:str):
        codeMessage = ""
        for letter in message:
            codeLetter = self.characters.index(letter)
            n = len(self.listRotors)-1
            while n >= 0:
                codeLetter = self.listRotors[n].code(codeLetter)
                n-=1
            
            codeLetter = self.listRotors[0].wiring[codeLetter]
            codeLetter = self.reflector.reflect(codeLetter)

            i = 0
            n = len(self.listRotors)-1
            codeLetter = self.listRotors[0].wiring.index(codeLetter)
            while i <= n:
                codeLetter = self.listRotors[i].code(codeLetter)
                i+=1
            
            while n >= 0:
                if n==(len(self.listRotors)-1):
                    self.listRotors[n].rotate()
                    self.listConts[n] += 1
                else:
                    if (self.listConts[n+1]%26)==0:
                        self.listRotors[n].rotate()
                        self.listConts[n] += 1
                n-=1
            
            codeMessage+=self.characters[codeLetter]
        
        return codeMessage
    
    def decode(self, message:str):
        codeMessage = ""
        for letter in message:
            codeLetter = self.characters.index(letter)
            n = len(self.listRotors)-1
            while n >= 0:
                codeLetter = self.listRotors[n].decode(codeLetter)
                n-=1

            codeLetter = self.listRotors[0].wiring[codeLetter]
            codeLetter = self.reflector.reflect(codeLetter)

            i = 0
            n = len(self.listRotors)-1
            codeLetter = self.listRotors[0].wiring.index(codeLetter)
            while i <= n:
                codeLetter = self.listRotors[i].decode(codeLetter)
                i+=1
            
            while n >= 0:
                if n==(len(self.listRotors)-1):
                    self.listRotors[n].position += 1
                    self.listConts[n] += 1
                else:
                    if (self.listConts[n+1]%26)==0:
                        self.listRotors[n].position += 1
                        self.listConts[n] += 1
                n-=1

            try:
                codeMessage+=self.characters[codeLetter]
            except:
                print(codeLetter)
                exit()
        
        return codeMessage


