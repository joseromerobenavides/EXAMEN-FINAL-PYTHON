class Hotel(object):
    """ Hotel: sus atributos son: nombre, ubicacion, puntaje y precio."""

    def __init__(self, nombre = '*', ubicacion = '*',
                 puntaje = 0, precio = float("inf")):
        """ nombre y ubicacion deben ser cadenas no vacías,
            puntaje y precio son números.
            Si el precio es 0 se reemplaza por infinito. """

        if es_cadena_no_vacia (nombre):
            self.nombre = nombre
        else:
            raise TypeError ("El nombre debe ser una cadena no vacía")

        if es_cadena_no_vacia (ubicacion):
            self.ubicacion = ubicacion
        else:
            raise TypeError ("La ubicación debe ser una cadena no vacía")

        if es_numero(puntaje):
            self.puntaje = puntaje
        else:
            raise TypeError ("El puntaje debe ser un número")

        if es_numero(precio):
            if precio != 0:
                self.precio = precio
            else:
                self.precio = float("inf")
        else:
            raise TypeError("El precio debe ser un número")

    def __str__(self):
        """ Muestra el hotel según lo requerido. """
        return self.nombre + " de "+ self.ubicacion+ \
                " - Puntaje: "+ str(self.puntaje) + " - Precio: "+ \
                str(self.precio)+ " pesos."

>>> h1=Hotel("Hotel 1* normal", "MDQ", 1, 10)
>>> h2=Hotel("Hotel 2* normal", "MDQ", 2, 40)
>>> h3=Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
>>> h4=Hotel("Hotel vale la pena" ,"MDQ", 4, 130)
>>> lista = [ h1, h2, h3, h4 ]
>>> lista.sort()
>>> for hotel in lista:
...     print hotel
...
Hotel 3* carisimo de MDQ - Puntaje: 3 - Precio: 130 pesos.
Hotel 1* normal de MDQ - Puntaje: 1 - Precio: 10 pesos.
Hotel 2* normal de MDQ - Puntaje: 2 - Precio: 40 pesos.
Hotel vale la pena de MDQ - Puntaje: 4 - Precio: 130 pesos.

def cmpPrecio(self, otro):
    """ Compara dos hoteles por su precio. """
    return cmp(self.precio, otro.precio)

def cmpPuntaje(self, otro):
    """ Compara dos hoteles por su puntaje. """
    return cmp(self.puntaje, otro.puntaje)

>>> h1 = Hotel("Hotel Guadalajara", "Pinamar", 2, 55)
>>> h2 = Hotel("Hostería París", "Rosario", 1, 35)
>>> h3 = Hotel("Apart-Hotel Estocolmo", "Esquel", 3, 105)
>>> h4 = Hotel("Posada El Cairo", "Salta", 2.5, 15)
>>> lista = [ h1, h2, h3, h4 ]
>>> lista.sort(cmp=Hotel.cmpPrecio)
>>> for hotel in lista:
...     print hotel
...
Posada El Cairo de Salta - Puntaje: 2.5 - Precio: 15 pesos.
Hostería París de Rosario - Puntaje: 1 - Precio: 35 pesos.
Hotel Guadalajara de Pinamar - Puntaje: 2 - Precio: 55 pesos.
Apart-Hotel Estocolmo de Esquel - Puntaje: 3 - Precio: 105 pesos.