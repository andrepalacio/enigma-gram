import tkinter as tk
from tkinter import messagebox
from os import path
from machine import Enigma
from json import dump, load

#creates a enigma machine based on a configuration
def create_machine(chars, msg):
    global enigma
    enigma = Enigma(chars)
    if len(config) == 2:
        enigma.createMachine(config[0], config[1])
    elif len(config) == 4:
        enigma.import_configuration(config)       
    enigma.getData()
    encrypt_process(msg)

#select the text to encrypt and use its characters to configure the machine
def reading():
    filename = entryl.get()+'.txt'
    if path.exists(filename):
        with open(filename, 'r',errors='ignore') as f:
            msg = f.read()
            f.close()
        #Read characters from the book
        uCharacters = set(msg)
        chars = sorted(list(uCharacters))
        create_machine(chars, msg)
    else:
        label = tk.Label(r_window, text="No existe un archivo con\nel nombre ingresado")
        label.pack(pady=10, padx=10)

#creates the window of book selection
def read_book():
    global r_window, entryl
    r_window = tk.Toplevel(root)
    r_window.title("Seleccionar Libro")
    label = tk.Label(r_window, text="Ingrese nombre del archivo:\n(ejemplo: Odisea)")
    label.pack(pady=10, padx=10)
    entryl = tk.Entry(r_window)
    entryl.pack(pady=20, padx=10)
    search_button = tk.Button(r_window, text="Buscar libro", command=reading)
    search_button.pack(pady=10, padx=10)

#encrypt and decrypt the message, it check if the configuration is appropriate
def encrypt_process(msg:str):
    flag = False
    try:
        encrypted_msg = enigma.code(msg)
        flag = True
    except:
        messagebox.showinfo("Error", "La configuracion no permite encriptar/desencriptar\nel archivo, es posible que la configuracion guardada\nno incluya los caracteres correctos\nIntente creando una nueva maquina")

    if flag: #this part only execute after checking that is possible to code the message
        file = open("LibroCifrado.txt","w")
        file.write(encrypted_msg)
        file.close()
        enigma.resetPositions()
        decrypted_msg = enigma.decode(encrypted_msg)
        file = open("LibroDecifrado.txt","w")
        file.write(decrypted_msg)
        file.close()

        #window to see the message
        e_window = tk.Toplevel(root)
        e_window.title("Proceso de encriptado")
        global slabel
        slabel = tk.Text(e_window)
        slabel.pack(fill=tk.BOTH, expand=True)

        #action buttons in the window
        se_button = tk.Button(e_window, text="Mostrar texto encriptado", command=show_encrypted)
        se_button.pack(side=tk.LEFT,padx=10, pady=10)

        sd_button = tk.Button(e_window, text="Mostrar texto desencriptado", command=show_decrypted)
        sd_button.pack(side=tk.LEFT, padx=10, pady=10)

        save_buton = tk.Button(e_window, text="Guardar configuracion",command=save_config)
        save_buton.pack(side=tk.LEFT, padx=10, pady=10)

#use the export method and saves configuration of the machine in a json file
def save_config():
    with open('charst.json', 'w') as f:
        dump(enigma.export_configuration(), f)
    window = tk.Toplevel(root)
    window.title("Configuracion guardada")
    label = tk.Label(window, text="Configuracion guardada exitosamente! \n\n Muy importante esta configuracion solo servira si el libro a encriptar/desencriptar \ntiene los mismos caracteres con los cuales se creó la configuración")
    label.pack(pady=10, padx=10)
    create_button = tk.Button(window, text="Aceptar", command=window.destroy)
    create_button.pack(pady=10, padx=10)

#show encrypted message in the window
def show_encrypted():
    slabel.delete('1.0', tk.END)
    file = open("LibroCifrado.txt","r")
    msg = file.read()
    file.close()
    slabel.insert(tk.END, msg)

#show decrypted message in the window
def show_decrypted():
    slabel.delete('1.0', tk.END)
    file = open("LibroDecifrado.txt","r")
    msg = file.read()
    file.close()
    slabel.insert(tk.END, msg)

#actions to upload a saved configuration for the machine
def yes_callback():
    global config
    yes_window = tk.Toplevel(root)
    yes_window.title("Seleccionar Configuración")
    file_path = "./charst.json"
    if path.exists(file_path): #check if file exists
        with open('charst.json', 'r') as f:
            config_dict = load(f)
            f.close()
        config = list(config_dict.values())
        label = tk.Label(yes_window, text="Configuración cargada\nexitosamente")
        label.pack(pady=10, padx=10)
        read_book()
    else:
        label = tk.Label(yes_window, text="No existe un archivo con\nla última configuración")
        label.pack(pady=10, padx=10)

#secondary function used to create a new configuration
def accept():
    global config
    t1 = entry.get() #read number of rotors
    t2 = list(entry2.get()) #read initial positions as a string and converts to list
    if int(t1) < 0 or len(t2)!=int(t1):
        window = tk.Toplevel(root)
        window.title("Ingresó mal la configuración")
        label = tk.Label(window, text="Porfavor vuelva a ingresar al configuración\n Recuerde que puede ingresar rotores desde 0 \n Y no olvide poner las posiciones iniciales \nPor ejemplo si ingresa 3 rotores debe ingresar las tres posiciones asi 000")
        label.pack(pady=10, padx=10)
        create_button = tk.Button(window, text="Volver a intentar", command=window.destroy)
        create_button.pack(pady=10, padx=10)
        no_callback()
    else:
        #set config as integers
        for i in range(0,len(t2)):
            t2[i] = int(t2[i])
        config = [int(t1), list(t2)]
        read_book()

#actions to create a configuration for the machine
def no_callback():
    global entry, entry2
    no_window = tk.Toplevel(root)
    no_window.title("Seleccionar Configuración")

    label = tk.Label(no_window, text="Ingrese número de rotores\nque desea usar:")
    label.pack(pady=10, padx=10)
    entry = tk.Entry(no_window)
    entry.pack(pady=20, padx=10)
    label2 = tk.Label(no_window, text="Ingrese la posicion inicial\nde los rotores que desea usar:\n(ejemplo: 111 para 3 rotores)")
    label2.pack(pady=10, padx=10)
    entry2 = tk.Entry(no_window)
    entry2.pack(pady=20, padx=10)
    create_button = tk.Button(no_window, text="Crear", command=accept)
    create_button.pack(pady=10, padx=10)

# Create the main window
root = tk.Tk()
root.title("Seleccionar configuración")

label = tk.Label(root, text="¿Desea utilizar la última\nconfiguración guardada?:")
label.pack(padx=10, pady=10)

yes_button = tk.Button(root, text="Sí", command=yes_callback)
yes_button.pack(side=tk.LEFT, padx=10, pady=10)

no_button = tk.Button(root, text="No", command=no_callback)
no_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the main loop
root.mainloop()