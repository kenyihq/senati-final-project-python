Algoritmo TornilliFeliz
	// Definimos las varaibles a usar, tambien se define el tipo	
	Definir opc, carrito, productos Como Entero
	Definir dni, nombre, apellido, direccion, ciudad, telefono Como Caracter
	Definir producto Como Caracter
	Definir precio, precio1, precio2, precio3, precioTotal, delivery Como Real
	Definir producto1, producto2, producto3 Como Caracter
	//  Pedimos datos y las almacenamos en sus respectivos variables
	Escribir 'DNI : '
	Leer dni
	Escribir 'Apellidos : '
	Leer apellido
	Escribir 'Nombres : '
	Leer nombre
	Escribir 'Dirección : '
	Leer direccion
	Escribir 'Ciudad : '
	Leer ciudad
	Escribir 'Teléfono : '
	Leer telefono
	
	// Insertamos los produtos de la tienda
	producto1 <- 'Chipote Chillon'
	precio1 <- 99.99
	producto2 <- 'Chicharra Paralizadora'
	precio2 <- 95.99
	producto3 <- 'Pastillas de Chiquitolina'
	precio3 <- 850
	
	// Le damos un valor aleatorio dirente a 0 para que inicie el ciclo, este cilco termina
	// igresando 0
	opc <- 99
	// en carrito se agrega la cantidad de productos agregados
	carrito <- 0
	// Aqui sumaremos el precio total
	precioTotal <- 0
	// Esto sumará cada indice de la dimension itemsCompra y precioCompra
	productos <- 1
	// Asignamos valor al precio del delivery
	delivery <- 4.99
	// Creamos el tamaño de la dimensión, el cual almacenará los productos que se compre
	Dimension itemsCompra[3]
	Dimension precioCompra[3]
	
	// Iniciamos un ciclo para pedir los productos que se el cliente comprará
	Escribir 'AGREGAR PARA COMPRAR'
	Mientras (opc <> 0) Hacer
		Escribir '---------------------------'
		Escribir '[1] ', producto1, ' : ', precio1
		Escribir '[2] ', producto2, ' : ', precio2
		Escribir '[3] ', producto3, ' : ', precio3
		Escribir '---------------------------'
		Si (opc = 1) Entonces
			Escribir 'Agragaste ', producto1 
			carrito <- carrito + 1
			itemsCompra[productos] <- producto1
			precioCompra[productos] <- precio1
			precioTotal <- precioTotal + precio1
			productos <- productos + 1
		SiNo
			Si (opc = 2) Entonces
				Escribir 'Agragaste ', producto2
				carrito <- carrito + 1
				itemsCompra[productos] <- producto2
				precioCompra[productos] <- precio2
				precioTotal <- precioTotal + precio2
				productos <- productos + 1
			SiNo
				Si (opc = 3) Entonces
					Escribir 'Agragaste ', producto3
					carrito <- carrito + 1
					itemsCompra[productos] <- producto3
					precioCompra[productos] <- precio3
					precioTotal <- precioTotal + precio3
					productos <- productos + 1
				FinSi
			FinSi
		FinSi
		Escribir 'Inserte 0 para terminar'
		Leer opc		
	FinMientras
	
	Escribir 'Tienes ', carrito, ' productos en tu compra'
	precioTotal <- precioTotal + delivery
		
	// Imrimimos en pantalla la orden
	Escribir '---------------------------'
	Escribir 'EL TORNILLO FELIZ'
	Escribir ''
	Escribir  'RUC 0000000000'
	Escribir 'Juliaca'
	Escribir 'Av. Tangamandapio Nro 123'
	Escribir 'CEL : 910594824'
	Escribir '---------------------------'
	Escribir 'DATOS DEL CLIENTE'
	Escribir  ''	
	Escribir 'DNI : ', dni
	Escribir 'Nombres : ', nombre
	Escribir 'Apellidos : ', apellido	
	Escribir 'Dirección : ', direccion
	Escribir 'Ciudad : ', ciudad
	Escribir 'Teléfono : ', telefono
	Escribir '---------------------------'
	Escribir 'DESCRIPCIÓN'
	Para i <- 1 Hasta 3 Con Paso 1 Hacer
		Escribir itemsCompra[i], ' : ', precioCompra[i]
	Fin Para
	Escribir 'Delivery : ', delivery
	Escribir '---------------------------'
	Escribir 'TOTAL : ', precioTotal
	Escribir '---------------------------'
	
FinAlgoritmo
