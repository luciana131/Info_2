# Se quiere hacer un sistema de maquinas hospitalarias usando POO
# La máquina padre contiene atributos y parametros de que pueden estar en todas las demás
# Las maquinas hijas contienen 3 atributos especificos de sus maquinas
# Todas entregan su información a través del uso de __str__()
# Inicialmente definimos una clase padre

class Maquina:
    def __init__(self, cantidad, precio, proveedor, estado):
        self.__cantidad = cantidad
        self.__precio = precio
        self.__proveedor = proveedor
        self.__estado = estado
          
    @property            # @property - GETTER
    def estado(self):    
        return self.__estado
    @estado.setter       # @nombrevariable.setter
    def estado(self, estado):
        self.__estado = estado
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
    @property
    def proveedor(self):
        return self.__proveedor
    @proveedor.setter
    def proveedor(self, proveedor):
        self.__proveedor = proveedor
    
    def __str__(self):
        return f'El estado del implante es {self.estado}'

class RM(Maquina):
    def __init__(self, cantidad, precio, proveedor, teslas):
        super().__init__(cantidad, precio, proveedor)
        self.__teslas = teslas
        
    @property
    def teslas(self):
        return self.__teslas
    @teslas.setter
    def teslas(self, teslas):
        self.__teslas = teslas
        
    def __str__(self):
        return f'{super().__str__()}, {self.teslas}'

class Hospital:
    def __init__(self, nMedicos, Nombre):
        self.nMedicos = nMedicos
        self.Nombre = Nombre
        self.Maquinas = []
        
    def anadirMaquina(self, maquina):
        self.Maquinas.append(maquina)
        
    def __str__(self):
        return f'{self.Nombre}, {self.nMedicos}'

name = "Hospital 1"
medicoz = 5
hos = Hospital(medicoz, name)
print(hos)

Hospitales = []
while True:
    menu = input("1. Crear hospital\n2.Crear maquina\n3.Salir\n4.Seguimiento\nR: ")
    if menu == '3':
        break
    elif menu == '1':
        nMedicos = input("Ingrese el numero de médicos: ")
        Nombre = input("Ingrese el Nombre: ")
        hospital = Hospital(nMedicos, Nombre)
        Hospitales.append(hospital)
    elif menu == '2':
        for i, j in enumerate(Hospitales):
            print(f'{i}. {j.Nombre}')
        k = int(input("Seleccionar hospital a añadir la maquina: "))
        Hospitales[k].anadirMaquina(RM(1,1,1,1))
        
        
