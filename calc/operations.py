class Add:
    def calculate(self, a: float, b: float) -> float:
        return a + b


class Sub:
    def calculate(self, a: float, b: float) -> float:
        return a - b


class Mul:
    def calculate(self, a: float, b: float) -> float:
        return a * b


class Div:
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class Calculator:
    def __init__(self) -> None:
        self.add = Add()
        self.sub = Sub()
        self.mul = Mul()
        self.div = Div()


if __name__ == "__main__":
    calc = Calculator()
    print("10 + 5 =", calc.add.calculate(10, 5))
    print("10 - 5 =", calc.sub.calculate(10, 5))
    print("10 * 5 =", calc.mul.calculate(10, 5))
    print("10 / 5 =", calc.div.calculate(10, 5))
