class Cliente:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get('nombre', '')
        self.id = kwargs.get('id', '')
        self.email = kwargs.get('email', '')
        self.direccion = kwargs.get('direccion', '')
        self.telefono = kwargs.get('telefono', '')
        
        for key, value in kwargs.items():
            if key not in ['nombre', 'id', 'email', 'direccion', 'telefono']:
                setattr(self, key, value)
    
    def mostrar_info(self):
        print("--- Informacion del Cliente ---")
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Email: {self.email}")
        print(f"Direccion: {self.direccion}")
        print(f"Telefono: {self.telefono}")
        
        for key, value in self.__dict__.items():
            if key not in ['nombre', 'id', 'email', 'direccion', 'telefono']:
                print(f"{key}: {value}")


print("=== EJERCICIO 1: REGISTRO DE CLIENTES ===")

cliente1 = Cliente(
    nombre="Luis Fernando",
    id="C001",
    email="luis@mail.com",
    direccion="Calle 10 #20-30",
    telefono="3001234567",
    ciudad="Bogota",
    empresa="ACME"
)

cliente2 = Cliente(
    nombre="Ana Maria",
    id="C002",
    email="ana@mail.com",
    telefono="3107654321",
    pais="Colombia"
)

cliente1.mostrar_info()
cliente2.mostrar_info()