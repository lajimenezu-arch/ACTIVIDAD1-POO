class Seguimiento:
    def __init__(self):
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar(self):
        self.suma = 0
        self.x = 20
        self.suma = self.suma + self.x
        self.y = 40
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y

    def mostrar_resultado(self):
        print("EL VALOR DE LA SUMA ES:", self.suma)


programa = Seguimiento()
programa.ejecutar()
programa.mostrar_resultado()
