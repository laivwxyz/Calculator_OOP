from calculator import Calculator

# Creating a class named CalculatorInheritance
class CalculatorInheritance(Calculator):
    # Modulus,
    def modulus(self, num1, num2):
        # if the user choose modulus,
        print()
        print("\033[96m>" * 5, "\033[0m The mathematical operation you choose is \033[91mModulus")
        result = num1 % num2
        return result

    # Exponent,
    def exponent(self, num1, num2):
        # if the user choose exponent,
        print()
        print("\033[96m>" * 5, "\033[0m The mathematical operation you choose is \033[92mExponent")
        result = num1 ** num2
        return result