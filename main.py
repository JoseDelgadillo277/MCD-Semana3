class CalculadoraMCD:
    def __init__(self):
        self._numero1 = None
        self._numero2 = None

    # Getter y Setter para numero1
    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El número debe ser un entero positivo.")
        self._numero1 = value

    # Getter y Setter para numero2
    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El número debe ser un entero positivo.")
        self._numero2 = value

    def calcular_mcd(self):
        """
        Calcula el Máximo Común Divisor (MCD) usando el algoritmo de Euclides.
        """
        a, b = self.numero1, self.numero2
        while b != 0:
            a, b = b, a % b
        return a


def solicitar_numero(mensaje):
    """
    Solicita un número entero positivo al usuario con validación.
    """
    while True:
        try:
            num = int(input(mensaje))
            if num <= 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                return num
        except ValueError:
            print("Entrada inválida. Intente nuevamente con un número entero.")


# Programa principal
def main():
    calc = CalculadoraMCD()

    # Solicitar y asignar números utilizando setters
    calc.numero1 = solicitar_numero("Ingrese el primer número entero positivo: ")
    calc.numero2 = solicitar_numero("Ingrese el segundo número entero positivo: ")

    # Mostrar resultado
    resultado = calc.calcular_mcd()
    print(f"El Máximo Común Divisor de {calc.numero1} y {calc.numero2} es: {resultado}")


if __name__ == "__main__":
    main()
