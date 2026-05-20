   def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, '_listo'):
            self.nombre = "Carlos Pérez"
            self.decisiones = []
            self._listo = True

    def tomar_decision(self, decision):
        self.decisiones.append(decision)
        print(f"Director {self.nombre} decidió: {decision}")


# FACADE 
class DirectorFacade:
    """
    Fachada: los módulos externos solo hablan con esta clase.
    Ellos no saben que adentro existe un Singleton ni cómo funciona.
    """
    def __init__(self):
        # El Facade obtiene (o crea) la única instancia del Director
        self._director = Director()

    def decision_ventas(self, texto):
        # Podría hacer validaciones, logs, etc. antes de llamar al Director
        print("[Ventas → Facade]")
        self._director.tomar_decision(f"[VENTAS] {texto}")

    def decision_rh(self, texto):
        print("[RH → Facade]")
        self._director.tomar_decision(f"[RH] {texto}")

    def ver_historial(self):
        return self._director.decisiones


#USO 
facade = DirectorFacade()

facade.decision_ventas("Bajar precios un 10%")
facade.decision_rh("Contratar 3 personas")

print(facade.ver_historial())
