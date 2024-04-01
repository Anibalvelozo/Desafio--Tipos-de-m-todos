import random
from personaje import Personaje

class Juego:
    def __init__(self):
        print("¡Bienvenido a Gran Fantasía!")
        nombre_personaje = input("Por favor, indique nombre de su personaje: ")
        self.jugador = Personaje(nombre_personaje)
        print(self.jugador.get_estado())

        self.orco = Personaje("Orco")
        print(self.orco.get_estado())

    def ataque(self):
        opcion = Personaje.enfrentamiento_dialogo(self.jugador, self.orco)
        if opcion == 1:
            resultado_ataque = random.uniform(0, 1) <= self.jugador.probabilidad_ganar(self.orco)
            if resultado_ataque:
                print("¡Le has ganado al orco, felicidades! ¡Recibirás 50 puntos de experiencia!")
                self.jugador.set_estado(50)
                self.orco.set_estado(-30)
            else:
                print("¡Oh no! ¡El orco te ha ganado! ¡Has perdido 30 puntos de experiencia!")
                self.jugador.set_estado(-30)
                self.orco.set_estado(50)

            print(self.jugador.get_estado())
            print(self.orco.get_estado())

            return True

        else:
            print("¡Has huido! El orco ha quedado atrás.")
            return False

    def jugar(self):
        while True:
            if self.ataque():
                continue
            else:
                break

if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
