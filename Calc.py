class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero"
        return round(self.num1 / self.num2, 2)

# Using the class
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
calc = Calculator(n1, n2)

print("1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide")
choice = input("Choose an operation (1-4): ")

if choice == "1":
    print("Result:", calc.add())
elif choice == "2":
    print("Result:", calc.subtract())
elif choice == "3":
    print("Result:", calc.multiply())
elif choice == "4":
    print("Result:", calc.divide())
else:
    print("Invalid choice")
