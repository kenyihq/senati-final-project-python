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
        
        # Ubicación de mi icono
        # self.wind.iconbitmap("D:\\Programacion\\Python\\TKinter\\SenatiProject\\Trabajo-Final-Python\\tornillofelizlogo.ico")

        # Creamos el titulo
        self.frame = LabelFrame(self.wind, text = "Ferretería El Tornillo Feliz", font = "Arial")
        self.frame.grid(row = 0, column = 0, columnspan = 2)

        # Ingresar datos
        Label(self.frame, text = "DNI :").grid(row = 1, column = 0)
        self.dni = Entry(self.frame)
        self.dni.grid(row = 1, column = 1, pady = 10)
        self.dni.focus()

        # Creamos boton de buscar
        self.search = Button(self.frame, text = "Buscar DNI", command = self.search_client)
        self.search.grid(row = 1, column = 2)
        self.message_search = Label(self.frame, text = "", fg = "red")
        self.message_search.grid(row = 1, column = 3)
        
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

        # Creamos boton de guardar datos
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

        ttk.Button(text = "ELIMINAR", command = self.delete_products).grid(row = 7, column = 0, sticky = W + E)
        ttk.Button(text = "EDITAR", command = self.edit_product).grid(row = 7, column = 1, sticky = W + E)

        ttk.Button(text = "AGREGAR PRODUCTOS", command = self.add_products).grid(row = 8, column = 0, columnspan = 2, sticky = W +E)

        self.get_products()

        # Creamos otro frame para mostrar el producto adquirido
        self.frame2 = LabelFrame(self.wind, text = "Resumen de Orden", font = "Arial")
        self.frame2.grid(row = 0, column = 2)

        Label(self.frame2, text = "Este es otro Frame").grid(row = 0, column = 0)
        self.tab_resume = ttk.Treeview(self.frame2, height = 9, columns = 2)
        self.tab_resume.grid(row = 1, column =0, columnspan = 2)
        self.tab_resume.heading("#0", text = "Producto", anchor = CENTER)
        self.tab_resume.heading("#1", text = "Precio Unitario", anchor = CENTER)

        Label(self.frame2, text = "TOTAL").grid(row = 2, column = 0, sticky = W + E)
        Entry(self.frame2, text = "").grid(row = 2, column = 1, sticky = W + E)
    
    # Creamos funcion para agregar nuevos productos
    def add_products(self):
        self.wind_add_products = Toplevel()
        self.wind_add_products.title("AGREGAR PRODUCTO")
        #self.wind_add_products.geometry("400x550")

        frame = LabelFrame(self.wind_add_products, text="REGISTRAR NUEVO PRODUCTO")
        frame.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        # Ingresar nombre
        Label(frame, text = "Nombre :").grid(row = 1, column = 0)
        self.name_prod = Entry(frame)
        self.name_prod.focus()
        self.name_prod.grid(row = 1, column = 1)

        # Ingresar precio
        Label(frame, text = "Precio :").grid(row = 2, column = 0)
        self.price_prod = Entry(frame)
        self.price_prod.grid(row = 2, column = 1)

        # Boton de agregar productos
        ttk.Button(frame, text = "Guardar Producto", command = self.add_new_prod).grid(row = 3, columnspan = 2, sticky = W + E)

        # Mensaje de Notificacion de accion
        # self.message["text"] = f"{self.name_prod} agregado correctamente"

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

    # Creamos función para validar si los campos estan vacios
    def validated_prod(self):
        return len(self.name_prod.get()) != 0 and len(self.price_prod.get()) != 0

    # Creamos funcion para agregar productos a la base de datos Products
    def add_new_prod(self):
        if self.validated_prod():
            query = "INSERT INTO Products VALUES(NULL, ?, ?)"
            parameters = (self.name_prod.get(), self.price_prod.get())
            self.run_query(query, parameters)
            self.message["text"] = f"{self.name_prod.get()} agregado correctamente"
            self.get_products()
            self.wind_add_products.destroy()

        else:
            self.message["text"] = "¡SE REQUIEREN TODOS LOS CAMPOS!"

    # Creamos función para mostrar los productos de la Base de datos en la interfaz principal
    def get_products(self):

        # Limpiando datos de la tabla
        record = self.tab.get_children()
        for elements in record:
            self.tab.delete(elements)
        # Consultando datos de la tabla Productos
        query = "SELECT * FROM Products ORDER BY Product DESC"
        db_row = self.run_query(query)
        # Rellenando datos en la tabla
        for row in db_row:
            self.tab.insert("", 0, text = row[1], values = row[2])
    
    # Eliminar productos de la tabla Products
    def delete_products(self):
        self.message["text"] = ""
        try:
            self.tab.item(self.tab.selection())["text"][0]
        except IndexError as e:
            self.message["text"] = "Selecione un producto"
            return
        self.message["text"] = ""
        name = self.tab.item(self.tab.selection())["text"]
        query = "DELETE FROM Products WHERE Product = ?"
        self.run_query(query, (name, ))
        self.message["text"] = f"{name} a sido eliminado"
        self.get_products()

    # Editar productos de la tabla Product
    def edit_product(self):
        self.message["text"] = ""
        try:
            self.tab.item(self.tab.selection())["text"][0]
        except IndexError as e:
            self.message["text"] = "Selecione un producto"
            return
        old_name = self.tab.item(self.tab.selection())["text"]
        old_price = self.tab.item(self.tab.selection())["values"][0]
        # Creamos una nueva ventana para editar
        self.edit_wind = Toplevel()
        self.edit_wind.title("Editar Producto")

        # Nombre actual
        Label(self.edit_wind, text = "Nombre actual : ").grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name), state = "readonly").grid(row = 0, column = 2)

        # Nuevo nombre
        Label(self.edit_wind, text = "Nuevo nombre : ", fg = "blue").grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Precio actual
        Label(self.edit_wind, text = "Precio actual : ").grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = "readonly").grid(row = 2, column = 2)

        # Nuevo Precio
        Label(self.edit_wind, text = "Nuevo precio : ", fg = "blue").grid(row = 3, column = 1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        # Boton de actualizar
        Button(self.edit_wind, text = "ACTUALIZAR", command = lambda: self.save_update_prod(new_name.get(), old_name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)

    # Creamos funcion para actualizar los cambios en la ventana de editar
    def save_update_prod(self, new_name, old_name, new_price, old_price):
        query = "UPDATE Products SET Product = ?, Price = ? WHERE Product = ? AND Price = ?"
        parameters = (new_name, new_price, old_name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message["text"] = f"{old_name} se actualizo con éxito"
        self.get_products()


    def validate_client(self):
        return len(self.dni.get()) != 0
    
    # Creamos funcion de buscar cliente
    def search_client(self):
        if self.validate_client():
            query = "SELECT * FROM Client WHERE DNI = ?"
            parameters = (self.dni.get())
            self.run_query(query, (parameters, ))
            database_data = self.run_query(query, (parameters, ))
            for self.search_dni in database_data:
                print(self.search_dni)
                self.message_search["text"] = f"{self.dni.get()} encontrado"
                self.delete_dates()
                self.full_dates()
                return

        else:
            self.message_search["text"] = "Ingrese DNI"
            return

        self.delete_dates()
        self.message_search["text"] = f"{self.dni.get()} no existe"

    # Funcion para rellenar los campos si el cliente esta en la base de datos
    def full_dates(self):
        self.last_name.insert(0, f"{self.search_dni[2]}")
        self.name.insert(0, f"{self.search_dni[3]}")
        self.addres.insert(0, f"{self.search_dni[4]}")
        self.city.insert(0, f"{self.search_dni[5]}")
        self.phone.insert(0, f"{self.search_dni[6]}")

    # Creamos función para limpiar los campos al realizar una busqueda
    def delete_dates(self):
        self.last_name.delete(0, END)
        self.name.delete(0, END)
        self.addres.delete(0, END)
        self.city.delete(0, END)
        self.phone.delete(0, END)        

    # Creamos funcion para guardar los datos 
    def save_dates(self):
        self.add_client()
        self.dni.delete(0, END)
        self.delete_dates()        

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
    window.geometry("820x550")
    window.mainloop()