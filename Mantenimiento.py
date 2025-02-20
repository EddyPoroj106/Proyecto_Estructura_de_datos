class Mantenimiento:
    def __init__(self, fecha, descripcion, precio):
        self.fecha = fecha
        self.descripcion = descripcion
        self.precio = precio

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        if not value: 
            raise ValueError("La fecha no puede estar vacia")
        self._fecha = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        if not value:  
            raise ValueError("Sin descripcion")
        self._descripcion = value

    @property
    def precio(self):
        return self.precio

    @precio.setter
    def precio(self, value):
        if value < 0: 
            raise ValueError("El precio no puede ser negativo.")
        self.precio = value

    def __str__(self):
        return f"Fecha: {self.fecha}, 
                Descripción: {self.descripcion}, 
                Costo: {self.precio}"
