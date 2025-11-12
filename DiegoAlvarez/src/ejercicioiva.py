def producto_iva(precio: float, iva: float = .16) -> float:
    '''Calcula el precio final de un producto con Iva'''
    return precio * (1 + iva)

print(f"El precio + iva es: {producto_iva(254):.2f}")