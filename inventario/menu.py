from .inventario import Inventario

class Menu:
    def __init__(self):
        self.inventario = Inventario()

    def mostrar_menu(self):
        while True:
            self.inventario.mostrar_productos()
            print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
            opcion = input("Elija opción: ")
            
            if opcion == '1':
                self.inventario.agregar_producto()
            elif opcion == '2':
                self.inventario.eliminar_producto()
            elif opcion == '3':
                self.inventario.actualizar_producto()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
