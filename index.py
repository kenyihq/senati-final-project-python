# Importamos la libreria Tkinter para iniciar la interfaz gráfica
from tkinter import *

# Utilizaremos POO

class User:

    # Empezamos a construir
    def __init__(self, window):
        self.wind = window
        self.wind.title("EL TORNILLO FELIZ")


# Aqui empieza a ejecutarse el código
if __name__ == '__main__':
    window = Tk()
    aplication = User(window)
    window.geometry("400x500")
    window.mainloop()