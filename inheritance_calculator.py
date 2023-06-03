from calculator import Calculator

# Creating a class named CalculatorInheritance
class CalculatorInheritance(Calculator):
    # Modulus,
    def modulus(self, num1, num2):
        # if the user choose modulus,
        result = num1 % num2
        return result