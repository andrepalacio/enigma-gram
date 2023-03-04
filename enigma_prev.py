import string

class Rotor:
    def __init__(self, wiring, notch, position):
        self.wiring = wiring
        self.notch = notch
        self.offset = position
        self.position = string.ascii_uppercase.index(position)

    def rotate(self):
        self.position = (self.position + 1) % 26
        self.offset = string.ascii_uppercase[self.position]

    def forward(self, letter):
        index = (string.ascii_uppercase.index(letter) + self.position) % 26
        letter = self.wiring[index]
        index = (string.ascii_uppercase.index(letter) - self.position) % 26
        return string.ascii_uppercase[index]

    def backward(self, letter):
        index = (string.ascii_uppercase.index(letter) + self.position) % 26
        letter = string.ascii_uppercase[self.wiring.index(string.ascii_uppercase[index])]
        index = (string.ascii_uppercase.index(letter) - self.position) % 26
        return string.ascii_uppercase[index]

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, letter):
        index = string.ascii_uppercase.index(letter)
        letter = self.wiring[index]
        index = string.ascii_uppercase.index(letter)
        return string.ascii_uppercase[index]

class Enigma:
    def __init__(self, rotor_configs, reflector_config, positions):
        self.rotors = []
        for rotor_config, position in zip(rotor_configs, positions):
            wiring, notch = rotor_config
            rotor = Rotor(wiring, notch, position)
            self.rotors.append(rotor)
        self.reflector = Reflector(reflector_config)

    def encrypt(self, plaintext):
        ciphertext = ''
        for letter in plaintext:
            # Rotate rotors before encryption
            self.rotors[0].rotate()
            if self.rotors[0].offset == self.rotors[0].notch:
                self.rotors[1].rotate()
            if self.rotors[1].offset == self.rotors[1].notch:
                self.rotors[2].rotate()

            if ord(letter) != 32:
                # Pass letter through rotors in forward direction
                for rotor in self.rotors:
                    letter = rotor.forward(letter)

                # Pass letter through reflector
                letter = self.reflector.reflect(letter)

                # Pass letter through rotors in backward direction
                for rotor in reversed(self.rotors):
                    letter = rotor.backward(letter)

            # Add encrypted letter to ciphertext
            ciphertext += letter

        return ciphertext

# Configuración de los rotores
rotor_configs = [('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
                 ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
                 ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')]

# Configuración del reflector
reflector_config = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

# Posiciones iniciales de los rotores
positions = ['A', 'A', 'A']

# Creación de una máquina Enigma con la configuración anterior
enigma = Enigma(rotor_configs, reflector_config, positions)

# Mensaje a cifrar
plaintext = 'HELLO WORLD'

# Cifrado del mensaje
ciphertext = enigma.encrypt(plaintext)

# Impresión del mensaje cifrado
print(ciphertext)

enigma2 = Enigma(rotor_configs, reflector_config, positions)

print(enigma2.encrypt(ciphertext))
