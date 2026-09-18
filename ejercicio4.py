class CalculoPotencias:
    def __init__(self, numero: float):
        self.numero = numero
        self.cuadrado = 0.0
        self.cubo = 0.0

    def calcular_potencias(self):
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3

    def mostrar_resultados(self):
        print(f"Número ingresado: {self.numero}")
        print(f"Cuadrado: {self.cuadrado}")
        print(f"Cubo: {self.cubo}")

if __name__ == "__main__":
    try:
        num = float(input("Ingrese un número: "))
        calc = CalculoPotencias(num)
        calc.calcular_potencias()
        calc.mostrar_resultados()
    except ValueError:
        print("Debe ingresar un valor numérico válido.")
