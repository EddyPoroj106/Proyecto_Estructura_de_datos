class NodoVehiculo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.siguiente = None

class FlotaVehiculos:
    def __init__(self):
        self.cabeza = None

    def registrar_vehiculo(self, vehiculo):
        nuevo_nodo = NodoVehiculo(vehiculo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_vehiculo(self, placa):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.vehiculo.placa == placa:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar_vehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.vehiculo.placa == placa:
                return actual.vehiculo
            actual = actual.siguiente
        return None

    def listar_vehiculos(self):
        vehiculos = []
        actual = self.cabeza
        while actual:
            vehiculos.append(str(actual.vehiculo))
            actual = actual.siguiente
        return vehiculos