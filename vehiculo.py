class NodoMantenimiento:
    def __init__(self, mantenimiento):
        self.mantenimiento = mantenimiento
        self.siguiente = None

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.historial_mantenimientos = None

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, value):
        if not value: 
            raise ValueError("Ingrese datos validos")
        self._placa = value

    @property
    def año(self):
        return self._año

    @año.setter
    def año(self, value):
        if value < 1900 or value > 2025:
            raise ValueError("Ingrese una fecha valida")
        self._año = value

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, value):
        if value < 0:
            raise ValueError("El kilometraje no puede ser negativo")
        self._kilometraje = value

    def agregar_mantenimiento(self, mantenimiento):
        nuevo_nodo = NodoMantenimiento(mantenimiento)
        if not self.historial_mantenimientos:
            self.historial_mantenimientos = nuevo_nodo
        else:
            actual = self.historial_mantenimientos
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def consultar_historial(self):
        historial = []
        actual = self.historial_mantenimientos
        while actual:
            historial.append(str(actual.mantenimiento))
            actual = actual.siguiente
        return historial

    def calcular_costo_total(self):
        total = 0
        actual = self.historial_mantenimientos
        while actual:
            total += actual.mantenimiento.precio
            actual = actual.siguiente
        return total

    def __str__(self):
        return f"Placa: {self.placa}, 
                Marca: {self.marca}, 
                Modelo: {self.modelo}, 
                Año: {self.año}, 
                Kilometraje: {self.kilometraje}"