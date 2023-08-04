# Elaborado por: Juan Ignacio Castro y Josué Arias
# Fecha de creación: 1/08/2020
# Ultima Modificacion: 1/08/2020 a las 10:20am
# version: 3.8.2

class Bebida():

    def __init__(self, codigo, nombre, ingredientes, precio, tamano):
        self.codigo = codigo
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.tamano = tamano

    def establecerCodigo(self, nuevoCodigo):
        """
        F: Cambia el valor del atributo codigo
        E: Nuevo valor para el atributo
        S: Se cambia el valor del atributo
        """
        self.codigo = nuevoCodigo
        return

    def retornarCodigo(self):
        """
        F: Retorna el atributo codigo
        E: Sí mismo
        S: El atributo codigo
        """
        return self.codigo

    def establecerNombre(self, nuevoNombre):
        """
        F: Cambia el valor del atributo nombre
        E: Nuevo valor para el atributo
        S: Se cambia el valor del atributo
        """
        self.nombre = nuevoNombre
        return

    def retornarNombre(self):
        """
        F: Retorna el atributo nombre
        E: Sí mismo
        S: El atributo nombre
        """
        return self.nombre

    def establecerIngredientes(self, nuevosIngredientes):
        self.ingredientes = nuevosIngredientes

    def retornarIngredientes(self):
        return self.ingredientes

    def establecerPrecio(self, nuevoPrecio):
        """
        F: Cambia el valor del atributo Creditos
        E: Nuevo valor para el atributo
        S: Se cambia el valor del atributo
        """
        self.precio = nuevoPrecio
        return

    def retornarPrecio(self):
        """
        F: Retorna el atributo creditos
        E: Sí mismo
        S: El atributo creditos
        """
        return self.precio

    def establecerTamano(self, nuevoTamano):
        """
        F: Cambia el valor del atributo requisitos
        E: Nuevo valor para el atributo
        S: Se cambia el valor del atributo
        """
        self.tamano = nuevoTamano
        return

    def retornarTamano(self):
        """
        F: Retorna el atributo requisitos
        E: Sí mismo
        S: El atributo requisitos
        """
        return self.tamano

    def informeDatosBebida(self):
        """
        F: Retorna un informe de los atributos del objeto
        E: Sí mismo
        S: El informe de los atributos
        """
        return [self.codigo, self.nombre,
                self.ingredientes, self.precio, self.tamano]


class Fria(Bebida):

    def __init__(self, codigo, nombre, ingredientes, precio, tamano):
        Bebida.__init__(self, codigo, nombre, ingredientes, precio, tamano)
        self.hielo = False
        self.categoria = False

    def establcerHielo(self, nuevoHielo):
        """
        F: Cambia el valor del atributo requisitos
        E: Nuevo valor para el atributo
        S: Se cambia el valor del atributo
        """
        self.hielo = nuevoHielo

    def retornarHielo(self):
        """
        F: Retorna un informe de los atributos del objeto
        E: Sí mismo
        S: El informe de los atributos
        """
        return self.hielo

    def establecerCategoria(self, nuevaCategoria):
        """
        F: Cambia el valor del atributo requisitos
        E: Nuevo valor para el atributo
        S: Se cambia el valor del atributo
        """
        self.categoria = nuevaCategoria

    def retornarCategoria(self):
        """
        F: Retorna un informe de los atributos del objeto
        E: Sí mismo
        S: El informe de los atributos
        """
        return self.categoria

    def informeDatosFria(self):
        """
        F: Retorna un informe de los atributos del objeto
        E: Sí mismo
        S: El informe de los atributos
        """
        return [self.codigo, self.nombre, self.ingredientes,
                self.precio, self.tamano, self.hielo, self.categoria]


class Caliente(Bebida):
    def __init__(self, codigo, nombre, ingredientes, precio, tamano, tipo):
        Bebida.__init__(self, codigo, nombre, ingredientes, precio, tamano)
        self.tipo = tipo

    def establecerTipo(self, nuevoTipo):
        """
        F: Cambia el valor del atributo requisitos
        E: Nuevo valor para el atributo
        S: Se cambia el valor del atributo
        """
        self.tipo = nuevoTipo

    def retornarTipo(self):
        """
        F: Retorna un informe de los atributos del objeto
        E: Sí mismo
        S: El informe de los atributos
        """
        return self.tipo

    def informeDatosCaliente(self):
        """
        F: Retorna un informe de los atributos del objeto
        E: Sí mismo
        S: El informe de los atributos
        """
        return [self.codigo, self.nombre, self.ingredientes,
                self.precio, self.tamano, self.tipo]
