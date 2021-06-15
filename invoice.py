# Importamos el módulo datetime para obtener la fecha y hora actual
import datetime

class Invoice:
    # Guardamos el metodo datetime en la variable get_date
    get_date = datetime.datetime.now()
    # Creamos el formato imprimible
    invoice_txt = f'''   EL TORNILLO FELIZ

    RUC : 00000000000
        Juliaca

Av. Tangamandapio Nro 123
CEL : 910594824
---------------------------------    
BOLETA DE VENTA ELECTRÓNICA
            BB00-00
Fecha de emision: {get_date.strftime('%d/%m/%Y')}
--------------------------------
'''

    datetime_txt =f'''
---------------------------------
\t{get_date.strftime('%d/%m/%Y %H:%M:%S')}
    
'''

    example = ''' 
------------------------------  
AQUI IRA LOS ARTICULOS QUE COMPRÓ
Item 1  : Precio
Item 2  : Precio
Item 3  : Precio
Item 4  : Precio
Item 5  : Precio
Item 6  : Precio
Item 7  : Precio
TOTAL   : 000000
------------------------------
FECHA Y HORA DE LA COMPRA '''
    
    whatsapp = """ 
📦 Ya procesamos tu pedido, te pedimos que estes atento a nuestro colaborador que en un apróximado de 30 minutos estará en tu domicilio en """

    contact = """
_Hecho con el ♥ y por la nota por Kenyi Hancco_
_© Copyright 2021 - Todos los derechos reservados._

_¿Quieres saber más de mí?_
_Visita mi pagina web ⬇_
_http://kenyihq.com_"""