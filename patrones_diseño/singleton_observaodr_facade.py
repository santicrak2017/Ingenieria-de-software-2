
class Director:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, '_listo'):
            self.nombre = "Carlos Pérez"
            self.decisiones = []
            self._observadores = []
            self._listo = True

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def _notificar(self, decision):
        for obs in self._observadores:
            obs.actualizar(decision)

    def tomar_decision(self, decision):
        self.decisiones.append(decision)
        print(f"\nDirector {self.nombre} decidió: {decision}")
        self._notificar(decision)



class Observador:
    def actualizar(self, decision):
        raise NotImplementedError

class DepartamentoVentas(Observador):
    def actualizar(self, decision):
        print(f"  [Ventas recibió notificación]: '{decision}'")

class DepartamentoRH(Observador):
    def actualizar(self, decision):
        print(f"  [RH recibió notificación]: '{decision}'")

class DepartamentoFinanzas(Observador):
    def actualizar(self, decision):
        print(f"  [Finanzas recibió notificación]: '{decision}'")



class DirectorFacade:
    def __init__(self):
        self._director = Director()
        self._director.agregar_observador(DepartamentoVentas())
        self._director.agregar_observador(DepartamentoRH())
        self._director.agregar_observador(DepartamentoFinanzas())

    def decision_ventas(self, texto):
        print("[Ventas → Facade]")
        self._director.tomar_decision(f"[VENTAS] {texto}")

    def decision_rh(self, texto):
        print("[RH → Facade]")
        self._director.tomar_decision(f"[RH] {texto}")

    def ver_historial(self):
        return self._director.decisiones



facade = DirectorFacade()
facade.decision_ventas("Bajar precios un 10%")
facade.decision_rh("Contratar 3 personas")
print("\nHistorial completo:", facade.ver_historial())
