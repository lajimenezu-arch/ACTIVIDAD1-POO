import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
        self.area = 0.0
        self.longitud = 0.0

    def calcular_area(self) -> float:
        self.area = math.pi * (self.radio ** 2)
        return self.area

    def calcular_longitud(self) -> float:
        self.longitud = 2 * math.pi * self.radio
        return self.longitud

    def mostrar_resultados(self):
        print(f"Radio del círculo: {self.radio}")
        print(f"Área: {self.area:.4f}")
        print(f"Longitud de la circunferencia: {self.longitud:.4f}")

if __name__ == "__main__":
    try:
        r = float(input("Ingrese el radio del círculo: "))
        if r < 0:
            print("El radio no puede ser negativo.")
        else:
            circ = Circulo(r)
            circ.calcular_area()
            circ.calcular_longitud()
            circ.mostrar_resultados()
    except ValueError:
        print("Entrada inválida. Ingrese un valor numérico.")
