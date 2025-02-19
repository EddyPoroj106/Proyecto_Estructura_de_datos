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

    def agregar_mantenimiento(self, mantenimiento):
        nuevo_nodo = NodoMantenimiento(mantenimiento)
        if not self.historial_mantenimientos:
            self.historial_mantenimientos = nuevo_nodo
        else:
            actual = self.historial_mantenimientos
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_historial(self):
        historial = []
        actual = self.historial_mantenimientos
        while actual:
            historial.append(str(actual.mantenimiento))
            actual = actual.siguiente
        return historial

    def precio(self):
        total = 0
        actual = self.historial_mantenimientos
        while actual:
            total = total + actual.mantenimiento.costo
            actual = actual.siguiente
        return total

    def __str__(self):
        return f"Placa: {self.placa}, 
                Marca: {self.marca}, 
                Modelo: {self.modelo}, 
                Año: {self.año}, 
                Kilometraje: {self.kilometraje}"
