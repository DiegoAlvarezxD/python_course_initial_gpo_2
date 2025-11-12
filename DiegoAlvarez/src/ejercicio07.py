class Producto():
    '''Clase que respresenta un producto con nombre'''
    
    
    def __init__(self, nombre: str):
        '''Constructor de la clase Producto'''
        self._nombre = nombre
        
    @property
    def nombre(self) -> str:
        ''' Permite acceder a la propiedad nombre de manera segura'''
        return self._nombre
        
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if(len(nuevo_nombre) < 1):
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nuevo_nombre

producto = Producto("Lap")

print(f"El Nombre del producto es: {producto.nombre}")

producto.nombre = "Laptop"

print(f"El nombre del producto es: {producto.nombre}")

