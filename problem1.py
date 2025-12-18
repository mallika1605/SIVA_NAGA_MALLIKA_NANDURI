class Calculator:
    def _init_(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "sub":
            return self.a - self.b
        elif operation == "mul":
            return self.a * self.b
        elif operation == "div":
            return self.a / self.b
        else:
            return "Invalid Operation"


a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operation (add/sub/mul/div): ")

calc = Calculator(a, b)
print("Result:", calc.calculate(op))
