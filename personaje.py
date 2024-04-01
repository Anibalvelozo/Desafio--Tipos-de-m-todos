class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def get_estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def set_estado(self, experiencia):
        temp_exp = self.experiencia + experiencia
        if temp_exp >= 0:
            self.experiencia = temp_exp
            self.nivel = 1 + temp_exp // 100
        else:
            self.experiencia = 0
            if self.nivel > 1:
                self.nivel -= 1

    def __lt__(self, other):
        return self.nivel < other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel

    # Método opcional
    def probabilidad_ganar(self, otro):
        if self < otro:
            return 0.33
        elif self > otro:
            return 0.66
        else:
            return 0.5

    # Método opcional
    @staticmethod
    def enfrentamiento_dialogo(jugador, orco):
        probabilidad = jugador.probabilidad_ganar(orco) * 100
        print(f"¡Oh no!, ¡Ha aparecido un Orco! Con tu nivel actual, tienes {probabilidad}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")

        while True:
            opcion = input("¿Qué deseas hacer? 1. Atacar 2. Huir ")
            if opcion in ['1', '2']:
                return int(opcion)
            else:
                print("Por favor, ingresa una opción válida (1 o 2).")
