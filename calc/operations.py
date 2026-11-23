import pytest
from calc.operations import Add, Sub, Mul, Div, Calculator


def test_add():
    op = Add()
    assert op.calculate(2, 3) == 5
    assert op.calculate(-4, 6) == 2


def test_sub():
    op = Sub()
    assert op.calculate(10, 4) == 6
    assert op.calculate(3, 8) == -5


def test_mul():
    op = Mul()
    assert op.calculate(3, 5) == 15
    assert op.calculate(-2, 4) == -8


def test_div():
    op = Div()
    assert op.calculate(10, 2) == 5
    assert pytest.approx(op.calculate(7, 2)) == 3.5


def test_div_by_zero():
    op = Div()
    with pytest.raises(ZeroDivisionError):
        op.calculate(10, 0)


def test_calculator_wrapper():
    calc = Calculator()
    assert calc.add.calculate(1, 2) == 3
    assert calc.sub.calculate(5, 2) == 3
    assert calc.mul.calculate(4, 3) == 12
    assert calc.div.calculate(8, 2) == 4
