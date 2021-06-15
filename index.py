# Importamos la libreria Tkinter para iniciar la interfaz gráfica
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
# Importamos la librería Pywhatkit para enviar mensjaes por Whatsapp
import pywhatkit
# Importamos la clase Invoice
from invoice import Invoice

# Usaremos la base de datos SQLite3, para guardar los datos de los clientes
# Importamos
import sqlite3

# Utilizaremos POO

class Client:
    # Guardamos la ubicacion relativa de la base de datos en una variable
    db_name = "database.db"

    # Llamamos a la clase Invoice para la impresion 
    invoice = Invoice()

    # Empezamos a construir
    def __init__(self, window):
        self.wind = window
        self.wind.title("EL TORNILLO FELIZ")
        
        # Ubicación de mi icono
        # self.wind.iconbitmap("D:\\Programacion\\Python\\TKinter\\SenatiProject\\Trabajo-Final-Python\\tornillofelizlogo.ico")

        # Creamos el titulo
        self.frame = LabelFrame(self.wind)
        self.frame.grid(row = 0, column = 0)
        Label(self.frame, text = "DATOS DEL CLIENTE", font = "Arial").grid(row = 0, column = 0, columnspan = 4)

        # Ingresar datos
        Label(self.frame, text = "DNI :").grid(row = 1, column = 0)
        self.dni = Entry(self.frame)
        self.dni.grid(row = 1, column = 1, pady = 10, padx = 10)
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

        # Creamos boton para limpiar todos lod datos
        Button(self.frame, text = "Limpiar datos", command = self.delete_button).grid(row = 4, column = 3, sticky = W + E)

        # Creamos boton para actualizar datos
        Button(self.frame, text = "VER CLIENTES", command = self.view_clients).grid(row = 6, column = 0, columnspan = 2, sticky = W + E)

        # Creamos boton de guardar datos
        Button(self.frame, text = "GUARDAR DATOS", command = self.add_client).grid(row = 6, column = 2, columnspan = 2, sticky = W + E)
        
        # Creamos boton de agregar a compra
        Button(self.frame, text = "AGREGAR PARA COMPRAR", command = self.add_tab_products).grid(row = 7, column = 0, columnspan = 4, sticky = W + E)

        # Cramos mensaje de accion
        self.message = Label(self.frame, text="", fg = "red", font = "Arial", pady = 11)
        self.message.grid(row = 5, column = 0, columnspan = 4, sticky = W + E)

        # Creamos la tabla de los productos de la tienda

        frame_products = LabelFrame(self.wind)
        frame_products.grid(row = 1, column = 0)

        Label(frame_products, text = "PRODUCTOS", font = "Arial").grid(row = 0, column = 0, columnspan = 2)
        self.tab = ttk.Treeview(frame_products, height = 10, columns = 2)
        self.tab.grid(row = 1, column = 0, columnspan = 2)
        self.tab.heading("#0", text = "Producto", anchor = CENTER)
        self.tab.heading("#1", text = "Precio", anchor = CENTER)

        ttk.Button(frame_products, text = "ELIMINAR", command = self.delete_products).grid(row = 2, column = 0, sticky = W + E)
        ttk.Button(frame_products, text = "EDITAR", command = self.edit_product).grid(row = 2, column = 1, sticky = W + E)
        ttk.Button(frame_products, text = "AGREGAR PRODUCTOS", command = self.add_products).grid(row = 3, column = 0, columnspan = 2, sticky = W +E)

        # Se inicia esta funcion para traer la lista de los productos a la tabla de productos
        self.get_products()

        # Creamos otro frame para mostrar el producto adquirido
        frame_resume = LabelFrame(self.wind)
        frame_resume.grid(row = 0, column = 2)
        Label(frame_resume, text = "RESUSMEN DE COMPRA", font = "Arial").grid(row = 0, column = 0, columnspan = 2)
        
        # Reservo variales para guardarlos en una lista y mostrarlos en la tabla de resumen
        self.item_price_tab_res = []
        self.item_name = []
        
        # Label(self.frame2, text = "Este es otro Frame").grid(row = 0, column = 0)
        self.tab_resume = ttk.Treeview(frame_resume, height = 9, columns = 2)
        self.tab_resume.grid(row = 1, column =0, columnspan = 2)
        self.tab_resume.heading("#0", text = "Producto", anchor = CENTER)
        self.tab_resume.heading("#1", text = "Precio Unitario", anchor = CENTER)

        Label(frame_resume, text = "TOTAL").grid(row = 2, column = 0, sticky = W + E)
        self.total_price = Label(frame_resume, text = "", font = "Arial", fg = "blue", bg = "azure")
        self.total_price.grid(row = 2, column = 1, rowspan = 2, columnspan = 2, sticky = W+E+N+S)
        #ttk.Button(frame_resume, text = "ELIMINAR PRODUCTO", command = self.delete_resume_tab).grid(row = 3, column = 0, sticky = W + E)
        ttk.Button(frame_resume, text = "LIMPIAR TABLA", command = self.delete_resume_tab).grid(row = 3, column = 0, sticky = W + E)

        # Se inicia esta función para agregar por defecto el delivery        
        self.add_tab_resume()

        # Creamos otr frame para agregar botones

        frame3 = LabelFrame(self.wind)
        Label(frame3, text = "FINALIZAR PEDIDO", font = "Arial").grid(row = 0, column = 0, columnspan = 2)
        frame3.grid(row = 1, column = 2, rowspan = 9)

        # Creamos boton de imprimir cliente
        self.print_dates = Button(frame3, text = "IMPRIMIR ORDEN", font = "Arial", bg = "red", fg = "white", bd = "10", command = self.println)
        self.print_dates.grid(row = 1, column = 0, sticky = W + E, pady = 122, padx = 100)
    
    # Creamos función para mostrar los clientes resgistrdos en la base de datos
    def view_clients(self):
        client_window = Toplevel()
        client_window.title("CLIENTES")

        Label(client_window, text = "CLIENTES REGISTRADOS", font = "Arial").grid(row = 0, column = 0)
        self.tab_client = ttk.Treeview(client_window, columns = (1,2,3,4,5,), height = 20)
        self.tab_client.grid(row = 1, column = 0)
        self.tab_client.heading("#0", text = "DNI", anchor = CENTER)
        self.tab_client.heading("#1", text = "Apellidos", anchor = CENTER)
        self.tab_client.heading("#2", text = "Nombres", anchor = CENTER)
        self.tab_client.heading("#3", text = "Dirección", anchor = CENTER)
        self.tab_client.heading("#4", text = "Ciudad", anchor = CENTER)
        self.tab_client.heading("#5", text = "Teléfono", anchor = CENTER)
        
        # Se inicia esta función para traer los clientes desde la base de datos de la tabla Client
        self.get_clients()

    # Creamos funcion para traer los datos de la base de datos a la tabla gráfica
    def get_clients(self):
        
        # Limpiando datos de la tabla
        record = self.tab_client.get_children()
        for clients in record:
            self.tab.delete(clients)
        # Consultando datos de la tabla Productos
        query = "SELECT * FROM Client ORDER BY LastName ASC"
        db_row = self.run_query(query)
        # Rellenando datos en la tabla
        for client in db_row:
            #print(client)
            self.tab_client.insert("", END, text = client[1], values = (client[2], client[3], client[4], client[5], client[6]))

    # Creamos funcion para agregar nuevos productos
    def add_products(self):
        self.wind_add_products = Toplevel()
        self.wind_add_products.title("AGREGAR PRODUCTO")

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

    # Creamos funcion para hacer la conexion con la base de datos
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Creamos funcion para validar si existen datos en la tabla
    def validated(self):
        return len(self.dni.get()) != 0 and len(self.last_name.get()) != 0 and len(self.name.get()) != 0 and len(self.addres.get()) != 0 and len(self.city.get()) != 0 and len(self.phone.get()) != 0

    # Creamos funcion para agregar datos a la base de datos Client
    def add_client(self):
        if self.validated():
            query = "INSERT INTO Client VALUES(NULL, ?, ?, ?, ?, ?, ?)"
            parameters = (self.dni.get(), self.last_name.get(), self.name.get(), self.addres.get(), self.city.get(), self.phone.get())
            self.run_query(query, parameters)
            self.message["text"] = f"{self.name.get()} agregado correctamente"

        else:
            self.message["text"] = "¡SE REQUIEREN TODOS LOS CAMPOS!"
            return
        self.dni.delete(0, END)
        self.delete_dates() 
            
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
        # Guardamos en una variable el nombre de la selección
        name = self.tab.item(self.tab.selection())["text"]
        # Preguntamos si realmente se quiere eliminar el prodcuto
        if messagebox.askyesno(message=f"Esta seguro de elimiar {name}", title = "Eliminar producto") == True:

            self.message["text"] = ""
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

    # Creamos funcion para validar los campos y posteriormente limpiarlos si en uno o más cassilas hay datos ingresdos
    def validated_button_delete(self):
        return len(self.dni.get()) != 0 or len(self.last_name.get()) != 0 or len(self.name.get()) != 0 or len(self.addres.get()) != 0 or len(self.city.get()) != 0 or len(self.phone.get()) != 0

    # Creamos funcion para eliminar los datos al presionar el el boton de limpiar datos
    def delete_button(self):
        if self.validated_button_delete():
            self.dni.delete(0, END)
            self.delete_dates()
            self.message_search["text"] = ""
            self.message["text"] = "SE LIMPIÓ CORRECTAMENTE"
        else:
            self.message["text"] = "NADA QUE LIMPIAR"

    # Creamos función para mostrar ventanas emergentes al imprimir la orden    
    def println(self):        
        if self.validated():
            self.print_txt()
            messagebox.showinfo("AVISO", message = f"Orden para {self.name.get()} se imprimió correctamente")
            self.send_whatasapp() # Para enviar un mesaje de Whatsapp al cliente
            self.delete_button()   # Esto borra todas las cajas de texto
            self.delete_resume_tab() # Esto borra la tabla de resumen
            self.message["text"] = ""
        else:
            messagebox.showerror("Error",message = "Se nesecitan todos los datos" )
        
    # Creamos función para imprimir los datos en un TXT
    def print_txt(self):
        file = open("nueva-venta.txt", "w")
        file.write(self.invoice.invoice_txt)
        file.write("\tDATOS DEL CLIENTE\n")
        file.write(f"\nDNI        : {self.dni.get()}")
        file.write(f"\nNOMBRE     : {self.name.get()}")
        file.write(f"\nAPELLIDOS  : {self.last_name.get()}")
        file.write(f"\nDIRECCIÓN  : {self.addres.get()}")
        file.write(f"\nCIUDAD     : {self.city.get()}")
        file.write(f"\nTELEFONO   : {self.phone.get()}")
        file.write("\n"+"-"*33)
        file.write("\n\t DESCRIPCIÓN\n")
        # Este ciclo saca de la lista cada producto que contiene la lista de precios y productos
        for i in range(len(self.item_price_tab_res)):
            resume = (f"\n{self.item_name[i]}\n\t\t\tS./ {self.item_price_tab_res[i]}")
            file.write(resume)
            i+=1
        file.write(f"\nDelivery\n\t\t\tS./ {self.delivery}")
        file.write("\n"+"-"*33)
        file.write(f"\nTOTAL\t\t\tS./{self.total_price_tab}")
        file.write(self.invoice.datetime_txt)

        file.close()

    # Creamos funcion para agregar por defecto el Delivery a la tabla de resumen
    def add_tab_resume(self):
        self.delivery = 4.99

        self.tab_resume.get_children()
        prueba = self.tab_resume.insert("", END, text = "Delivery", values = self.delivery)
        self.item_data = self.tab_resume.item(prueba)
        self.item_price = self.item_data['values']

    # Creamos funcion para agregar producto a la tabla de resumen
    def add_tab_products(self):
        # Validamos en caso de que ocurra un suceso inesperado
        self.message["text"] = ""
        try:
            self.tab.item(self.tab.selection())["text"][0]
        except IndexError as e:
            self.message["text"] = "Selecione un producto"
            return
       
        # Guardamos en un varaibles los textos seleccionados
        self.name_selection = self.tab.item(self.tab.selection())["text"]
        self.price_selection = self.tab.item(self.tab.selection())["values"][0]
        # Agregaamos a la tabla cada vez que se ejecute la funcion add_tab_products
        self.tab_resume.get_children()
        self.add_name = self.tab_resume.insert("", END, text = self.name_selection, values = self.price_selection)
        # Mesnaje de agregar productos
        self.message["text"] = f"{self.name_selection} se agregó"

        self.item_price_tab_res.append(self.price_selection)
        self.item_name.append(self.name_selection)

        self.total_price_items = 0
        # Este ciclo agrega a una lista cada vez que se agregue un producto
        for item in self.item_price_tab_res:
            self.total_price_items += float(item)

        self.total_price_tab = round(self.total_price_items + self.delivery, 2)
        self.total_price["text"] = f"S./{self.total_price_tab}"

    # Creamos funcion para eliminar productos de la tabla resumen
    def delete_resume_tab(self):
                
        # Este ciclo recoore todos los items de la tabla Resumen y las elimina
        for items in self.tab_resume.get_children():
            self.tab_resume.delete(items)

        # Vuelve a poner las listas de precio y producto vacias
        self.item_price_tab_res = []
        self.item_name = []
        # Se vuelve a iniciar con el precio del Delivery por defecto arriba de la tabla
        self.add_tab_resume()
        # Borra el precio anterior
        self.total_price["text"] = ""

    # Funcion para enviar mensjes por Whatsapp
    def send_whatasapp(self):
        
        name = f"*{self.name.get()} {self.last_name.get()}*"
        great = f"Hola {name}, gracias por comprar en *El Tornillo Feliz*\n"
        number = f"+51{self.phone.get()}"
        address = f"*{self.addres.get()}*\n"
        gratitude = self.invoice.whatsapp
        contact = self.invoice.contact
        message = great + gratitude + address + contact
        try:
            pywhatkit.sendwhatmsg_instantly(str(number), str(message), 10, None, True)
            messagebox.showinfo("Whatsapp", message = f"Se envio un mensaje de Whatsapp al cliente {self.name.get()} satisfactoriamente")
            print("Enviado a Whatassapp correctamente")

        except ValueError:
            print("Ocurrio un error")

# Aqui empieza a ejecutarse el código
if __name__ == '__main__':
    window = Tk()
    aplication = Client(window)
    window.geometry("815x605")
    window.resizable(0, 0)
    window.mainloop()