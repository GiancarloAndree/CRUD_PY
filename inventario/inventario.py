from .producto import Producto

class Inventario:
    def __init__(self):
            self.productos = {
            1: Producto(1, 'Pantalones', 200.00, 50),
            2: Producto(2, 'Camisas', 120.00, 45),
            3: Producto(3, 'Corbatas', 50.00, 30),
            4: Producto(4, 'Casacas', 350.00, 15)
        }

    def mostrar_productos(self):
        print("========================================")
        print("Lista de Productos:")
        print("========================================")
        print("#        PRODUCTO       PRECIO  STOCK"),
        for producto in self.productos.values():
            print(f"{producto.id}\t {producto.nombre}\t {producto.precio}\t {producto.stock}")
        print("========================================")

    def agregar_producto(self):
        nuevo_id = max(self.productos.keys()) + 1
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        
        self.productos[nuevo_id] = Producto(nuevo_id, nombre, precio, stock)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self):
        id = int(input("Ingrese el ID del producto a eliminar: "))
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado exitosamente.")
        else:
            print("ID de producto no encontrado.")

    def actualizar_producto(self):
        id = int(input("Ingrese el ID del producto a actualizar: "))
        if id in self.productos:
            nombre = input("Ingrese el nuevo nombre del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            stock = int(input("Ingrese el nuevo stock del producto: "))
            
            self.productos[id] = Producto(id, nombre, precio, stock)
            print("Producto actualizado exitosamente.")
        else:
            print("ID de producto no encontrado.")
