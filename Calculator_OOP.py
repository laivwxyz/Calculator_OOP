# import class UserInterface
from user_interface import UserInterface
# import class Calculator
from calculator import Calculator
# import class CalculatorInheritance
from inheritance_calculator import CalculatorInheritance

# Assign variable for class
ui = UserInterface()
calc = Calculator()
inherit = CalculatorInheritance()

# Display mathematical operation
ui.operation()

while True:
    # Ask user for first and second number
    num1 = ui.input_number()
    num2 = ui.input_number()

    # Choose Operation
    operation = ui.choose_operation()
    if operation == "1":
        result = calc.addition(num1, num2)
        ui.answer(result)
    elif operation == "2":
        result = calc.subtraction(num1, num2)
        ui.answer(result)        
    elif operation == "3":
        result = calc.multiplication(num1, num2)
        ui.answer(result)
    elif operation == "4":
        result = calc.dividision(num1, num2)
        ui.answer(result)
    elif operation == "5":
        result = inherit.modulus(num1, num2)
        ui.answer(result)
    elif operation == "6":
        result = inherit.exponent(num1, num2)
        ui.answer(result)
    else:
        print()
        print("\033[91mError: \033[0mInvalid input!")
        print()
        continue

    if not ui.try_again():
        break