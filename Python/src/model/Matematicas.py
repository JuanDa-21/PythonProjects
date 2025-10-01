class Matematicas:
    @staticmethod
    def fun_restar(numero_uno,numero_dos):
        return numero_uno-numero_dos
    @staticmethod
    def fun_sumar(numero_uno,numero_dos):
        return numero_uno+numero_dos
    @staticmethod
    def fun_multiplicar(numero_uno,numero_dos):
        return numero_uno*numero_dos
    @staticmethod
    def fun_division(numero_uno,numero_dos):
        try:
            if numero_dos == 0:
                return "Error no se puede dividir por cero."
            return numero_uno / numero_dos
        except Exception as e:
            return f"Error en la division:{str(e)}"
    
    