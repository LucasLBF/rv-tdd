import pytest
from src.CalculatorA import CalculatorA, CalculatorError;


@pytest.mark.parametrize("a, b, result", [(1, 1, 2), (2, 3, 5)])
def test_somar(a, b, result):
    calc = CalculatorA()
    assert calc.somar(a, b) == result

@pytest.mark.parametrize("a, b, wrong_result", [(1, 1, 3), (4, 4, 6)])
def test_somar_with_wrong_results(a, b, wrong_result):
    calc = CalculatorA()
    assert calc.somar(a, b) != wrong_result

@pytest.mark.parametrize("a, b, result", [(2, "5", 7), ("4", "4", 8), ("1", 2, 3)])
def test_somar_with_strings(a, b, result):
    calc = CalculatorA()
    with pytest.raises(CalculatorError):
        calc.somar(a, b)

def test_two_minus_one_equals_one():
    calc = CalculatorA()
    assert calc.subtrair(2, 1) == 1