from Cometela.models import Vianda, Tamaño

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, vianda_tamaño):
        id = str(vianda_tamaño.id)
        vianda = vianda_tamaño.vianda
        tamaño = vianda_tamaño.tamaño
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "vianda_tamaño_id" : vianda_tamaño.id,
                "dia" : vianda.dia,
                "tipo" : vianda.tipo,
                "tamaño" : tamaño.tamaño,
                "acumulado" : tamaño.precio,
                "cantidad": 1,
                "menu": vianda.descripcion,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += tamaño.precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, vianda_tamaño):
        id = str(vianda_tamaño.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, vianda_tamaño):
        id = str(vianda_tamaño.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= vianda_tamaño.tamaño.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(vianda_tamaño)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True


