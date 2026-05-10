class Director:
    _instancia = None

#Aca se mira la instancia vacía y después se crea la instancia  

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

  # Aca se inicializa y se le coloca los usuarios 
    def __init__(self):
        # Protegemos para que no se reinicialice
        if not hasattr(self, '_listo'):
            self.nombre = "Carlos Pérez"
            self.decisiones = []
            self._listo = True

    def tomar_decision(self, decision):
        self.decisiones.append(decision)
        print(f"Director {self.nombre} decidió: {decision}")


#Ahora pediremos decisiones al director 

director_en_ventas = Director()
director_en_ventas.tomar_decision("Bajar precios un 10%")

# El módulo de RH lo pide
director_en_rh = Director()
director_en_rh.tomar_decision("Contratar 3 personas")

print(director_en_ventas is director_en_rh)  
print(director_en_ventas.decisiones)
