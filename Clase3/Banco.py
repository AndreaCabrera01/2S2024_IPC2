class Banco:
    def __init__(self, nombre, direccion, antiguedad, sucursales, clientes):
        self.nombre = nombre
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.sucursales = sucursales
        self.clientes = clientes

    def __str__(self):
        return f'BANCO: {self.nombre} \n Ubicado en: {self.direccion} \n Posee {self.antiguedad} años de antiguedad \nTiene {self.sucursales} sucursales\n'
    
    def promedio(self):
        suma = 0
        for cliente in self.clientes:
            suma += cliente.saldo
        return int(suma/len(self.clientes))