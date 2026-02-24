class Notificador:
    def __init__(self):
        self.suscriptores = []
    
    def suscribir(self, funcion, *medios):
        if callable(funcion):
            self.suscriptores.append({
                'funcion': funcion,
                'medios': medios if medios else ['email']
            })
            print(f"Suscrito a: {', '.join(medios)}")
    
    def notificar(self, evento, datos, *medios_preferidos):
        print(f"\nNotificacion: {evento}")
        
        for s in self.suscriptores:
            medios = medios_preferidos if medios_preferidos else s['medios']
            
            for medio in medios:
                if medio in s['medios']:
                    try:
                        resultado = s['funcion'](evento, datos, medio)
                        print(f"  [{medio}] {resultado}")
                    except:
                        print(f"  Error en {medio}")
    
    def email(self, evento, datos, medio):
        if evento == "registro":
            return f"Email a {datos['email']}: Bienvenido {datos['nombre']}"
        elif evento == "factura":
            return f"Email a {datos['email']}: Factura #{datos['numero']} por ${datos['total']}"
        return f"Email: {evento}"
    
    def sms(self, evento, datos, medio):
        telefono = datos.get('telefono', 'Sin telefono')
        return f"SMS a {telefono}: {evento}"
    
    def whatsapp(self, evento, datos, medio):
        telefono = datos.get('telefono', 'Sin telefono')
        return f"WhatsApp a {telefono}: {datos.get('mensaje', evento)}"


print("=== EJERCICIO 4: NOTIFICACIONES ===")

noti = Notificador()

def callback_personalizado(evento, datos, medio):
    return f"Mensaje: {datos.get('texto', 'Hola')}"

noti.suscribir(noti.email, 'email')
noti.suscribir(noti.sms, 'sms')
noti.suscribir(noti.whatsapp, 'whatsapp')
noti.suscribir(callback_personalizado, 'email', 'sms')

datos1 = {
    'nombre': 'Laura',
    'email': 'laura@mail.com',
    'telefono': '3001112233'
}

noti.notificar('registro', datos1, 'email', 'whatsapp')

datos2 = {
    'email': 'cliente@mail.com',
    'telefono': '3104445566',
    'numero': 'F001',
    'total': 1500,
    'texto': 'Su factura esta lista'
}

noti.notificar('factura', datos2, 'email', 'sms')