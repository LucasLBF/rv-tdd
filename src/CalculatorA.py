
class CalculatorError(Exception):
    def __init__(self, error_msg: str):
        pass

class CalculatorA:
    def somar(self, a: int, b: int) -> int:
        self._check_type(a)
        self._check_type(b)
        return a + b
    
    def subtrair(self, a: int, b: int) -> int:
        return a - b

    def _check_type(self, arg) -> None:
        if (type(arg) != int):
            raise CalculatorError(f"{arg} não é um número")