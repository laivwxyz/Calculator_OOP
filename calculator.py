# Import UserInterface for ZeroDivision error
from user_interface import UserInterface
ui = UserInterface()

# Creating a class named Calculator
class MathematicalOperator:
# Performing the chosen operation
    # Addition,
    def addition(self, num1, num2):
        # if the user choose addition,
        result = num1 + num2
        return result
    
    # Subtraction
    def subtraction(self, num1, num2):
        # if the user choose subtraction,
        result = num1 - num2
        return result
    
    # Multiplication
    def multiplication(self, num1, num2):
        # if the user choose multiplication,
        result = num1 * num2
        return result
    
    # Division
    def dividision(self, num1, num2):
        try:
            # if the user choose division,
            result = num1 / num2
            return result
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            num1 = ui.input_number()
            num2 = ui.input_number()