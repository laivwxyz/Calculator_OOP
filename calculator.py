# Creating a class named Calculator
class Calculator:
# Performing the chosen operation
    # Addition,
    def addition(self, num1, num2):
        # if the user choose addition,
        print("\033[96m>" * 5, "\033[0m The mathematical operation you choose is \033[93mAddition")
        result = num1 + num2
        return result
    
    # Subtraction
    def subtraction(self, num1, num2):
        # if the user choose subtraction,
        print("\033[96m>" * 5, "\033[0m The mathematical operation you choose is \033[94mSubtraction")
        result = num1 - num2
        return result
    
    # Multiplication
    def multiplication(self, num1, num2):
        # if the user choose multiplication,
        print("\033[96m>" * 5, "\033[0m The mathematical operation you choose is \033[91mMultiplication")
        result = num1 * num2
        return result
    
    # Division
    def dividision(self, num1, num2):
        try:
            # if the user choose division,
            print("\033[96m>" * 5, "\033[0m The mathematical operation you choose is \033[95mDivision")
            result = num1 / num2
            return result
        except ZeroDivisionError:
            print()
            print("\033[91mError: \033[0mCannot divide by zero.")
            print()