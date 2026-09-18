class EmpleadoCalculo:
    def __init__(self, horas_trabajadas: float, valor_hora: float, porcentaje_retencion: float):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = 0.0
        self.retencion_fuente = 0.0
        self.salario_neto = 0.0

    def calcular_liquidaciones(self):
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        self.retencion_fuente = self.salario_bruto * (self.porcentaje_retencion / 100)
        self.salario_neto = self.salario_bruto - self.retencion_fuente

    def mostrar_liquidacion(self):
        print("--- LIQUIDACIÓN DEL EMPLEADO ---")
        print(f"Salario Bruto: ${self.salario_bruto:,.2f}")
        print(f"Retención en la Fuente ({self.porcentaje_retencion}%): ${self.retencion_fuente:,.2f}")
        print(f"Salario Neto: ${self.salario_neto:,.2f}")

if __name__ == "__main__":
    # Datos definidos según el enunciado
    HORAS = 48
    VALOR_HORA = 5000
    PORCENTAJE_RETENCION = 12.5

    emp = EmpleadoCalculo(HORAS, VALOR_HORA, PORCENTAJE_RETENCION)
    emp.calcular_liquidaciones()
