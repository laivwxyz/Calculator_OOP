# import class UserInterface
from user_interface import UserInterface
# import class Calculator
from calculator import Calculator

# Assign variable for class
ui = UserInterface()
calc = Calculator()

# Display mathematical operation
ui.operation()

while True:
    # Ask user for first and second number
    num1 = ui.input_number()
    num2 = ui.input_number()

    # Choose Operation
    operation = ui.choose_operation()
    if operation == "1":
        sum = calc.addition(num1, num2)
        ui.answer(sum)
