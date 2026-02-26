class MySQL:
    def guardar(self, data): ...

class PedidoService:
    def __init__(self):
        self.db = MySQL()  # acoplado

    def crear(self, data):
        self.db.guardar(data)
# cambiar a Postgres?
# → hay que reescribir PedidoService

# con DIP
class Database:
    def guardar(self, data): ...

class MySQL(Database):
    def guardar(self, data): ...

class PedidoService:
    def __init__(self, db: Database):
        self.db = db  # inyectado

    def crear(self, data):
        self.db.guardar(data)
# cambiar DB  sin necesidad de tocar PedidoService