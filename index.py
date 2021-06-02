# Importamos la libreria Tkinter para iniciar la interfaz gráfica
from tkinter import ttk
from tkinter import *

# Usaremos la base de datos SQLite3, para guardar los datos de los clientes
# Importamos
import sqlite3

# Utilizaremos POO

class Client:
    # Guardamos la ubicacion relativa de la base de datos en una variable
    db_name = "database.db"

    # Empezamos a construir
    def __init__(self, window):
        self.wind = window
        self.wind.title("EL TORNILLO FELIZ")

        # Creamos el titulo
        self.frame = LabelFrame(self.wind, text = "Ferretería El Tornillo Feliz", font = "Arial")
        self.frame.grid(row = 0, column = 0, columnspan = 2)

        # Ingresar datos
        Label(self.frame, text = "DNI :").grid(row = 1, column = 0)
        self.dni = Entry(self.frame)
        self.dni.grid(row = 1, column = 1, pady = 10)
        self.dni.focus()

        # Creamos boton de buscar
        self.search = Button(self.frame, text = "Buscar", command = self.search_client)
        self.search.grid(row = 1, column = 2)
        
        Label(self.frame, text = "Apellidos :").grid(row = 2, column = 0)
        self.last_name = Entry(self.frame)
        self.last_name.grid(row = 2, column = 1, pady = 10)

        Label(self.frame, text = "Nombres :").grid(row = 2, column = 2)
        self.name = Entry(self.frame)
        self.name.grid(row = 2, column = 3, pady = 10)

        Label(self.frame, text = "Dirección :").grid(row = 3, column = 0)
        self.addres = Entry(self.frame)
        self.addres.grid(row = 3, column = 1, pady = 10)

        Label(self.frame, text = "Ciudad : ").grid(row = 3, column = 2)
        self.city = Entry(self.frame)
        self.city.grid(row = 3, column = 3, pady = 10)

        Label(self.frame, text = "Teléfono :").grid(row = 4, column = 0)
        self.phone = Entry(self.frame)
        self.phone.grid(row = 4, column = 1, pady = 10)

        # Creamos boton de agregar datos
        self.add_dates = Button(self.frame, text = "GUARDAR DATOS", command = self.save_dates)
        self.add_dates.grid(row = 6, column = 1, pady = 20)

        # Creamos boton de imprimir cliente
        self.print_dates = Button(self.frame, text = "IMPRIMIR", command = self.println)
        self.print_dates.grid(row = 6, column = 2, pady = 20)

        # Cramos mensaje de accion
        self.message = Label(self.frame, text="", fg = "red")
        self.message.grid(row = 5, column = 1, columnspan = 2, sticky = W + E)

        # Creamos la tabla de los productos de la tienda
        self.tab = ttk.Treeview(height = 10, columns = 2)
        self.tab.grid(row = 6, column = 0, columnspan = 2)
        self.tab.heading("#0", text = "Producto", anchor = CENTER)
        self.tab.heading("#1", text = "Precio", anchor = CENTER)

    # Creamos funcion para hacer la conexion con la base de datos
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Creamos funcion para validar si existen datos en la tabla
    def validated(self):
        return len(self.dni.get()) != 0 and len(self.dni.get()) != 0 and len(self.dni.get()) != 0 and len(self.dni.get()) != 0 and len(self.dni.get()) != 0 and len(self.dni.get()) != 0

    # Creamos funcion para agregar datos a la base de datos Client
    def add_client(self):
        if self.validated():
            query = "INSERT INTO Client VALUES(NULL, ?, ?, ?, ?, ?, ?)"
            parameters = (self.dni.get(), self.last_name.get(), self.name.get(), self.addres.get(), self.city.get(), self.phone.get())
            self.run_query(query, parameters)
            self.print_txt()
            self.message["text"] = "Guardado correctamente"

        else:
            self.message["text"] = "¡SE REQUIEREN TODOS LOS CAMPOS!"
            
    # Creamos funcion de buscar cliente
    def search_client(self):
        Label(self.frame, text = f"{self.dni.get()} no existe", fg = "red").grid(row = 1, column = 3)

    # Creamos funcion para guardar los datos 
    def save_dates(self):
        self.add_client()
        self.dni.delete(0, END)
        self.last_name.delete(0, END)
        self.name.delete(0, END)
        self.addres.delete(0, END)
        self.city.delete(0, END)
        self.phone.delete(0, END)

    # Creamos función para imprimir en consola    
    def println(self):
        
        print(f"DNI : {self.dni.get()}")
        print(f"Apellidos : {self.last_name.get()}")
        print(f"Nombres : {self.name.get()}")
        print(f"Dirección : {self.addres.get()}")
        print(f"Ciudad : {self.city.get()}")
        print(f"Teléfono : {self.phone.get()}")

    # Creamos función para imprimir los datos en un TXT
    def print_txt(self):
        print_display = f"NUEVO CLIENTE\nDNI : {self.dni.get()}\nApellidos : {self.last_name.get()}\nNombres : {self.name.get()}\nDirección : {self.addres.get()}\nCiudad : {self.city.get()}\nTeléfono : {self.phone.get()}\n"
        file = open("nuevo-cliente.txt", "w")
        file.write(print_display)
        file.close()
        
# Aqui empieza a ejecutarse el código
if __name__ == '__main__':
    window = Tk()
    aplication = Client(window)
    window.geometry("400x500")
    window.mainloop()