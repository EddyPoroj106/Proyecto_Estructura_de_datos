class Mantenimiento:
    def __init__(self, fecha, descripcion, precio):
        self.fecha = fecha
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}, Costo: {self.precio}"