'''
Date: 31/03/2023 - 22:30
Authors: Juan Jose Espinoza Mendez and Andres Palacio Sanchez
Repository of the project: https://github.com/andrepalacio/enigma-gram.git
'''

from reflector import Reflector
from rotor import Rotor

class Enigma:
    def __init__(self, characters): #basic definition
        self.characters = characters
        self.listRotors = []
        self.listConts = []
        self.initialPos = []
        self.reflector = Reflector()

    def createMachine(self, nRotors:int, iPosition:list):
        self.initialPos = iPosition
        n = 0
        while n < nRotors: #creation of n rotors
            self.listRotors.append(Rotor(self.characters, iPosition[n]))
            self.listConts.append(1)
            n+=1
        self.reflector.createReflector(self.characters)
    
    #show the info of the machine
    def getData(self):
        print(self.characters,'\n')
        n=0
        while n < len(self.listRotors):
            print(self.listRotors[n].wiring,'\n')
            n+=1
        print(self.reflector.GetL1Conexiones())
        print(self.reflector.GetL2Conexiones(),'\n')
        print(self.initialPos, self.listConts)

    def setCharacters(self, chars):
        self.characters = chars

    #restore initial positions of the rotors
    def resetPositions(self):
        for i in range(0, len(self.initialPos)):
            self.listRotors[i].setPosition(self.initialPos[i])
            self.listConts[i]=1

    def code(self, message:str):
        codeMessage = ""
        for letter in message:
            codeLetter = letter
            if len(self.listRotors) != 0:
                codeLetter = self.characters.index(letter)
            n = len(self.listRotors)-1
            while n >= 0: #coding through rotors
                codeLetter = self.listRotors[n].code(codeLetter)
                n-=1
            
            if len(self.listRotors) != 0:
                codeLetter = self.listRotors[0].wiring[codeLetter]
            codeLetter = self.reflector.reflect(codeLetter) #coding in reflector

            i = 0
            n = len(self.listRotors)-1
            if len(self.listRotors) != 0:
                codeLetter = self.listRotors[0].wiring.index(codeLetter)
            while i <= n: #coding through rotors to back
                codeLetter = self.listRotors[i].code(codeLetter)
                i+=1
            
            while n >= 0: #rotors rotation
                if n==(len(self.listRotors)-1):
                    self.listRotors[n].rotate()
                    self.listConts[n] += 1
                else:
                    if (self.listConts[n+1]%26)==0:
                        self.listRotors[n].rotate()
                        self.listConts[n] += 1
                n-=1
            
            if len(self.listRotors) != 0: #convertion from int to char
                codeMessage+=self.characters[codeLetter]
            else:
                codeMessage+=codeLetter       
        return codeMessage
    
    def decode(self, message:str):
        codeMessage = ""
        for letter in message:
            codeLetter = letter
            if len(self.listRotors) != 0:
                codeLetter = self.characters.index(letter)
            n = len(self.listRotors)-1
            while n >= 0: #decoding through rotors
                codeLetter = self.listRotors[n].decode(codeLetter)
                n-=1

            if len(self.listRotors) != 0:
                codeLetter = self.listRotors[0].wiring[codeLetter]
            codeLetter = self.reflector.reflect(codeLetter) #decoding in reflector

            i = 0
            n = len(self.listRotors)-1
            if len(self.listRotors) != 0:
                codeLetter = self.listRotors[0].wiring.index(codeLetter)
            while i <= n: #decoding through rotors to back
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

            if len(self.listRotors) != 0: #convertion from int to char
                codeMessage+=self.characters[codeLetter]
            else:
                codeMessage+=codeLetter       
        return codeMessage

    def export_configuration(self):
        rotors_config = []
        if len(self.listRotors) != 0:
            n = len(self.listRotors)-1
            while n >= 0: 
                config = self.listRotors[n].getWiring()
                rotors_config.append(config)
                n-=1
        reflector_config = []
        reflector_config.append(self.reflector.GetL1Conexiones())
        reflector_config.append(self.reflector.GetL2Conexiones())
        #creates a dictionary of lists about the machine configuration
        configuration = {'characters':self.characters ,'rotors':rotors_config, 'reflector':reflector_config,'initialPos': self.initialPos}
        return configuration
    
    def import_configuration(self, configuration:list):
        #takes a list of lists with the machine configuration
        self.setCharacters(configuration[0])
        rotors_config = configuration[1]
        positions = configuration[3]
        if len(rotors_config) != 0:
            n = len(rotors_config)-1
            self.initialPos = positions
            while n >= 0:
                rotor = Rotor(self.characters, positions[n])
                rotor.setWiring(rotors_config[n])
                self.listRotors.append(rotor)
                self.listConts.append(1)
                n-=1
            self.resetPositions()
        reflector_config = configuration[2]
        self.reflector = Reflector()
        self.reflector.SetL1Conexiones(reflector_config[0])
        self.reflector.SetL2Conexiones(reflector_config[1])