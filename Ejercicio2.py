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
        print("Agregando servicios:")
        for item in args:
            if isinstance(item, str):
                if item in self.catalogo:
                    self.seleccionados.append(self.catalogo[item].copy())
                    print(f"  + {self.catalogo[item]['nombre']}")
                else:
                    print(f"  x Servicio '{item}' no existe")
            elif isinstance(item, dict):
                if 'nombre' in item and 'precio' in item:
                    self.seleccionados.append(item)
                    print(f"  + {item['nombre']} (personalizado)")
    
    def mostrar(self):
        if not self.seleccionados:
            print("No hay servicios")
            return
        
        print("\nServicios contratados:")
        total = 0
        for i, s in enumerate(self.seleccionados, 1):
            print(f"  {i}. {s['nombre']} - ${s['precio']}")
            total += s['precio']
        print(f"Total: ${total}")


print("=== EJERCICIO 2: GESTION DE SERVICIOS ===")

servicios = GestionServicios()
servicios.agregar('software', 'soporte', 'redes', {'nombre': 'Mantenimiento', 'precio': 300})
servicios.mostrar()