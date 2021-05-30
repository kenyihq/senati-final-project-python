# Importamos la libreria Tkinter para iniciar la interfaz gráfica
from tkinter import *

# Utilizaremos POO

class User:

    # Empezamos a construir
    def __init__(self, window):
        self.wind = window
        self.wind.title("EL TORNILLO FELIZ")

        # Creamos el titulo
        title = Label(self.wind, text = "Ferretería El Tornillo Feliz", font = "Arial")
        title.grid(row = 0, column = 0, columnspan = 5, pady = 20)

        # Ingresar datos
        Label(self.wind, text = "DNI :").grid(row = 2, column = 1)
        self.dni = Entry(self.wind)
        self.dni.grid(row = 2, column = 2, pady = 10)
        self.dni.focus()

        Label(self.wind, text = "Apellidos :").grid(row = 3, column = 1)
        self.last_name = Entry(self.wind)
        self.last_name.grid(row = 3, column = 2, pady = 10)

        Label(self.wind, text = "Nombres :").grid(row = 3, column = 3)
        self.name = Entry(self.wind)
        self.name.grid(row = 3, column = 4, pady = 10)

        Label(self.wind, text = "Dirección :").grid(row = 4, column = 1)
        self.addres = Entry(self.wind)
        self.addres.grid(row = 4, column = 2, pady = 10)

        Label(self.wind, text = "Teléfono :").grid(row = 5, column = 1)
        self.phone = Entry(self.wind)
        self.phone.grid(row = 5, column = 2, pady = 10)

        # Creamos boton de agregar datos

        self.add_dates = Button(self.wind, text = "GUARDAR DATOS", command = self.save_dates)
        self.add_dates.grid(row = 7, column = 1, pady = 20, sticky = W + E)

        # Cramos mensaje de accion
        self.message = Label(text="", fg = "red")
        self.message.grid(row = 6, column = 1, columnspan = 2, sticky = W + E)

    def save_dates(self):
        self.message["text"] = "Guardado correctamente"
        self.dni.delete(0, END)
        self.last_name.delete(0, END)
        self.name.delete(0, END)
        self.addres.delete(0, END)
        self.phone.delete(0, END)
        
        

        
# Aqui empieza a ejecutarse el código
if __name__ == '__main__':
    window = Tk()
    aplication = User(window)
    window.geometry("500x600")
    window.mainloop()