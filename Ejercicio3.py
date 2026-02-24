class Cliente:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get('nombre', '')
        self.id = kwargs.get('id', '')
        self.email = kwargs.get('email', '')


class GestionServicios:
    def __init__(self):
        self.catalogo = {
            'software': {'nombre': 'Desarrollo Software', 'precio': 1000},
            'soporte': {'nombre': 'Soporte Tecnico', 'precio': 500},
            'consultoria': {'nombre': 'Consultoria', 'precio': 800},
            'qa': {'nombre': 'Auditoria QA', 'precio': 600}
        }
        self.seleccionados = []
    
    def agregar(self, *args):
        for item in args:
            if isinstance(item, str):
                if item in self.catalogo:
                    self.seleccionados.append(self.catalogo[item].copy())


class Facturacion:
    def __init__(self, cliente, servicios):
        self.cliente = cliente
        self.servicios = servicios
        self.subtotal = 0
        self.descuento = 0
        self.total = 0
        self.descuentos = {
            'ninguno': 0,
            'basico': 5,
            'premium': 10,
            'vip': 15
        }
    
    def calcular_subtotal(self):
        self.subtotal = 0
        for servicio in self.servicios:
            self.subtotal += servicio['precio']
        return self.subtotal
    
    def aplicar_descuento(self, tipo):
        if tipo in self.descuentos:
            porcentaje = self.descuentos[tipo]
            self.descuento = self.subtotal * porcentaje / 100
            self.total = self.subtotal - self.descuento
            print(f"Descuento {tipo}: {porcentaje}%")
        else:
            print("Tipo de descuento no valido")
    
    def generar_factura(self, *notas, **opciones):
        self.calcular_subtotal()
        
        iva = opciones.get('iva', False)
        moneda = opciones.get('moneda', 'USD')
        
        print("\n" + "="*40)
        print("FACTURA")
        print("="*40)
        
        print(f"Cliente: {self.cliente.nombre}")
        print(f"ID: {self.cliente.id}")
        print(f"Email: {self.cliente.email}")
        
        print("\nServicios:")
        for servicio in self.servicios:
            print(f"  - {servicio['nombre']}: ${servicio['precio']}")
        
        print(f"\nSubtotal: ${self.subtotal}")
        print(f"Descuento: -${self.descuento}")
        
        if iva:
            valor_iva = self.total * 0.19
            print(f"IVA 19%: ${valor_iva:.2f}")
            print(f"Total: ${self.total + valor_iva:.2f} {moneda}")
        else:
            print(f"Total: ${self.total:.2f} {moneda}")
        
        if notas:
            print("\nNotas:")
            for nota in notas:
                print(f"  * {nota}")
        
        print("="*40)


print("=== EJERCICIO 3: FACTURACION ===")

cliente = Cliente(nombre="Carlos Perez", id="C003", email="carlos@mail.com")

servicios = GestionServicios()
servicios.agregar('software', 'qa')

factura = Facturacion(cliente, servicios.seleccionados)
factura.calcular_subtotal()
factura.aplicar_descuento('premium')
factura.generar_factura("Pago a 30 dias", "Gracias por su compra", iva=True, moneda="COP")